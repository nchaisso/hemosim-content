# Central references pass over the Informed pages. Written 2026-08-15.
#
# File 04 requires this be ONE pass, not one per module: per-module citation work
# drifts in format and cannot see a citation orphaned on another page. Run it after
# any batch of module work.
#
#   python3 verify_refs.py            # all Informed pages
#   python3 verify_refs.py i4 i9      # named pages
#
# It pulls every entry out of each page's <div class="refs">, resolves the DOI to a
# PMID through PubMed, and checks the page's citation text against the real record.
# It reports unresolvable DOIs, author and year mismatches, PMC links claimed that
# do not exist, free full text that exists but is not linked, and any reference
# cited on more than one page.
#
# On 2026-08-15 it verified 300 references across fifteen pages and found three
# problems, none of them a wrong citation.
#
# TWO BUGS TO NOT REINTRODUCE, both of which made the first run accuse a dozen
# correct references of fabricating links:
#   1. elink treats a comma-joined id list as a SET and returns one merged
#      linkset. Repeat the id parameter instead, one linkset per PMID.
#   2. Decode HTML entities before comparing author names, or every page carrying
#      "Ospina-Tasc&oacute;n" reports an author mismatch.

# Central references pass over the Informed pages.
#
# File 04: "References are one pass, not ten." Per-module citation work drifts in
# format and cannot see a citation orphaned on another page. This does the pass.
#
# For every <div class="refs"> entry on every page: pull the DOI out of the link,
# resolve it to a PMID through PubMed, fetch the authoritative record, and compare
# the page's citation string against it. Reports mismatches, unresolvable DOIs,
# and PMC links that are claimed but do not exist.

import html as htmlmod
import json, os, re, subprocess, sys, time, urllib.parse

WEB = '/Users/chaissn/Claude/hemosim-web'
E = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'


def get(url):
    # curl rather than urllib, 2026-09-12: the sandboxed sessions let curl out and
    # block urllib, so the pass silently found nothing. Same fix as build_refs.py.
    # -g turns off curl's URL globbing, which otherwise chokes on the [doi] field tag.
    for attempt in range(3):
        time.sleep(0.35)                      # NCBI allows three requests a second without a key
        r = subprocess.run(['curl', '-s', '-g', '-m', '30', url], capture_output=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.decode('utf-8', 'replace')
        if attempt == 2:
            return ''
        time.sleep(2)
    return ''


def refs_of(path):
    html = open(path).read()
    m = re.search(r'<div class="refs">.*?</div>', html, re.S)
    if not m:
        return []
    out = []
    for li in re.findall(r'<li>(.*?)</li>', m.group(0), re.S):
        doi = re.search(r'href="https://doi\.org/([^"]+)"', li)
        pmc = re.search(r'articles/PMC(\d+)', li)
        pmid = re.search(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)', li)
        # Decode entities before comparing. The pages carry accented author names
        # as &oacute; and friends, so a raw comparison against PubMed's "Ospina-
        # Tascón" reports an author mismatch on a perfectly correct citation.
        text = htmlmod.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]*>', '', li))).strip()
        out.append({'text': text, 'doi': doi.group(1) if doi else None,
                    'pmc': pmc.group(1) if pmc else None,
                    'pmid_link': pmid.group(1) if pmid else None})
    return out


def resolve(doi):
    j = get(E + 'esearch.fcgi?db=pubmed&retmode=json&term=%s[doi]'
            % urllib.parse.quote(doi))
    try:
        ids = json.loads(j)['esearchresult']['idlist']
    except Exception:
        return None
    return ids[0] if ids else None


def summarise(pmids):
    if not pmids:
        return {}
    j = get(E + 'esummary.fcgi?db=pubmed&retmode=json&id=' + ','.join(pmids))
    try:
        return json.loads(j)['result']
    except Exception:
        return {}


def pmc_of(pmids):
    """One linkset per PMID.

    A comma-joined id list is WRONG here: elink treats it as a set and returns a
    single merged linkset, so only the first PMID gets attributed and every other
    reference appears to claim a PMC record that does not exist. Repeating the id
    parameter is what produces per-id linksets. This bug made the first run of
    this script accuse a dozen correct references of fabricating free-text links.
    """
    found = {}
    if not pmids:
        return found
    for i in range(0, len(pmids), 20):
        chunk = pmids[i:i + 20]
        j = get(E + 'elink.fcgi?dbfrom=pubmed&db=pmc&retmode=json'
                    '&linkname=pubmed_pmc&' + '&'.join('id=' + p for p in chunk))
        try:
            for ls in json.loads(j).get('linksets', []):
                ids = [str(x) for x in ls.get('ids', [])]
                if len(ids) != 1:
                    print('  ! elink returned a merged linkset, results unreliable')
                    continue
                for db in ls.get('linksetdbs', []):
                    if db.get('linkname') == 'pubmed_pmc' and db.get('links'):
                        found[ids[0]] = str(db['links'][0])
        except Exception:
            pass
    return found


pages = sys.argv[1:] or ['i%d' % n for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 11,
                                             12, 13, 14, 15, 16)]
all_rows, problems, by_doi = [], [], {}

for p in pages:
    path = os.path.join(WEB, p + '.html')
    if not os.path.exists(path):
        continue
    entries = refs_of(path)
    print('%-5s %d references' % (p, len(entries)))
    resolved = []
    for e in entries:
        pmid = e['pmid_link']
        if not pmid and e['doi']:
            pmid = resolve(e['doi'])
        e['pmid'] = pmid
        e['page'] = p
        resolved.append(e)
        if e['doi']:
            by_doi.setdefault(e['doi'].lower(), []).append((p, e['text'][:60]))
        if not pmid:
            problems.append((p, 'UNRESOLVED', e['text'][:110],
                             'doi=%s' % e['doi']))
    pm = [e['pmid'] for e in resolved if e['pmid']]
    summ, pmc = summarise(pm), pmc_of(pm)
    for e in resolved:
        if not e['pmid']:
            continue
        r = summ.get(e['pmid'], {})
        if not r:
            problems.append((p, 'NO RECORD', e['text'][:110], e['pmid']))
            continue
        year = (r.get('pubdate') or '')[:4]
        first = (r['authors'][0]['name'].split()[0] if r.get('authors') else '')
        if year and year not in e['text']:
            problems.append((p, 'YEAR', e['text'][:110],
                             'PubMed says %s (pmid %s)' % (year, e['pmid'])))
        if first and first.lower() not in e['text'].lower():
            problems.append((p, 'AUTHOR', e['text'][:110],
                             'PubMed first author %s (pmid %s)' % (first, e['pmid'])))
        real = pmc.get(e['pmid'])
        if e['pmc'] and not real:
            problems.append((p, 'PMC CLAIMED, NONE EXISTS', e['text'][:110],
                             'PMC%s' % e['pmc']))
        elif e['pmc'] and real and e['pmc'] != real:
            problems.append((p, 'PMC MISMATCH', e['text'][:110],
                             'page PMC%s, PubMed PMC%s' % (e['pmc'], real)))
        elif real and not e['pmc']:
            problems.append((p, 'FREE TEXT EXISTS, NOT LINKED', e['text'][:110],
                             'PMC%s' % real))
        e['pmc_real'] = real
        all_rows.append(e)

print('\n===== PROBLEMS =====')
for pg, kind, text, detail in problems:
    print('[%s] %-28s %s\n      %s' % (pg, kind, detail, text))
print('\n%d problems across %d verified references' % (len(problems), len(all_rows)))

print('\n===== CITED ON MORE THAN ONE PAGE =====')
for doi, uses in sorted(by_doi.items()):
    if len(uses) > 1:
        print('%s' % doi)
        for pg, t in uses:
            print('   %-5s %s' % (pg, t))

json.dump(all_rows, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'refs_verified.json'), 'w'), indent=1)

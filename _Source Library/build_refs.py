# -*- coding: utf-8 -*-
# Build a page's reference list from PubMed, so no citation string is ever typed by hand.
#
#   python3 build_refs.py 10430725 28877293 ...          # PMIDs, in the order they should appear
#   python3 build_refs.py doi:10.1056/NEJM197008272830902  # a DOI is resolved to its PMID first
#
# Prints <li> entries in the site's house format: authors (all, up to six, then et al.),
# title, journal abbreviation, year;volume(issue):pages, a DOI link, and "Free full text"
# linked to PMC only where a PMC record genuinely exists. Written 2026-09-12 for the
# N7-T3 and N7-T4 rebuild. verify_refs.py is the check that runs afterwards; this is the
# generator that makes the check boring.
import json, re, subprocess, sys, time, urllib.parse

E = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

def get(url):
    # curl rather than urllib: the sandboxed sessions this runs in let curl out
    # and block urllib, and the difference cost an hour on 2026-09-12.
    for attempt in range(3):
        r = subprocess.run(['curl', '-s', '-g', '-m', '30', url], capture_output=True)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.decode('utf-8', 'replace')
        time.sleep(2)
    return ''

def pmid_of_doi(doi):
    j = json.loads(get(E + 'esearch.fcgi?db=pubmed&retmode=json&term=' + urllib.parse.quote(doi + '[doi]')) or '{}')
    ids = j.get('esearchresult', {}).get('idlist', [])
    return ids[0] if ids else None

def pmc_of(pmid):
    j = json.loads(get(E + 'elink.fcgi?dbfrom=pubmed&db=pmc&retmode=json&linkname=pubmed_pmc&id=' + pmid) or '{}')
    try:
        return j['linksets'][0]['linksetdbs'][0]['links'][0]
    except Exception:
        return None

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def entry(pmid):
    r = json.loads(get(E + 'esummary.fcgi?db=pubmed&retmode=json&id=' + pmid))['result'][pmid]
    authors = [a['name'] for a in r.get('authors', []) if a.get('authtype', 'Author') == 'Author']
    au = ', '.join(authors[:6]) + (', et al' if len(authors) > 6 else '')
    title = r['title'].strip()
    if not title.endswith(('.', '?', '!')): title += '.'
    year = r['pubdate'].split()[0]
    vol, iss, pages = r.get('volume', ''), r.get('issue', ''), r.get('pages', '')
    # PubMed abbreviates "535-41"; the house style writes the full second number.
    m = re.match(r'^(\d+)-(\d+)$', pages)
    if m and len(m.group(2)) < len(m.group(1)):
        pages = m.group(1) + '-' + m.group(1)[:len(m.group(1)) - len(m.group(2))] + m.group(2)
    doi = next((a['value'] for a in r.get('articleids', []) if a['idtype'] == 'doi'), '')
    cite = '%s. %s %s. %s;%s%s%s.' % (au, esc(title), r['source'], year, vol, ('(%s)' % iss) if iss else '', (':%s' % pages) if pages else '')
    cite = cite.replace('..', '.').replace('?.', '?')
    if doi:
        cite += ' <a href="https://doi.org/%s">doi:%s</a>.' % (doi, doi)
    else:
        cite += ' PMID %s.' % pmid
    pmc = pmc_of(pmid)
    if pmc:
        cite += ' <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC%s/">Free full text</a>.' % pmc
    return cite

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        pmid = pmid_of_doi(arg[4:]) if arg.startswith('doi:') else arg
        if not pmid:
            print('<!-- UNRESOLVED: %s -->' % arg); continue
        print('<li>%s</li>' % entry(pmid))
        time.sleep(0.35)

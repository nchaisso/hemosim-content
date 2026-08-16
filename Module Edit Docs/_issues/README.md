# Per-module issue files

One file per module, named for its edit-doc label, for example `I14.md`. The
contents are rendered as a block at the top of that module's Word edit doc by
`_Source Library/make_edit_docs.py`.

One issue per line. Wrapped lines continue if indented. Each line starts with a
class:

- `SOURCE:` a defect in a deck, Notion page, document or the source index. Fixing
  the module alone leaves the error in circulation.
- `DECISION:` a judgement needed before the page is final.
- `NOTE:` done deliberately, worth knowing, no action needed.

Blank lines and `#` comments are ignored. A module with no file gets no block and
its doc regenerates exactly as before, which is why this is safe on the Novice
docs too.

Delete a line once it is resolved, then regenerate that module's doc.

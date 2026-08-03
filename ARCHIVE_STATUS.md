# Archive status and map

This page describes how to interpret repository paths. It is a navigation aid,
not a claim that every file has already been individually reviewed.

| Area | Interpretation | Default evidence level |
| --- | --- | --- |
| `CCT/` | Editorial reader editions of the CCT manuscript | Speculative framework |
| `PROJECTS/` | Topic-specific essays, generators, and graphs | Hypothesis or prototype |
| `SEED_VOCABULARY/` | Experimental machine-readable vocabulary | Prototype |
| `SIGNAL_IN/` | Raw incoming records preserved before synthesis | Unreviewed source material |
| `OMPU/` | Agent desks, institutional lore, frameworks, and history | Mixed historical archive |
| `Administration/` | Experimental economic and governance models | Simulation/draft |
| `GOVERNANCE/` | Proposed rules and RFCs | Proposal |
| `SONGS_IN/` | Music prompts and cultural artifacts | Creative work |
| `archive/` | Superseded repository entry points | Historical |

## Version rule

Git history is the provenance layer. A newer commit may correct or retract an
older statement, but it does not make the older statement disappear. For any
important claim, record the path and commit hash.

## Promotion rule

Repository material should be described as evidence-backed only when it has:

- a recoverable primary source;
- a clear claim boundary;
- a method or derivation that can be inspected;
- limitations and uncertainty;
- a review or reproduction record.

Everything else remains useful as hypothesis, prototype, history, or art.

## Current CCT shelf

- `CCT/v1.1a/`: image-free archival reader edition derived from Zenodo record
  `10.5281/zenodo.17573841`.
- The reader edition is published as `10.5281/zenodo.21781310`; the stable
  concept DOI for all CCT versions is `10.5281/zenodo.17573840`.
- The original illustrated DOCX remains on Zenodo as immutable provenance.
- Scientific corrections are intentionally deferred to a separately versioned
  CCT v2.0 rather than being smuggled into an editorial cleanup.

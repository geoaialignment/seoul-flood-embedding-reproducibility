# Annual embeddings separate official inundation traces from storm-candidate backgrounds beyond terrain and land cover

Eungyu Park, Taeyu Kim, and Jangwon Park

GeoAI Alignment, Inc., Daegu 41544, Republic of Korea

## Reproduce the reported numerical checks

With Python 3 (standard library only), run from this directory:

```bash
python3 reproduce_scores.py
```

The command calculates AUROC, average precision and capture at the 20% review
workload from the paired out-of-fold predictions for all three backgrounds.
The included timing, spatial exclusion and count-control prediction tables and
aggregate summaries provide the saved evidence for the other reported contrasts.
The calculation uses stored predictions, with no network or model fitting.

## Contents and scientific roles

| Path | Scientific role |
| --- | --- |
| `reproduce_scores.py` | Recalculate ranking metrics and 20% capture from B2 predictions. |
| `data/B2_*.csv` | Baseline and annual-embedding predictions for the full cohorts. |
| `data/B3_*.csv` | Prior-year and event-year timing comparison on the paired cohorts. |
| `data/B4_*.csv` | Paired predictions at 0 m, 250 m and 500 m spatial exclusions. |
| `data/B5_primary_*.csv` | Count-matched training controls. |
| `summaries/B0_*.csv` | Saved initial grouping comparison supporting supplementary context. |
| `summaries/B2_*.csv` | Pooled and fold-level full-cohort ranking results. |
| `summaries/B3_*.csv`, `B4_*.csv`, `B5_*.csv` | Saved paired uncertainty, training counts, seed and omission summaries. |
| `summaries/DSS_capture_*.csv` | Saved capture curves and pooled/fold-local workload counts. |
| `manifest.json` | Original source/output SHA256, row counts and transformation provenance. |
| `public_packages.csv` | File sizes, SHA256 and scientific roles for package contents. |
| `SOURCE_LICENSES.txt` | Provider attribution and redistribution boundaries. |
| `CITATION.cff` | Current paper title, authors and affiliation metadata. |

Site identifiers preserve clustering through stable opaque IDs. Prediction,
label and fold values are retained from the supporting numerical package.
Raw geospatial archives, provider raster products and feature-acquisition assets
are obtained from the sources documented in `SOURCE_LICENSES.txt`.

## Citation and licensing

Repository: https://github.com/geoaialignment/seoul-flood-embedding-reproducibility

Use the title and authors in `CITATION.cff` when citing this numerical package.
This repository is publicly accessible for **noncommercial academic use**.
Original code, documentation, and original contributions to derived data and
numerical summaries are provided under the
[GeoAI Alignment Academic Noncommercial Use License, version 1.0](LICENSE).

- Permitted purposes: noncommercial academic research, teaching and learning,
  scholarly peer review, and verification or reproduction of research results.
- Credit the authors and GeoAI Alignment, Inc., cite this research package,
  identify modifications, and retain the license and source notices when sharing.
- Commercial use and non-academic operational deployment are not permitted
  under this license; uses outside its scope require separate prior written
  permission. Contact: contact@geoaialign.com.

The full terms in `LICENSE` govern. This is a custom academic noncommercial
license, not an unrestricted open-source license. Third-party materials retain
their own terms; our license applies only to rights we are authorized to grant
in original contributions. See [SOURCE_LICENSES.txt](SOURCE_LICENSES.txt).

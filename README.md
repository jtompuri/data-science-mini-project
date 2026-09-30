# Party Map

How differently do Finnish parties speak in parliament, and has that changed over 2015–2026? Introduction to Data Science mini-project, University of Helsinki, autumn 2026. The plan is in `party-map-project-plan.md` and the method notes for the report are in `docs/methods.md`.

## Language and party codes

The analysis is done in numbered Jupyter notebooks written in Finnish for the team. Each notebook explains its method and results in Markdown next to the code. Reports, the blog and `docs/methods.md` are in English, and notebook 08 produces the English figures.

Party codes in all data and result files are the Finnish abbreviations: VAS, SDP, VIHR, KESK, RKP, KD, KOK, SIN (Blue Reform, 2017–19), PS. `src/config.py` maps them to Finnish names (`PARTY_NAMES_FI`) and English names (`PARTY_NAMES_EN`, `PARTY_SHORT_EN`).

## Folder layout

```text
Data/                         raw downloads (kept untouched, except one encoding fix: see below)
  dataset-*.ndjson            all plenary speeches 2015-05-12 … 2026-09-23 (Parliament open data export; git-ignored, see below)
  Eduskuntavaalit 2023 …csv   Yle election compass 2023, anonymised
  avoin_data_eduskuntavaalit_2015.csv, Avoin_data_eduskuntavaalit_2019_valintatiedot.csv   Yle election compass 2015 and 2019
  processed/                  derived tables (rebuilt by notebooks 01, 02, 04 and 05; git-ignored except mp_terms.parquet)
notebooks/                    the analysis, run in order
  01_aineiston_lataus.ipynb   NDJSON -> speeches_raw.parquet
  02_siivous.ipynb            sample rules + text cleaning -> speeches_clean.parquet, mp_terms.parquet
  03_eda.ipynb                exploratory analysis
  04_sanasto.ipynb            vocabulary (Simola/Gentzkow thresholds) -> counts.npz
  05_luokittelija.ipynb       party classifier, separability, MP profiles, diversity (+ control runs)
  06_leaveout.ipynb           Gentzkow–Shapiro–Taddy leave-out estimator (cross-check)
  07_tulokset.ipynb           results for the team (reads results/, fast)
  08_raporttikuvat.ipynb      English figures + results/summary_tables.md for the report
  09_vaalikone.ipynb          election-compass comparison 2015, 2019, 2023 (party positions vs. speech)
  10_sanat.ipynb              most distinctive words per party and term from classifier weights
  11_teemat.ipynb             separability within topics (Gronow & Malkamäki keywords), comparison with Twitter
  90_sivupolut.ipynb          informal side notes for the blog (not part of the results); run after 06
src/
  config.py                   shared definitions: parties, terms, governments, sample rules
  reporting.py                shared helpers for the results notebooks (07-09)
  stopwords_fi.txt, stopwords_sv.txt   NLTK stop-word lists (frozen copies)
  stopwords_fi_style.txt      extra style words for the robustness run party_nostyle (notebook 05)
  data_cleanup.py             column check of the raw export (see Source data)
results/                      model outputs (csv/json) and summary_tables.md
reports/figures/              figures (eda_*, tulokset_* in Finnish; res_* in English)
docs/methods.md               paper summaries, design decisions, limitations (English)
scripts/setup_venv.sh         creates the virtual environment
Canvas/                       project canvas (course submission)
Articles/                     source articles as PDFs (git-ignored: copyrighted; links in the project plan)
archive/                      outputs of earlier versions, kept locally (git-ignored)
```

## Setup

Requires Python 3.10–3.13. From the project root:

```bash
./scripts/setup_venv.sh            # creates .venv, installs requirements.txt, registers Jupyter kernel "Party Map (.venv)"
source .venv/bin/activate
jupyter lab                        # or open the notebooks in VS Code
```

If `python3` is a different version, run it as `PYTHON=python3.12 ./scripts/setup_venv.sh`. `requirements.txt` gives version ranges. `requirements-lock.txt` pins the exact versions tested, for exact reproduction. `.venv/` is git-ignored.

## Rebuild everything

Run the notebooks in the order below (08 last, because it reads the outputs of 09, 10 and 11), with the kernel "Party Map (.venv)". From the command line:

```bash
cd notebooks
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 \
  01_aineiston_lataus.ipynb 02_siivous.ipynb 03_eda.ipynb 04_sanasto.ipynb \
  05_luokittelija.ipynb 06_leaveout.ipynb 07_tulokset.ipynb 09_vaalikone.ipynb 10_sanat.ipynb \
  11_teemat.ipynb 08_raporttikuvat.ipynb
```

| notebook | time | note |
| --- | --- | --- |
| 01, 02, 03 | ~2 min | |
| 04 | ~1 min | needs ~5 GB RAM |
| 05 | ~15–55 min | five runs; also writes `Data/processed/party_oof.parquet` and `party_nostyle_oof.parquet` for notebook 11; lower `TOISTOT` / `SATUNNAISET` for a quick test |
| 06 | ~15 min | |
| 07, 09 | seconds | read `results/` (09 also the election-compass CSVs) |
| 10 | ~2 min | fits 10 models per term to get the word weights |
| 11 | ~1 min | needs the prediction files from 05 and the raw text from 01; also writes the speech-length check used by 07 |
| 08 | ~1 min | English figures; run last |
| 90 | ~1 min | optional side notes; needs the raw text from 01 and results of 05 and 06 |

Notebooks 04, 05 and 06 skip the heavy computation when their output files already exist and read them instead; set `UUDELLEEN = True` at the top of the notebook to recompute. Notebooks 07, 08 and 09 need only `results/`, the election-compass files and `Data/processed/mp_terms.parquet` (35 kB, kept in git), so they run on a fresh clone without rebuilding the rest of `Data/processed/`.

All random steps are seeded, so the numbers repeat exactly. Everything in `Data/processed/` is derived and can be deleted.

## Source data

The plenary speeches were retrieved from the Parliament of Finland search service as JSON: https://www.eduskunta.fi/haku?category=puheenvuorot&alkuajankohta=2015-01-01&loppuajankohta=2026-09-15 (speeches 1 Jan 2015 – 15 Sep 2026). The notebooks use the same export downloaded later (to 23 Sep 2026) as `Data/dataset-*.ndjson`.

`src/data_cleanup.py` removes empty and unnecessary columns from the export and summarises the content of selected columns. It reads `Kansanedustajien_puheet.ndjson` from the working directory and writes `src/dropped_columns.txt` and `src/column_content_analysis.txt`.

## Data not in the repository

- **Speech export** (`Data/dataset-*.ndjson`, about 530 MB) is over GitHub's 100 MB file limit. Download the plenary speeches from the Parliament of Finland open data service as an NDJSON export and place the file in `Data/`. Notebook 01 reads any file matching `dataset-*.ndjson`.
- **`Data/processed/`** is rebuilt by the notebooks. Notebook 04 needs about 5 GB RAM, and notebook 05 takes 15–55 minutes.
- The election-compass CSV files (13–17 MB each) are in the repository.

## Changes to raw data

- `Data/avoin_data_eduskuntavaalit_2015.csv`: one Latin-1 byte in an otherwise UTF-8 file was replaced with its UTF-8 form (byte 9,223,331, `0xE4` → `0xC3 0xA4`, the *ä* in "1.kesä" in a free-text field), 23 Sep 2026.

## Data licence

Parliament of Finland open data: CC BY 4.0. Yle election compass data: CC BY 4.0, anonymised; analysed at party level only.

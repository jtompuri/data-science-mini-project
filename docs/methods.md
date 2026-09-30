# Party Map – methods notes

Last updated 23 Sep 2026. Purpose: record what the reference papers do, what we copy from them, where we deviate and why. The technical report's methods section can be written from this file. The code is in the numbered notebooks in `notebooks/` (in Finnish).

## 1. What the reference papers do

### Simola, Nieminen & Tukiainen (2023, JHPE 2025) – *A century of partisanship in Finnish political speech*

- **Question:** how different is left-party speech from right-party speech in the Eduskunta, 1907–2018? They also compare government vs. opposition and four long-lived parties in pairs.
- **Data:** OCR'd plenary records; speeches split by speaker tags and linked to the MP register.
- **Sample rules** (Online Appendix B):
  - Only discussion sections. Procedural turns, such as vote corrections and announcements, are dropped.
  - Speeches by the Speaker and Deputy Speakers are dropped.
  - The Åland MP is dropped.
  - Speeches detected as Swedish (langdetect) are dropped. Mixed-language speeches stay in.
  - Speakers with no party are dropped.
  - An MP who switches party is assigned the party they had at the start of the parliamentary year.
- **Text preprocessing:**
  1. Drop parenthetical insertions (interjections).
  2. Map €, $, %, § to words; replace other non-alphanumeric characters with spaces; lowercase.
  3. Remove stop words (the NLTK/Snowball Finnish list).
  4. Stem with the Snowball Finnish stemmer (PyStemmer).
  5. Build **bigrams** of consecutive stems.
  6. Drop phrases that contain MP names, party names, chair addresses ("arvoisa puhemies") or months, plus a list of procedural phrases.
- **Vocabulary thresholds** (copied from Gentzkow et al.): a phrase must be used ≥100 times in total, ≥10 times in at least one year, and by ≥10 distinct speaker-years. The result is about 53,000 bigrams.
- **Unit:** phrase counts per speaker-year.
- **Measure:** the Gentzkow–Shapiro–Taddy partisanship π, the probability that a neutral observer guesses the speaker's side correctly after hearing one phrase (0.5 = no difference).
  - Estimated with an L1-penalised (lasso) multinomial logit, approximated by independent Poisson regressions.
  - Penalty chosen by BIC.
  - Controls: government status, gender and region. Region matters because of dialect.
- **Inference:**
  - 100 subsamples of 20 % of the data without replacement give the confidence intervals.
  - A permutation test, with party labels shuffled across MPs, gives the "random series". It shows how much apparent partisanship is pure bias.
- **Findings:**
  - Left-right partisanship peaked in the 1970s, driven by the SKDL (the pro-Soviet far left).
  - Partisanship has risen since the 1990s but is modest historically: about 0.502–0.506, far below the US.
  - Government-opposition differences appear from the 1970s and rise after the mid-1990s.
  - The paper's own caveat: rule-based stemming splits Finnish lemmas (e.g. *kotihoido tuen / tuke*).

### Simola, Nieminen & Tukiainen (2025, *Scientific Data*) – dataset descriptor

- Describes the 1907–2018 speech dataset and the MP characteristics dataset that go with the paper above.
- Pipeline: OCR, regex tagging of discussion sections and speakers, fuzzy name matching, removal of parenthetical content, langdetect, lowercasing, stop words, stemming.
- The retrieval audit found that over 90 % of speeches were captured.
- Party names changed over time, so the authors treat predecessor and successor groups as one party.
- **Relevance to us:** it confirms the preprocessing recipe. Our 2015–2026 export is born-digital, so we do not need the OCR steps.

### Gentzkow, Shapiro & Taddy (2019, *Econometrica*) – *Measuring group differences in high-dimensional choices*

- **Central point: naive measures of group differences in text are badly biased upward in finite samples.**
  - With many phrases and little speech, many phrases are said mostly by one party *by chance*, so plug-in estimates show strong "partisanship" even when there is none.
  - The bias grows as the amount of speech per speaker shrinks, so trends can be spurious.
  - This applies to any distance computed from raw frequencies, including Euclidean distance and correlations.
- **Fixes:**
  1. A **leave-out estimator**: party frequencies are computed without the speaker being evaluated. It is simple and has little bias, but takes no covariates.
  2. A **penalised estimator**: lasso on the party effects, a Poisson approximation to the multinomial logit and distributed computing. This is their preferred method.
- **Validation:**
  - A **permutation "random series"**, which should stay at 0.5.
  - Simulations.
  - **Out-of-sample validation**: learn phrase partisanship on one part of the speakers and predict on others (5 partitions).
- **Inference:** subsampling (100 subsamples of 1/10 of speakers). A plain bootstrap is invalid for the lasso.
- **Preprocessing:** stop words, Snowball Finnish stems, bigrams, removal of procedural phrases, the same frequency thresholds as above.
- **Warning relevant to us:** they criticise measuring partisanship by **classifier accuracy** (Peterson & Spirling 2018). Classifier accuracy also shows spurious, time-varying "partisanship" on data where party labels are random. **Any classifier-based measure must therefore be reported next to its permutation baseline, with the amount of training data held constant across periods.**
- **Finding:** US congressional partisanship was flat until about 1990, then rose sharply.

### Gronow & Malkamäki (2024) – *Political polarisation in turbulent times* (HS Foundation)

- **Data:** Finnish Twitter, 2015–2023, keyword sets for immigration, climate, COVID-19, security and inequality.
- **Method:**
  - Users are clustered into ideological groups (Conservative Right, Moderate Right, Liberal Left) and institutional groups (government vs. opposition) from their retweet networks (stochastic block models).
  - Groups are validated against candidates' accounts.
  - Polarisation = the **adaptive E-I index**, which compares retweets within groups with retweets between groups and adjusts for group size.
  - Also: topic alignment (mutual information of partitions) and a FinBERT sentiment model for news-link tweets.
- **Findings:** polarisation rose on most topics, especially under the Marin government. The Conservative Right is most distinct, and immigration and climate are aligned.
- **Relevance to us:** this is the social-media benchmark we want to compare parliament against. Two points carry over:
  - Their institutional split changes with the government, which is why our government-vs-opposition control task is essential.
  - Their group-size adjustment serves the same purpose as our balanced sampling and permutation baseline.

## 2. Our design and how it maps to the papers

| Step | Papers | Party Map | Why |
|---|---|---|---|
| Source | OCR'd PDF records 1907–2018 | Parliament open-data export 2015–2026 (born-digital, speaker IDs and party group per speech) | No OCR errors; speaker linkage is exact |
| Speaker/chair turns | dropped | chair lines are a separate field in the export, so they are never speeches | same effect |
| Åland MP | dropped | dropped (Löfström, Norrback) | as in paper |
| Swedish | langdetect at speech level, drop Swedish | stop-word vote per **sentence**; Swedish sentences removed; speeches >50 % Swedish dropped | stops the classifier from learning "Swedish ⇒ SPP" from mixed speeches |
| Party | party at start of year | party group **at the time of the speech** (exact in the export); MP-level grouping for CV uses the person across the whole term | exact and simpler; switchers are few (29 MPs, mostly the 2017 Finns split) |
| Small groups | – | groups with <5 MPs in a term dropped (Movement Now, Power Belongs to the People, one-person groups; 851 speeches) | cannot be modelled |
| Blue Reform | – | kept in the data; excluded from the cross-term main models (it exists only in 2015–19), analysed separately | keeps the cross-term measures comparable |
| Interjections | parenthetical text dropped | `[...]` and `(...)` dropped | same |
| Names / parties / procedure | phrases containing them dropped | tokens removed and replaced by a break marker, so no bigram spans them; names removed if capitalised (ambiguous names such as *Rinne*, *Aalto*, *Toimi* only mid-sentence) | same effect; avoids deleting common words |
| Stop words | NLTK Finnish | NLTK Finnish | same |
| Stemming | "Porter2" (Snowball; presumably its Finnish algorithm) | Snowball Finnish (PyStemmer) | same; lemmatisation (e.g. Voikko / Turku parser) is a possible robustness check |
| Phrases | bigrams | **unigrams + bigrams** for the classifier (Finnish compounds carry meaning in single words); **bigrams only** for the leave-out estimator | classifier benefits from unigrams; leave-out replicates the paper |
| Vocabulary thresholds | ≥100 total, ≥10 in one year, ≥10 speaker-years | same → 26,209 phrases (13,468 unigrams, 12,741 bigrams) | same |
| Unit | speaker-year | **speech** for the classifier; speaker-term and speaker-year for leave-out | the project classifies individual speeches |
| Measure | π via penalised Poisson / leave-out | (1) classifier pairwise separability; (2) GST leave-out π for every party pair | (2) validates (1) with the literature's method |
| Bias control | permutation "random series", subsampling | permutation series for both measures; MP subsampling (80 %) for intervals; **balanced training size** per party and term | Gentzkow et al.'s warning about classifier accuracy |
| Controls | government status, gender, region | government-vs-opposition control task; with/without ministerial speeches | gender/region not in the export (could be added from the MP register later) |

## 3. The classifier and the measures

- **Model:** TF-IDF (sublinear tf) + multinomial logistic regression, one model per term, the 8 parties present in all terms. The regularisation strength was tuned once on 2019–23 and is flat between C = 1 and 20; C = 2 is used everywhere.
- **Validation:** 5-fold StratifiedGroupKFold by MP, so no MP is ever in both training and test.
- **Balanced training data:** 300 speeches per party per fold, in every term. Speeches with fewer than 20 vocabulary phrases are left out (0.7 % of speeches).
- **Predictions:** out-of-fold probabilities for every speech of the held-out MPs.
- **Repetitions:** each is a fresh random 80 % of every party's MPs. The spread across repetitions is the uncertainty interval. There are 8 real repetitions and 4 permuted ones per term.
- **Polarisation:**
  - Pairwise separability: d_ab = 2·AUC_ab − 1 on the log-probability ratio of parties a and b (0 = cannot tell apart, 1 = perfectly separable).
  - The polarisation index is the mean over all 28 pairs.
  - The party map is MDS on the d matrix.
- **Viewpoint diversity:**
  - Each MP gets two independent profiles: the mean predicted probability vector over two disjoint sets of 20 random speeches. Only MPs with at least 40 speeches in the term are profiled.
  - A party's diversity is the square root of the split-half covariance of its MPs' profiles around the party centre. Noise in the two halves is independent, so it cancels. This is the same leave-out idea as in Gentzkow et al. The naive spread is inflated by noise.
  - **Relative diversity** is diversity divided by the mean distance between party centres. It separates "MPs of a party becoming alike" from "the classifier getting sharper".
  - Also reported: the mean probability the model gives to the MP's own party.
- **Control task:** the same pipeline with government vs. opposition as the label.
- **Cross-check:** Gentzkow et al.'s leave-out π for every party pair, on MP-term and MP-year bigram counts, with a permutation series (`pi_random` = mean of 4 label permutations per pair) and subsampling intervals.

## 4. Known limitations to state in the report

- **Three terms, three governments.** A time trend cannot be separated from government composition. This is the main limitation of the whole study.
- **Language, not positions.** Separability measures how differently parties speak. It matches election-compass positions in 2019–23 and 2023–27 but not in 2015–19 (§5).
- **Stemming** is crude for Finnish. The vocabulary thresholds partly compensate. Stems can look colloquial (*kyl* = kyllä, *tääl* = täällä) although the words are standard Finnish.
- **Region and dialect** may correlate with party through where parties draw their MPs. Simola et al. control for region; we do not yet.
- **Small parties.** CD has 5 MPs per term, and its 3 most active MPs give about 70 % of its speeches; the SPP has 8–10 MPs. Their estimates are noisy, and their distinctive words are partly single MPs' habits (notebook 10).
- **Party names** partly remained in the vocabulary: the cleaning pattern matches the official SDP spelling *sosialidemokraat-* but not the more common *sosiaalidemokraat-*, nor *vasemmisto* or *demareiden*. The run without style words also removes these, and the result does not change.
- Classifier accuracy depends on training size and the number of classes, so both are held fixed, and results are read against the permutation baseline.

- **Vocabulary thresholds use the full corpus.** The vocabulary and its frequency thresholds (notebook 04) are computed over all speeches, including those later used as test folds, following Gentzkow et al. The thresholds never see party labels, so this is not target leakage, but it is a design choice to state.
- **Regularisation C was chosen without nested cross-validation.** C = 2 was picked by a coarse grid on the 2019–23 term with the same data the results are reported on. Sensitivity to C is small (see the tuning cell in notebook 05), so the optimism is negligible, but the choice is not nested.

## 4b. Source checklist (preprocessing and method warnings)

Page numbers: Simola et al. = ACE Discussion Paper 160 (May 2023, the version in `Articles/`); the JHPE 2025 journal version has different pages. Gentzkow et al. = *Econometrica* 87(4), 1307–1340. Notebook 02 has the same table in Finnish.

| step or warning | Simola et al. | Gentzkow et al. | ours | reason for deviation |
|---|---|---|---|---|
| discussion speeches only, procedural speeches out | p. 44 | – | all speech types | the export has no procedural speeches; the chair's lines are a separate field |
| Speaker and Deputy Speakers out | p. 45 | p. 1311 | same | – |
| Åland MP out | p. 46 | – | same | – |
| Swedish out | speech level, p. 46 | – | sentence level, plus speeches > 50 % Swedish | Swedish sentences in bilingual speeches would reveal the SPP |
| no party → out | p. 46 | p. 1311 | same (plus groups under 5 MPs) | – |
| party switchers | party at start of year, p. 46 | new party for the term, p. 1311 | group at the time of the speech | the unit is the speech, and the group is known for each speech |
| parenthetical insertions out | p. 47 | p. 1311 | same | – |
| symbols to words, punctuation to spaces, lowercase | p. 47 | p. 1311 | same | – |
| numbers | kept, p. 47 | – | removed | years and bill numbers mark time and agenda, not party |
| hyphens | to spaces, p. 47 | deleted, p. 1311 | to spaces (as Simola) | – |
| stop words | list p. 49 | Snowball list, pp. 1311–1312 | identical list (229/229 words) | – |
| Snowball stemming | p. 47 ("Porter2") | p. 1312 (English Porter2) | Snowball Finnish; Porter2 is the name of Snowball's English algorithm | – |
| names, party names, *arvoisa puhemies*, months, procedural phrases | p. 48 | p. 1312 | removed as words with a break marker | same effect; known gap: *sosiaalidemokraat-*, *vasemmisto* (robustness run) |
| bigrams | p. 10 | p. 1311 | unigrams + bigrams (classifier), bigrams (leave-out) | Finnish compounds carry meaning; Simola et al. mention unigrams as an option (p. 10) |
| thresholds 100 / 10 per year / 10 speaker-years | p. 10 | p. 1312 | same | – |
| thresholds tightened by 10 % | – | p. 1312 | **not done** | open |
| stemming splits Finnish lemmas | p. 11 fn 10 | – | **lemmatisation not done** | open |
| finite-sample bias, spurious classifier accuracy | – | pp. 1308, 1310, 1314–1315 | grouped CV, balanced training, leave-out estimator | – |
| permutation test ("random series") | p. 19 | p. 1318 | same (classifier and leave-out) | – |
| subsampling intervals | – | p. 1321 | same (80 % of MPs) | – |
| individual MPs' mannerisms drive partisanship | p. 19 | – | grouped CV; single-MP phrases flagged (notebook 10) | – |
| confounders: government status, region, gender | pp. 13–14, 19–21 | p. 1316 | government: control task; region and gender **not done** | open; region affects filler words such as *sit tämmöis*, *elik tääl* (Simola p. 20), partly covered by the style-word run |
| transcripts keep regional speech | p. 9 | – | limitation stated | – |
| fixed vocabulary favours older phrases | p. 11 | – | limitation stated (2023–27 incomplete) | – |
| within- vs. between-topic partisanship | – | p. 1326 | notebook 11 (topics as speeches, not phrases) | – |

## 5. Key results (23 Sep 2026)

All numbers are in `results/summary_tables.md` (notebook 08), which is the single source for the report. Finnish walk-through: notebook 07.

**Finding 1: parties became more distinguishable, with a step in 2023–27.**
- Mean pairwise separability 0.39 → 0.45 → 0.56 (subsampling intervals 0.37–0.41 and 0.53–0.60 for the first and last term). Balanced accuracy 0.25 → 0.28 → 0.33 (chance 0.125).
- The permutation baseline stays at about 0. The leave-out π rises the same way (0.520 → 0.525 → 0.532) and ranks the pairs almost identically (Spearman 0.89–0.95).
- By year, π is flat in 2015–2022 (0.514–0.522) and rises in 2023–2025 (0.525–0.531). This is a step during the Orpo government, not a steady decade-long trend.
- Speech length: speeches got longer from 2015–19 to 2019–23 (median 88 → 111 cleaned words) but not after (105). Within length bins, separability rises only slightly from 2015–19 to 2019–23 (−0.02 to +0.06) but clearly to 2023–27 (+0.09 to +0.18). The first rise is partly longer speeches; the second is not. The leave-out π is per phrase and so not affected (Gentzkow et al. 2019, pp. 1313–1314).
- Robust to dropping ministers (0.39 / 0.46 / 0.55) and style words (0.39 / 0.45 / 0.55; about 130 a-priori words, 12 % of phrase occurrences, list in `src/stopwords_fi_style.txt`).

**Finding 2: not only issue ownership.** Separability within the same topic (keywords from Gronow & Malkamäki 2024; six largest parties):

| topic | 2015–19 | 2019–23 | 2023–27 |
|---|---|---|---|
| all speeches (6 parties) | 0.37 | 0.47 | 0.58 |
| immigration | 0.42 | 0.46 | 0.55 |
| climate | 0.34 | 0.51 | 0.56 |
| security | 0.30 | 0.31 | 0.45 |

Parties increasingly speak differently *about the same topic*. Part of this can still be role (government defends, opposition attacks). The directions agree with the Twitter study: for example, Finns vs. the left-greens on climate doubles in 2019–23 (0.42 → 0.82), when climate began to polarise on Twitter.

**Finding 3: two blocs.**
- NCP, Finns and CD speak more alike than their compass positions predict in all three terms (rank difference −9, −7, −10), including 2019–23 in opposition. Left, SDP and Greens are close in positions (rank ~5 of 28) but speak differently.
- Government status alone does not explain cohesion: in 2019–23 the opposition (NCP, Finns, CD) was more cohesive (0.27) than the five-party government (0.41); in 2023–27 the government is cohesive (0.33) and the opposition fragmented (0.53).
- In 2023–27 the ideological divide and the government line coincide for the first time, and cross-line pairs separate most (0.45 → 0.51 → 0.66). This explains the step in Finding 1.
- Party map 2023–27: NCP, Finns and CD form a tight cluster (0.13–0.25). The Left and Greens are at the opposite side, and SDP and Centre are apart from both. The SPP is separate in every term, probably because of its topics.

**Secondary results.**
- *Within-party diversity:* absolute spread is flat or slightly up (0.041 → 0.053); relative spread falls (0.77 → 0.51) because the denominator, the distance between parties, grows. It is Finding 1 at MP level, not an independent result. The defensible statement is that MPs did not become more alike; the parties pulled apart. The compass could not validate the measure (rho −0.62, −0.40, −0.14).
- *Speech vs. positions:* rho 0.08 / 0.47 / 0.48 (8 parties) and 0.21 / 0.60 / 0.71 without the SPP (Mantel p 0.20 / 0.004 / 0.003). The link is not stronger in 2023 than in 2019 (leave-out: 0.59 → 0.42), and compass questions change, so levels are not compared.
- *Distinctive words* (notebook 10) illustrate the findings: topics (immigration for the Finns, climate for the Greens, regions for the Centre) and roles (opposition parties talk about the government).
- *Appendix only:* Blue Reform is closest to NCP (0.20) and the Finns (0.21); elected candidates are closer to the party line than non-elected ones (−0.09, −0.11, p < 0.0005).

## 6. Method notes for the supporting analyses

- **Election compass (notebook 09).** Yle 2015 (named, 26 Likert statements), 2019 (anonymised, elected flag, 29), 2023 (anonymised, 47). Candidates answering ≥ 80 % of statements, Åland excluded, about 1,500 per year. Party distance = root-mean-square difference of party means, noise-corrected per statement (subtract s²/n for both parties). Spearman correlation over the 28 pairs with an exact Mantel test (all 8! orderings). Elected candidates in 2015 by name matching to MPs (210/210), used only as a flag. The 2015 file had one Latin-1 byte, fixed in the raw file (byte 9,223,331, 0xE4 → 0xC3 0xA4).
- **Distinctive words (notebook 10).** Per term, 10 models on 700 speeches per party from a random 80 % of MPs; weight = mean coefficient. Only phrases whose top user gives at most half of the party's use are shown.
- **Topics (notebook 11).** Gronow & Malkamäki (2024, Table A1) keywords, substring matching, at least two hits per speech. *matu*, *rikka* and *krim* restricted to word starts (mostly false hits in parliament). Separability from the main model's out-of-fold predictions within the topic's speeches; six largest parties (15 pairs); a pair needs ≥ 30 topic speeches per party.
- **Side notes (notebook 90).** Informal statistics for the blog, not used in the report's conclusions: frequency of the stem *polaris\** vs. separability and leave-out π; transcript reactions (interjections, laughter, noise, the Speaker's gavel) and who interjects at whom, with the interjector's party inferred from names or group names in the transcript (names are not reported); night sessions; year-on-year rising stems; idioms; party mentions; punctuation; per-party recall from the confusion matrix. All reported at party level. Transcription practice may change over time, and the idiom and party-mention searches are rough regular expressions.
- **Result files (notebook 05).** MP profile files carry `person_id` only; MP names were dropped from all `*_mp_profiles.csv` (data minimisation — the public repo should not pair names with model estimates). Two-class runs (`government`) save only `_summary`, since the single pair equals the summary polarisation.
- **Style words (notebook 05, run 5).** Three a-priori classes: colloquial forms, discourse particles and intensifiers, speech-act verbs. Stems shared with content words were left out after checking inflected forms (e.g. *kanssa* → *kans* = *kansa*).

## 7. Open items

- **Done (30 Sep 2026): SDP name-leak fix and rerun.** The party-name regex in notebook 02 now also removes *sosiaalidemokraat-* (transcript spelling from ~2017) and *demareiden/demareita*; the full pipeline 02→04→05→06→10→11→08 was rerun. Measured effect: negligible. Vocabulary 26,209 → 26,203 phrases (exactly the six leaked stems). Classifier polarisation 0.389/0.451/0.559 → 0.391/0.451/0.558 (|Δ| ≤ 0.002, well inside the rep spread of ±0.02–0.04); leave-out π changed by ≤ 3×10⁻⁵; topic-level separability by ≤ 0.008; government vs opposition 2015–19 by −0.013. SDP's distinctive-word lists no longer contain party-name stems. The no-style-words run was byte-identical, as expected: it already excluded these stems, which also confirms the pipeline is deterministic. *vasemmisto\** removal remains a team decision.

- Region (and gender) controls from the MP register, as in Simola et al.
- Lemmatisation instead of stemming; learning curve over training size.
- Read a sample of speeches for the two surprising 2023–27 shifts: Left vs. SDP on immigration (0.13 → 0.63) and Centre vs. NCP on climate (0.25 → 0.65).

Party codes: VAS = Left Alliance, SDP = Social Democratic Party, VIHR = Green League, KESK = Centre Party, RKP = Swedish People's Party, KD = Christian Democrats, KOK = National Coalition Party, SIN = Blue Reform, PS = Finns Party

## Party classifier, 8 parties, 300 training speeches per party

`labels = random`: party labels shuffled across MPs (bias check).

| term      | labels   |   balanced accuracy |   macro-F1 |   separability |   separability p10 |   separability p90 |
|:----------|:---------|--------------------:|-----------:|---------------:|-------------------:|-------------------:|
| 2015-2019 | random   |               0.129 |      0.121 |         -0.003 |             -0.079 |              0.099 |
| 2015-2019 | real     |               0.249 |      0.226 |          0.391 |              0.369 |              0.408 |
| 2019-2023 | random   |               0.126 |      0.122 |          0.001 |             -0.049 |              0.065 |
| 2019-2023 | real     |               0.278 |      0.254 |          0.451 |              0.402 |              0.485 |
| 2023-2027 | random   |               0.121 |      0.114 |         -0.004 |             -0.014 |              0.01  |
| 2023-2027 | real     |               0.33  |      0.281 |          0.558 |              0.527 |              0.595 |

## Separability: robustness and control task

| term      |   parties |   parties, no ministers |   parties, no style words |   government vs opposition |   government vs opposition, random |
|:----------|----------:|------------------------:|--------------------------:|---------------------------:|-----------------------------------:|
| 2015-2019 |     0.391 |                   0.387 |                     0.386 |                      0.347 |                             -0.013 |
| 2019-2023 |     0.451 |                   0.463 |                     0.451 |                      0.467 |                              0.005 |
| 2023-2027 |     0.558 |                   0.547 |                     0.547 |                      0.519 |                             -0.027 |

## Separability of party pairs on the same side vs across the government–opposition line

Main cabinet of each term; the Finns Party counted as government in 2015–19.

| term      |   across government/opposition |   same side |
|:----------|-------------------------------:|------------:|
| 2015-2019 |                          0.448 |       0.326 |
| 2019-2023 |                          0.513 |       0.379 |
| 2023-2027 |                          0.654 |       0.43  |

## Within-party diversity

`diversity` = split-half (noise-corrected) spread of MP profiles around the party centre; `diversity_relative` = the same divided by the mean distance between party centres; `own_prob` = mean probability the model gives an MP's own party (chance = 0.125).

| term      |   diversity_naive |   diversity |   diversity_relative |
|:----------|------------------:|------------:|---------------------:|
| 2015-2019 |            0.0431 |      0.0406 |               0.7644 |
| 2019-2023 |            0.0503 |      0.0488 |               0.6702 |
| 2023-2027 |            0.0545 |      0.053  |               0.5142 |

| party   |   ('diversity', '2015-2019') |   ('diversity', '2019-2023') |   ('diversity', '2023-2027') |   ('diversity_relative', '2015-2019') |   ('diversity_relative', '2019-2023') |   ('diversity_relative', '2023-2027') |   ('own_prob', '2015-2019') |   ('own_prob', '2019-2023') |   ('own_prob', '2023-2027') |   ('n_mps_profiled', '2015-2019') |   ('n_mps_profiled', '2019-2023') |   ('n_mps_profiled', '2023-2027') |
|:--------|-----------------------------:|-----------------------------:|-----------------------------:|--------------------------------------:|--------------------------------------:|--------------------------------------:|----------------------------:|----------------------------:|----------------------------:|----------------------------------:|----------------------------------:|----------------------------------:|
| VAS     |                        0.041 |                        0.053 |                        0.056 |                                 0.768 |                                 0.73  |                                 0.545 |                       0.134 |                       0.146 |                       0.208 |                            10     |                            12.75  |                            11     |
| SDP     |                        0.042 |                        0.052 |                        0.061 |                                 0.785 |                                 0.721 |                                 0.593 |                       0.147 |                       0.15  |                       0.161 |                            29.25  |                            31.125 |                            34.125 |
| VIHR    |                        0.045 |                        0.059 |                        0.05  |                                 0.843 |                                 0.816 |                                 0.482 |                       0.159 |                       0.19  |                       0.19  |                            12     |                            15.25  |                            10.5   |
| KESK    |                        0.045 |                        0.05  |                        0.041 |                                 0.846 |                                 0.689 |                                 0.402 |                       0.17  |                       0.156 |                       0.186 |                            40.375 |                            24.375 |                            20.625 |
| RKP     |                        0.033 |                        0.048 |                        0.071 |                                 0.613 |                                 0.657 |                                 0.691 |                       0.167 |                       0.159 |                       0.181 |                             8     |                             5.25  |                             6     |
| KD      |                        0.036 |                        0.029 |                        0.035 |                                 0.676 |                                 0.389 |                                 0.34  |                       0.126 |                       0.131 |                       0.139 |                             4     |                             4     |                             4     |
| KOK     |                        0.043 |                        0.053 |                        0.056 |                                 0.812 |                                 0.723 |                                 0.54  |                       0.147 |                       0.156 |                       0.161 |                            29.5   |                            31.375 |                            35.625 |
| PS      |                        0.041 |                        0.046 |                        0.054 |                                 0.772 |                                 0.638 |                                 0.522 |                       0.158 |                       0.196 |                       0.18  |                            28.625 |                            28.375 |                            35.875 |

## Agreement: classifier separability vs Gentzkow leave-out π (party pairs)

| term      |   spearman rho |   pairs |
|:----------|---------------:|--------:|
| 2015-2019 |          0.957 |      28 |
| 2019-2023 |          0.891 |      28 |
| 2023-2027 |          0.939 |      28 |

## Leave-out π by term (mean over the 28 party pairs; 0.5 = no difference)

| term      |     pi |   pi_random |   gov vs opp pi |   gov vs opp pi, random |
|:----------|-------:|------------:|----------------:|------------------------:|
| 2015-2019 | 0.5196 |      0.4948 |          0.5141 |                  0.5006 |
| 2019-2023 | 0.5246 |      0.4962 |          0.5199 |                  0.499  |
| 2023-2027 | 0.5317 |      0.4942 |          0.5211 |                  0.4989 |

## Election compass vs. speech in the following term (28 party pairs; 21 without SPP)

2015 → 2015–19, 2019 → 2019–23, 2023 → 2023–27. Exact Mantel permutation test over all party orderings.

|   compass year | candidates   | speech measure            | parties     |   Spearman rho |   Mantel p (exact) |
|---------------:|:-------------|:--------------------------|:------------|---------------:|-------------------:|
|           2015 | all          | separability (classifier) | 8 parties   |           0.07 |             0.3797 |
|           2015 | all          | separability (classifier) | without SPP |           0.18 |             0.2383 |
|           2015 | all          | leave-out π               | 8 parties   |           0.16 |             0.2237 |
|           2015 | all          | leave-out π               | without SPP |           0.35 |             0.072  |
|           2015 | elected      | separability (classifier) | 8 parties   |           0.14 |             0.2287 |
|           2015 | elected      | separability (classifier) | without SPP |           0.29 |             0.0915 |
|           2015 | elected      | leave-out π               | 8 parties   |           0.22 |             0.1229 |
|           2015 | elected      | leave-out π               | without SPP |           0.42 |             0.049  |
|           2019 | all          | separability (classifier) | 8 parties   |           0.47 |             0.0148 |
|           2019 | all          | separability (classifier) | without SPP |           0.6  |             0.004  |
|           2019 | all          | leave-out π               | 8 parties   |           0.59 |             0.0038 |
|           2019 | all          | leave-out π               | without SPP |           0.75 |             0.0004 |
|           2019 | elected      | separability (classifier) | 8 parties   |           0.44 |             0.0185 |
|           2019 | elected      | separability (classifier) | without SPP |           0.55 |             0.0065 |
|           2019 | elected      | leave-out π               | 8 parties   |           0.54 |             0.0064 |
|           2019 | elected      | leave-out π               | without SPP |           0.68 |             0.0032 |
|           2023 | all          | separability (classifier) | 8 parties   |           0.48 |             0.0139 |
|           2023 | all          | separability (classifier) | without SPP |           0.71 |             0.003  |
|           2023 | all          | leave-out π               | 8 parties   |           0.42 |             0.0203 |
|           2023 | all          | leave-out π               | without SPP |           0.69 |             0.0044 |

## Within-bloc party pairs: rank of closeness (1 = closest of 28 pairs)

|                           |   rank in compass |   rank in speech |   rank difference (speech − compass) |
|:--------------------------|------------------:|-----------------:|-------------------------------------:|
| ('Left–SDP–Greens', 2015) |               5   |              5.7 |                                  0.7 |
| ('Left–SDP–Greens', 2019) |               5   |             11.7 |                                  6.7 |
| ('Left–SDP–Greens', 2023) |               5.7 |              8.7 |                                  3   |
| ('NCP–Finns–CD', 2015)    |              16.3 |              7.3 |                                 -9   |
| ('NCP–Finns–CD', 2019)    |              14.3 |              7   |                                 -7.3 |
| ('NCP–Finns–CD', 2023)    |              12   |              2   |                                -10   |

## Most distinctive phrases (Finnish stems; top 8 per party, excluding phrases where one MP accounts for over half of the party's use)

|        | 2015-2019                                                              | 2019-2023                                                                            | 2023-2027                                                                                          |
|:-------|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| Left   | kuink, työttöm, mitenk, ongelm, pitä, pako, työntekijö, tarkoit        | työntekijö, vasemmisto, kuink, koulutuks, työnantaj, ihmist, erit, toimeentulo       | leikkauks, pienitulois, työntekijö, sosiaaliturvaleikkauks, leika, politiik, pääminister, leikkaat |
| SDP    | tääl, hallituspuolue, minister, eduskun, siis, kyl, ihmis, valiokun    | kysymys, myösk, keskustelu, ihmis, kokonaisuud, vuoks, palvelu, eduskun              | palkansaaj, työeläm, sit, pääminister, tääl, aika, leikkauks, työntekij                            |
| Greens | mite, kaik, ihmis, ihmist, kute, koulutuks, ilmastonmuutoks, ympäristö | tärkeä, kute, ihmis, keino, tosia, myös, luono, tietyst                              | hallituks, luono, ajattel, hallitus, tode, ilmastotoim, päästöj, keino                             |
| Centre | erit, as, osa, jatko, pysty, eteenp, mets, pitä                        | aiva, pitä, tule, erit, koko suome, vaik, kasvu, maataloud                           | vaalikaud, itäis, kyl, pitä, kysy, maakun, siel, pohjois                                           |
| SPP    | hallitus, vaasa, eduskuntaryhm, mite, ehk, tiete, ruots, luke          | tiete, ehk, varm, mite, hyvä, as, hyvä as, nost es                                   | koulu, panost, tosi, tärkeä, panostuks, as, luoda, ehk                                             |
| CD     | sit, tode, kyl, tääl, ikä, eduskuntaryhm, potil, kirko                 | tode, kyl, ajattel, terveydenhuolo, toivo, kysy, lääkär, minister                    | nimenom, hamas, nost, oppositio, ajatel, tode, kohd, pyr                                           |
| NCP    | eli, tietyst, työtä, myösk, työn, pitä, ratkaisu, esimerk              | pääminister, hallituks, minister, hallituspuolue, kysy, lakialoit, terapiataku, asia | uudistuks, miljard, teem, eli, tietyst, työtä, töitä, vahvist                                      |
| Finns  | lakialoit, tosia, maahanmuuto, siel, kans, henkilö, täytyy, oppositio  | raha, kans, maahanmuuto, jopa, oikeast, ongelm, edes, siel                           | rikoks, maahanmuuttopolitiik, kunnioitetu, oppositio, maahanmuuto, maas, vasem, vasemmisto         |

## Separability within topics (6 largest parties, 15 pairs; notebook 11)

|                                                    |   2015-2019 |   2019-2023 |   2023-2027 |
|:---------------------------------------------------|------------:|------------:|------------:|
| ('Main model', 'all speeches')                     |        0.38 |        0.47 |        0.58 |
| ('Main model', 'immigration')                      |        0.43 |        0.46 |        0.55 |
| ('Main model', 'climate')                          |        0.34 |        0.5  |        0.56 |
| ('Main model', 'security')                         |        0.3  |        0.31 |        0.45 |
| ('Main model', 'inequality (mostly tax)')          |        0.47 |        0.58 |        0.69 |
| ('Main model', 'COVID-19')                         |      nan    |        0.54 |      nan    |
| ('Without style words', 'all speeches')            |        0.37 |        0.47 |        0.57 |
| ('Without style words', 'immigration')             |        0.42 |        0.43 |        0.53 |
| ('Without style words', 'climate')                 |        0.33 |        0.5  |        0.53 |
| ('Without style words', 'security')                |        0.31 |        0.31 |        0.44 |
| ('Without style words', 'inequality (mostly tax)') |        0.46 |        0.58 |        0.69 |
| ('Without style words', 'COVID-19')                |      nan    |        0.53 |      nan    |

## Confusion matrix 2015-2019 (rows = true party, share of its speeches)

|      |   VAS |   SDP |   VIHR |   KESK |   RKP |   KD |   KOK |   PS |
|:-----|------:|------:|-------:|-------:|------:|-----:|------:|-----:|
| VAS  |  0.15 |  0.18 |   0.16 |   0.11 |  0.1  | 0.08 |  0.1  | 0.12 |
| SDP  |  0.15 |  0.24 |   0.12 |   0.12 |  0.08 | 0.09 |  0.09 | 0.11 |
| VIHR |  0.14 |  0.12 |   0.28 |   0.1  |  0.12 | 0.08 |  0.09 | 0.09 |
| KESK |  0.07 |  0.09 |   0.07 |   0.33 |  0.06 | 0.08 |  0.17 | 0.13 |
| RKP  |  0.09 |  0.08 |   0.14 |   0.08 |  0.33 | 0.1  |  0.09 | 0.09 |
| KD   |  0.1  |  0.14 |   0.11 |   0.14 |  0.12 | 0.14 |  0.11 | 0.15 |
| KOK  |  0.09 |  0.1  |   0.09 |   0.2  |  0.08 | 0.08 |  0.22 | 0.16 |
| PS   |  0.09 |  0.1  |   0.08 |   0.14 |  0.08 | 0.09 |  0.12 | 0.3  |

## Confusion matrix 2019-2023 (rows = true party, share of its speeches)

|      |   VAS |   SDP |   VIHR |   KESK |   RKP |   KD |   KOK |   PS |
|:-----|------:|------:|-------:|-------:|------:|-----:|------:|-----:|
| VAS  |  0.2  |  0.16 |   0.16 |   0.1  |  0.08 | 0.07 |  0.1  | 0.12 |
| SDP  |  0.14 |  0.25 |   0.12 |   0.14 |  0.07 | 0.09 |  0.11 | 0.08 |
| VIHR |  0.12 |  0.1  |   0.43 |   0.1  |  0.09 | 0.04 |  0.07 | 0.05 |
| KESK |  0.1  |  0.16 |   0.11 |   0.24 |  0.07 | 0.06 |  0.12 | 0.14 |
| RKP  |  0.12 |  0.11 |   0.15 |   0.13 |  0.26 | 0.06 |  0.09 | 0.09 |
| KD   |  0.11 |  0.14 |   0.06 |   0.1  |  0.06 | 0.14 |  0.22 | 0.17 |
| KOK  |  0.09 |  0.1  |   0.09 |   0.12 |  0.05 | 0.11 |  0.25 | 0.18 |
| PS   |  0.07 |  0.06 |   0.05 |   0.08 |  0.06 | 0.08 |  0.15 | 0.46 |

## Confusion matrix 2023-2027 (rows = true party, share of its speeches)

|      |   VAS |   SDP |   VIHR |   KESK |   RKP |   KD |   KOK |   PS |
|:-----|------:|------:|-------:|-------:|------:|-----:|------:|-----:|
| VAS  |  0.44 |  0.13 |   0.18 |   0.07 |  0.03 | 0.04 |  0.05 | 0.06 |
| SDP  |  0.18 |  0.27 |   0.08 |   0.18 |  0.04 | 0.05 |  0.11 | 0.08 |
| VIHR |  0.2  |  0.1  |   0.38 |   0.08 |  0.05 | 0.06 |  0.07 | 0.06 |
| KESK |  0.07 |  0.15 |   0.07 |   0.41 |  0.04 | 0.06 |  0.09 | 0.1  |
| RKP  |  0.03 |  0.06 |   0.06 |   0.07 |  0.35 | 0.16 |  0.15 | 0.11 |
| KD   |  0.04 |  0.09 |   0.08 |   0.12 |  0.13 | 0.18 |  0.18 | 0.17 |
| KOK  |  0.04 |  0.11 |   0.06 |   0.11 |  0.08 | 0.11 |  0.26 | 0.22 |
| PS   |  0.05 |  0.07 |   0.05 |   0.12 |  0.07 | 0.1  |  0.19 | 0.36 |

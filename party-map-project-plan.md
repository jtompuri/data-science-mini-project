# Party Map – projektisuunnitelma

**Kurssi:** Introduction to Data Science, Helsingin yliopisto, syksy 2026 (opettaja Teemu Roos)
**Tiimi:** Janne Tompuri, Maarit Vilen, Karri Lumivirta
**Tilanne 23.9.2026:**
- Canvas on palautettu.
- Anonymisoitu vaalikoneaineisto on käytössä.
- Kaikki täysistuntopuheet 5/2015–9/2026 (133 648) on ladattu ja siivottu.
- Analyysi on tehty kaikille kolmelle kaudelle (muistiot 01–11). Päälöydökset ovat muistion `07_tulokset` alussa ja englanniksi tiedostossa `docs/methods.md` (osio 5).
- Yle ei ole vielä vastannut pyyntöön nimellisestä vaalikonedatasta.

Sisäinen työ (muistiot, palaverit, tämä suunnitelma) tehdään suomeksi. Kurssille menevät canvas, tekninen raportti, blogi ja spotlight ovat englanniksi.

## 1. Tiivistelmä

Mittaamme, kuinka eri tavoin suomalaiset puolueet puhuvat eduskunnassa ja miten tämä on muuttunut vaalikausilla 2015–2026. Opetamme yksinkertaisen tekstiluokittelijan arvaamaan edustajan puolueen hänen täysistuntopuheistaan.
- **Polarisaatio** (*polarisation*): kuinka helposti malli erottaa puolueet toisistaan.
- **Puolueen sisäinen monimuotoisuus** (*within-party diversity*): kuinka paljon saman puolueen edustajat eroavat toisistaan mallin silmissä.

Vertaamme vuoden 2023 puheista laskettua puoluekarttaa karttaan, joka lasketaan ehdokkaiden vastauksista Ylen vaalikoneeseen.

Lopputuotteet ovat blogikirjoitus interaktiivisine kuvineen politiikasta kiinnostuneille kansalaisille ja toimittajille sekä enintään viisisivuinen tekninen raportti.

## 1b. Päälöydökset (23.9.2026)

1. **Puolueet erottuvat puheissaan selvemmin** (0,39 → 0,45 → 0,56), ja muutos tapahtuu kaudella 2023–27. Ensimmäinen nousu on osin puheiden pitenemistä, ja leave-out-mittarin vuosisarja on tasainen 2015–2022.
2. **Ero ei johdu vain aiheista:** erottuvuus kasvaa myös saman teeman puheissa (maahanmuutto, ilmasto, turvallisuus).
3. **Kaksi blokkia:** KOK, PS ja KD puhuvat samankaltaisesti joka kaudella. Kaudella 2023–27 ideologinen jako ja hallitusraja osuvat yksiin.

Toissijaista: sisäinen monimuotoisuus ei ole kaventunut, vaan puolueet ovat erkaantuneet toisistaan (tutkimuskysymys 2 saa heikon vastauksen). Puhe vastaa vaalikoneen kantoja kausilla 2019–23 ja 2023–27, mutta ei kaudella 2015–19.

**Raportin kuvat (enintään 5):** polarisaatio kausittain ja vuosittain, puoluekartat, blokkitaulukko, erottuvuus teemoittain, vaalikone vs. puheet 2023. Liitteeseen: sanat, monimuotoisuus, robustisuustaulukko.

## 2. Tutkimuskysymykset

1. Kuinka erilaisilta puolueet kuulostavat eduskunnassa, ja mitkä kuulostavat samanlaisilta?
2. Erkaantuvatko puolueet ajan myötä, ja tulevatko saman puolueen edustajat samankaltaisemmiksi?
3. Mitkä sanat ja aiheet erottavat puolueet kullakin kaudella?

"Ei selvää muutosta" on hyväksyttävä vastaus kysymykseen 2. Emme yritä todistaa mitään hypoteesia.

## 3. Miksi tämä projekti (päätökset ja perustelut)

- **Aiempi tutkimus päättyy vuoteen 2018.** Simola, Nieminen ja Tukiainen (2025) mittasivat puolueiden eroja eduskuntapuheissa 1907–2018 Gentzkowin, Shapiron ja Taddyn menetelmällä. Jatkamme samaa vuosiin 2019–2026 (Marinin ja Orpon hallitukset). Gronow ja Malkamäki (2024) havaitsivat polarisaation kasvaneen suomalaisessa Twitterissä 2015–2023; kukaan ei ole tarkistanut, näkyykö sama eduskunnassa.
- **Emme tutki sävyä.** Kaksi tutkimusta (Lehtosalo & Nerbonne 2024; Ristilä ym. 2026) havaitsee eduskuntapuheen muuttuneen *myönteisemmäksi*. Me mittaamme asemaa ja erottuvuutta, emme sävyä.
- **Vain vakiintuneita menetelmiä.** Lineaarinen tekstiluokittelija sanamäärillä, ristiinvalidointi edustajittain, erottuvuuteen perustuvat etäisyydet. Menetelmässä ei ole mitään uutta; huolellisuus on harhojen torjunnassa ja arvo mallin tulkinnassa.
- **Yksi aineistolähde.** Eduskunnan avoin data on julkista (CC BY 4.0) ja heti saatavilla. Datan tai laajuuden takia hylätyt ideat:
  - X/Twitter: rajapinta suljettu tutkimukselta
  - uutismedian kehystykset: raapiminen ja maksumuurit
  - YouTube-tekstitykset: IP-estot
  - Bluesky: poliittisesti vino käyttäjäkunta
  - vihamielisyysmittari: erillinen malli, jota ei ole validoitu eduskuntapuheella
  - aihemallit ja Wordfish
  - tekoäly lehdissä: jo tehty

## 4. Laajuus

**Pakolliset**
- Täysistuntopuheet 2015–2026 siivottuina
- Puolueluokittelija kausittain sekä hallitus–oppositio-kontrollitehtävä
- Polarisaatio- ja monimuotoisuusmittarit epävarmuusväleineen
- Vaalikonevertailu: vuoden 2023 puheista lasketut puolue-etäisyydet vs. vaalikoneen puolue-etäisyydet (anonymisoitu aineisto, puoluetaso)
- Kuvat 1–3, blogikirjoitus, tekninen raportti, kolmen minuutin spotlight

**Jos aikaa jää**
- ~~Suomenkielinen BERT-luokittelija vertailuksi~~ (päätös 30.9.: jätetään pois; lineaarinen malli riittää tutkimuskysymykseen)
- "Kuka tämän sanoi?" -demo (Streamlit)
- Plan B: jos Yle lähettää nimellisen vaalikonetiedoston, edustajatason vertailu "mitä sanoi vaalikoneessa vs. mitä puhuu eduskunnassa"

**Ei tehdä**
- Sosiaalisen median aineistoja, vihamielisyysmittareita, aihemalleja, Wordfishia, kielimalliin perustuvaa sijoittelua, uutisten kokotekstien raapimista, anonymisoitujen ehdokkaiden tunnistamista

## 5. Aineistot

| lähde | sisältö | saatavuus | huomiot |
|---|---|---|---|
| Eduskunnan avoin data | kaikki täysistuntopuheet 12.5.2015–23.9.2026: puhuja, eduskuntaryhmä, aika, asia, teksti | ladattu NDJSON-exporttina (`Data/dataset-*.ndjson`) | säilytetään muuttamattomana; vanha avoindata.eduskunta.fi-palvelu suljetaan vuoden 2026 lopussa |
| ParliamentSampo (Aalto) | siivotut puheet 2015–2022 | massalataus | varalla, ei tarvittu |
| Ylen vaalikone 2023 (anonymisoitu, CC BY) | noin 2 000 ehdokkaan vastaukset puolueittain | ladattu (`Data/Eduskuntavaalit 2023 …csv`) | vain puoluetaso |
| Ylen vaalikone 2015 (nimet) ja 2019 (valintatieto) | valtakunnalliset väitteet, puolue, valintatieto | ladattu (`Data/avoin_data_eduskuntavaalit_2015.csv`, `Data/Avoin_data_eduskuntavaalit_2019_valintatiedot.csv`) | vaalikonevertailu kaikille kausille (muistio 09); 2015 nimiä käytetään vain valittujen tunnistamiseen |
| Ylen vaalikone 2023 nimillä | sama, yhdistettävissä edustajiin | pyydetty sähköpostilla 14.9. (ville.seuri@yle.fi, kopio vaalikone.tuki@yle.fi); ei vastausta 23.9. mennessä | vain plan B; ellei vastausta tule ~25.9. mennessä, jatketaan ilman |

**Aineistonhallinta:**
- `Data/` sisältää ladatut raakatiedostot muuttamattomina.
- `Data/processed/` sisältää johdetut taulut: puhetaulun (yksi rivi per puhe) ja edustajataulun (edustaja × kausi × puolue). Ne rakennetaan uudelleen muistioilla 01, 02 ja 04, eikä niitä versioida gitissä.

## 6. Menetelmä

Tarkemmin muistioissa 02, 04, 05 ja 06 sekä raporttia varten tiedostossa `docs/methods.md`.

### Siivous (Simola ym.; muistio 02)
1. Pois jäävät ruotsinkieliset virkkeet, pääosin ruotsinkieliset puheet, Ahvenanmaan edustaja sekä puolueettomat ja alle viiden hengen ryhmät. Puhemiehen repliikit eivät ole aineistossa puheina.
2. Pikakirjoittajan merkinnät, edustajien nimet, puolueiden nimet ja muodollisuudet (*arvoisa puhemies*, *edustaja*, kuukaudet) poistetaan tekstistä. Tulos tarkistetaan otoksella.
3. Täytesanat poistetaan ja sanat vartaloidaan Snowball-stemmerillä, kuten Simolalla ym. Lemmatisointia ei tehdä (päätös 30.9.); rajoitus kirjataan raporttiin.
4. Puolue on eduskuntaryhmä puheen hetkellä. Vuoden 2017 PS:n hajoamisessa syntynyt ryhmä (Uusi vaihtoehto, myöhemmin Siniset) on oma puolueensa. Ryhmää vaihtaneet edustajat merkitään edustajatauluun.

### Harhojen torjunta
- Opetus- ja testiaineisto jaetaan **edustajittain**, ei puheittain; muuten malli oppii yksittäisten ihmisten puhetavan.
- **Sama määrä opetuspuheita** jokaiselle puolueelle joka kaudella (300 per osio). Pelkkä datan määrä saa puolueet näyttämään erottuvammilta (Gentzkow ym. 2019).
- **Satunnaistesti:** sama analyysi sekoitetuilla puoluenimikkeillä. Sen pitää antaa arvaustaso.

### Mallinnus (muistio 05)
- Yksi lineaarinen luokittelija (logistinen regressio TF-IDF-painotetuilla sanoilla ja sanapareilla) per kausi: 2015–19, 2019–23, 2023–27 (aineisto 23.9.2026 asti).
- Viisinkertainen ristiinvalidointi edustajittain. Epävarmuus 8 toistosta, joissa kussakin arvotaan 80 % kunkin puolueen edustajista.
- Tulokset kausittain: tarkkuus ja macro-F1, sekaannusmatriisi, puolueparien erottuvuus, edustajakohtaiset todennäköisyysprofiilit ja painavimmat sanat puolueittain.
- Kontrollitehtävä: sama asetelma, arvattavana hallitus vs. oppositio. Lisäksi ajot ilman ministerien puheita, ilman tyylisanoja (`src/stopwords_fi_style.txt`) ja Siniset mukana (2015–19).
- Erottuvuus teemoittain (muistio 11): sama malli, mutta vain saman teeman puheet (Gronowin ja Malkamäen hakusanat: maahanmuutto, ilmasto, turvallisuus, korona, eriarvoisuus). Erottaa aiheiden omistajuuden kehystyksestä ja mahdollistaa vertailun Twitter-tulokseen.
- Vertailu Gentzkowin ym. leave-out-mittariin (muistio 06).

### Mittarit
- **Polarisaatio** = puolueparien erottuvuuden (2·AUC − 1) keskiarvo. Erottuvuusmatriisista tehdään kausittainen puoluekartta (MDS).
- **Puolueen sisäinen monimuotoisuus** = puolueen edustajien todennäköisyysprofiilien kohinakorjattu hajonta, myös suhteessa puolueiden väliseen etäisyyteen.
- **Vaalikonevertailu** = vaalikoneesta puolueiden keskimääräiset vastaukset, puolueiden väliset etäisyydet ja puolueen sisäinen hajonta. Puolueparien etäisyysjärjestystä verrataan kauden 2023–27 puhemalliin, ja kartat esitetään rinnakkain.

## 7. Lopputuotteet ja kuvat

1. **Puoluekartta kausittain:** puolueet lähekkäin, jos ne sekoittuvat helposti; edustajat pisteinä; vuoden 2023 kartta vaalikonekartan vieressä.
2. **Muutos 2015–2026:** puolueiden välinen etäisyys ja puolueen sisäinen hajonta, yksi viiva per puolue.
3. **Mikä erottaa puolueet:** painavimmat sanat puolueittain ja kausittain.
4. **Blogikirjoitus:** selkokielinen, kolme päähavaintoa, interaktiiviset Plotly-kuvat.
5. **Tekninen raportti** (enintään 5 sivua): aineisto, esikäsittely, mallit, validointi, tulokset, rajoitukset, mikä muuttui canvasista ja miksi, jatkotutkimus (vihamielisyysmittari, useammat kaudet, plan B jos ei toteutunut).
6. **Spotlight** (3 min, ei-tekninen): "A parliament can change in two ways: parties move apart, or they stop disagreeing inside. We measured both, for every party, 2015–2026."

## 8. Roolit

- **A – aineisto ja putki:** lataus, siivous, edustajataulu, tasapainotettu otanta, toistettavuus, "liitä puhe" -toiminto
- **B – mallit ja mittarit:** luokittelijat, kontrollitehtävä, polarisaatio ja monimuotoisuus, vaalikonevertailu, BERT jos aikaa
- **C – EDA, visualisointi ja viestintä:** EDA-muistio, kuvat, blogi, spotlight-käsikirjoitus, etiikkaosio; ottaa plan B:n, jos se toteutuu

Viikoittainen palaveri perjantaisin; rajaus- ja karsintapäätökset tehdään siellä.

## 9. Aikataulu

| viikko | päivät | tavoite |
|---|---|---|
| 1 (tehty) | 15.–21.9. | Canvas palautettu; latauksia aloitettu; Yleen otettu yhteyttä |
| 2 | 22.–28.9. | Puheet ladattu ja siivottu ✓; ensimmäinen luokittelija ✓ (kaikki kaudet); EDA ✓; vaalikoneen puolueprofiilit. **Pe 26.9.: plan B mukaan vai ei** |
| 3–4 | 29.9.–11.10. | Vaalikonevertailu; lopulliset kuvat; blogin runko; spotlight-käsikirjoitus. **30.9.: päätetty jättää pois BERT, vakioinnit ja herkkyystarkastelut. 9.10.: tulokset lukitaan** |
| 5 | 12.–16.10. | Spotlight-esitykset; harjoitellaan vähintään 3 kertaa; kuvista staattiset varaversiot; palaute muille ryhmille |
| 6 | 17.–26.10. | Blogi julkaistu; tekninen raportti; joku muu kuin tekijä ajaa muistiot puhtaalta pöydältä. **Ma 26.10. klo 23.59: palautus** |

## 10. Riskit

- Puolueet voivat erota lähinnä siinä, *mistä* ne puhuvat, eivätkä siinä, *miten*. → EDA näyttää aihejakauman puolueittain; rajoitus kerrotaan tulosten yhteydessä. (EDA vahvisti, että erot ovat pitkälti aiheissa.)
- Muutokset ajassa voivat olla pieniä. → Raportoidaan sellaisinaan.
- Hallitusasema muokkaa puhetta. → Kontrollitehtävä mittaa sen. (Ensimmäiset tulokset: puolueiden erottuvuuden kasvu näkyy pääosin hallitus–oppositio-rajan yli.)
- Pienillä puolueilla on vähän aineistoa (KD: 5 edustajaa, RKP: 8–10). → Leveämmät epävarmuusvälit, näytetään rehellisesti.
- Murre ja alue voivat selittää osan eroista. → Ei vakioida (päätös 30.9.); mainitaan raportin rajoituksissa, että Simola ym. vakioivat alueen ja sukupuolen.
- Plan B riippuu Ylestä; mikään muu ei riipu.

## 11. Etiikka

- Kaikki aineisto on julkista, eikä suostumusta tarvita. Henkilötietoja on vain kansanedustajien julkisista rooleista.
- Mallin tulokset ovat arvioita julkisuuden henkilöistä. Blogi raportoi puoluetasolla; edustajatason tulokset ovat vain teknisessä raportissa; edustajia ei aseteta paremmuusjärjestykseen.
- Vaalikoneaineisto on tarkoituksella anonymisoitu: käytetään vain puoluetasoa, eikä ehdokkaita yritetä tunnistaa puolueen, vaalipiirin, iän ja sukupuolen perusteella.
- Ruotsinkieliset puheet jätetään pois, ja se kerrotaan. Ministerien virkakieli mainitaan mahdollisena harhana, ja se testataan ajolla ilman ministerejä.

## 12. Avoimet asiat

- [x] Päätös 30.9.: vakiointia alueella ja sukupuolella ei tehdä; ero Simolaan ym. kirjataan raportin rajoituksiin
- [x] Päätös 30.9.: lemmatisointi-, oppimiskäyrä- ja esiintymisrajatarkasteluja ei tehdä; tehdyt tarkistukset (satunnaistesti, leave-out, ministerit, tyylisanat, pituusluokat, teemat) riittävät kurssityöhön
- [x] Tyylisanatarkistus (muistio 05 ajo `party_nostyle`, 23.9.): polarisaatio 0,39 → 0,45 → 0,55, lähes sama kuin päätuloksessa
- [x] Erottuvuus teemoittain ja vertailu Gronowin ja Malkamäen Twitter-tulokseen (muistio 11, 23.9.): kasvu näkyy kaikissa teemoissa
- [x] SDP:n nimivuoto korjattu ja putki ajettu uudelleen 30.9.: vaikutus mitätön (polarisaatio muuttui enintään 0,002; erot kirjattu methods.md §7). Tiimin päätettävä vielä *vasemmisto*-sanan poisto
- [x] Vaalikoneen puolueprofiilit ja vaalikonevertailu 2015, 2019 ja 2023 (muistio 09, 23.9.)
- [ ] Päätös: edustajatason vertailu 2015–19 (vaalikone 2015 vs. puheprofiili; korvaa plan B:n) – perjantain palaveri
- [x] Painavimmat sanat puolueittain (kuva 3): muistio 10, `sanat_puolueittain.png` ja `res_top_words.png`. Havainto: RKP:n ja KD:n kärkisanoista moni on yhden edustajan maneeri; oman puolueen nimi jäi sanastoon (SDP, VIHR, VAS)
- [ ] Workshopin numero canvasiin
- [ ] Ylen vastaus (plan B:n takaraja ~25.9.); muistutus lähetetty 23.9.
- [x] Puheaineiston lähde: Eduskunnan avoimen datan NDJSON-exportti (`Data/dataset-*.ndjson`), 23.9.
- [x] ~~api.eduskunta.fi-rajapinnan taulujen nimet~~ – ei tarvita, käytetään exporttia
- [ ] Oikeusministeriön lähdeviitteen tiedot (Eduskuntavaalitutkimus 2023, URN)
- [ ] Kurssin menetelmälista vertailua varten (kurssisivu on JavaScript-pohjainen, sitä ei voitu lukea)

## 13. Kansiorakenne

```text
data-science-mini-project/
  README.md                   # asennus ja muistioiden ajojärjestys (englanniksi)
  party-map-project-plan.md   # tämä tiedosto
  Data/                       # ladatut raakatiedostot, muuttamattomina
    processed/                # johdetut taulut (muistiot 01, 02, 04, 05; ei gitissä)
  notebooks/                  # analyysi suomeksi, ajetaan järjestyksessä
    01_aineiston_lataus.ipynb
    02_siivous.ipynb
    03_eda.ipynb
    04_sanasto.ipynb
    05_luokittelija.ipynb
    06_leaveout.ipynb
    07_tulokset.ipynb
    08_raporttikuvat.ipynb    # englanninkieliset raporttikuvat
    09_vaalikone.ipynb        # vaalikonevertailu
    10_sanat.ipynb            # painavimmat sanat puolueittain (kuva 3)
    11_teemat.ipynb           # erottuvuus teemoittain, vertailu Twitteriin
  src/config.py               # yhteiset määritelmät: puolueet, kaudet, hallitukset
  src/stopwords_*.txt         # täytesanalistat (NLTK) ja tyylisanalista
  results/                    # mallien tulokset (csv/json) ja summary_tables.md
  reports/figures/            # kuvat
  docs/methods.md             # artikkelien tiivistelmät ja menetelmäperustelut raporttia varten
  Canvas/                     # canvas
  Articles/                   # lähdeartikkelit (ei gitissä: tekijänoikeus)
  archive/                    # vanhojen versioiden tulokset (ei gitissä)
  scripts/setup_venv.sh       # virtuaaliympäristö
  (tulossa) blog/, report/    # blogiluonnos ja tekninen raportti
```

## 14. Keskeiset lähteet

- Simola, Nieminen & Tukiainen (2025). A century of partisanship in Finnish political speech. *JHPE* 5(2). Working paper: https://ace-economics.fi/kuvat/dp160.pdf
- Simola, Nieminen & Tukiainen (2025). Finnish parliamentary speeches dataset. *Scientific Data* 12, 1063. https://www.nature.com/articles/s41597-025-05056-y
- Gentzkow, Shapiro & Taddy (2019). Measuring group differences in high-dimensional choices. *Econometrica* 87(4). https://scholar.harvard.edu/files/shapiro/files/politext.pdf
- Gronow & Malkamäki (2024). Political polarisation in turbulent times. HS-säätiön raportti. https://arxiv.org/pdf/2403.03842
- Lehtosalo & Nerbonne (2024). Detecting emotional polarity in Finnish parliamentary proceedings. https://aclanthology.org/2024.cpss-1.7.pdf
- Ristilä, Tarkka, Laippala & Elo (2026). Hopes and fears. https://arxiv.org/pdf/2601.20424
- Artikkelien tiivistelmät ja menetelmävertailu: `docs/methods.md`

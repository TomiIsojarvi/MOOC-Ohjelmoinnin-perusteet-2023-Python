# Osa 7 - Tehtävien vastaukset
## Hypotenuusa
Tee funktio hypotenuusa(kateetti1: float, kateetti2: float), joka saa parametrikseen suorakulmaisen kolmion kateettien pituudet. Funktio palauttaa kolmion hypotenuusan pituuden.

Ratkaisu lasketaan Pythagoraan lauseen avulla. Saat laskettua neliöjuuren math-moduulin funktion avulla.

Esimerkkejä:
```python
print(hypotenuusa(3,4)) # 5.0
print(hypotenuusa(5,12)) # 13.0
print(hypotenuusa(1,1)) # 1.4142135623730951
```

[Vastaus](osa07-01_hypotenuusa/src)

## Erikoismerkit
Moduulissa string on merkkijonovakioita, jotka määrittelevät tiettyjä merkkiryhmiä (esim. pienet kirjaimet ja välimerkit). Tutustu näihin vakioihin ja kirjoita niitä käyttäen funktio jaa_merkkeihin(merkkijono: str), joka saa parametrikseen merkkijonon. Funktio palauttaa tuplen, jossa parametrina saadun merkkijonon merkit on jaettu kolmeen eri merkkijonoon:

- Ensimmäisessä jonossa on kaikki pienet ja suuret englanninkieliset kirjaimet (vakio ascii_letters)
- Toisessa jonossa on kaikki vakiossa punctuation määritellyt välimerkit
- Kolmannessa jonossa on kaikki merkit (mukaan lukien esim. välilyönnit), jotka eivät kuulu kahteen edelliseen ryhmään

Merkit tulee tallentaa palautettuihin merkkijonoihin siinä järjestyksessä kuin ne esiintyvät alkuperäisessä merkkijonossa.

Esimerkki:
```python
osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
print(osat[0])
print(osat[1])
print(osat[2])
```
```
TmontestiToimiikomit
!!!,?
ää    ä
```

[Vastaus](osa07-02_erikoismerkit/src)

## Murtoluvuilla laskeminen
Tutustu Pythonin moduuliin fractions ja toteuta sen avulla funktio jaa_palasiksi(maara: int), joka saa parametrikseen palasten määrän. Funktio jakaa luvun 1 parametrin mukaisesti yhtä suuriin murtolukupalasiin ja palauttaa nämä palaset listassa.

Esimerkki:
```python
for p in jaa_palasiksi(3):
    print(p)

print()

print(jaa_palasiksi(5))
```
```
1/3
1/3
1/3

[Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]
```

[Vastaus](osa07-03_murtoluvuilla_laskeminen/src)

## Lottonumerot
Tee funktio lottonumerot(maara: int, alaraja: int, ylaraja: int), joka arpoo annetun määrän satunnaislukuja väliltä alaraja...ylaraja, tallentaa ne listaan ja palauttaa listan. Lukujen tulee olla palautetussa listassa suuruusjärjestyksessä.

Koska kyseessä ovat lottonumerot, sama numero ei saa esiintyä listassa kahta kertaa.

Esimerkki:
```python
for numero in lottonumerot(7, 1, 40):
    print(numero)
```
```
4
7
11
16
22
29
38
```

[Vastaus](osa07-04_lottonumerot/src)

## Salasanan arpoja, osa 1
Tee funktio, jonka avulla on mahdollista luoda halutun pituisia satunnaisista pienistä kirjaimista (väliltä a-z) muodostettuja salasanoja.

Esimerkki:
```python
for i in range(10):
    print(luo_salasana(8))
```
```
lttehepy
olsxttjl
cbjncrzo
dwxqjdgu
gpfdcecs
jabyvgar
xnbbonbl
ktmsjyww
ejhprmel
rjkoacib
```

[Vastaus](osa07-05_salasanan_arpoja_1/src)

## Salasanan arpoja, osa 2
Tee paranneltu versio edellisen tehtävän funktiosta. Funktio saa nyt kolme parametria:

- jos toinen parametri on True, salasanassa on myös (yksi tai useampi) numero
- jos kolmas parametri on True, salasanassa on myös (yksi tai useampi) erikoismerkki joukosta !?=+-()#

Salasanassa täytyy olla parametreista riippumatta aina vähintään yksi kirjain. Voit olettaa, että funktiota kutsutaan aina parametreilla, joilla on mahdollista tuottaa halutunlaisia salasanoja.

Esimerkki:
```python
for i in range(10):
    print(luo_hyva_salasana(8, True, True))
```
```
2?0n+u31
u=m4nl94
n#=i6r#(
da9?zvm?
7h)!)g?!
a=59x2n5
(jr6n3b5
9n(4i+2!
32+qba#=
n?b0a7ey
```

[Vastaus](osa07-06_salasanan_arpoja_2/src)

## Noppasimulaatio
Tehdään tässä tehtävässä muutamia funktioita, joita on mahdollista käyttää nopanheittoon liittyvissä peleissä.

Normaalin nopan sijaan tehtävässä käytetään ns. epätransitiivisia noppia, joista on lisää tietoa esim. tässä artikkelissa tai tässä videossa.

Käytössä on kolme noppaa:

- Nopassa A on numerot 3, 3, 3, 3, 3, 6
- Nopassa B on numerot 2, 2, 2, 5, 5, 5
- Nopassa C on numerot 1, 4, 4, 4, 4, 4

Tee funktio heita(noppa: str), joka heittää parametrinsa kertomaa noppaa. Esimerkki:
```python
for i in range(20):
    print(heita("A"), " ", end="")
print()
for i in range(20):
    print(heita("B"), " ", end="")
print()
for i in range(20):
    print(heita("C"), " ", end="")
```
```
3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  6  3  6  3
2  2  5  2  2  5  5  2  2  5  2  5  5  5  2  5  2  2  2  2
4  4  4  4  4  1  1  4  4  4  1  4  4  4  4  4  4  4  4  4
```

Tee vielä funktio pelaa(noppa1: str, noppa2: str, kertaa: int) joka heittää kokonaisluvun kertoman määrän parametreina olevia noppia. Funktio palauttaa tuplen, joka kertoo nopan 1 voittojen lukumäärän, nopan 2 voittojen lukumäärän ja tasapelien lukumäärän.
```python
tulos = pelaa("A", "C", 1000)
print(tulos)
tulos = pelaa("B", "B", 1000)
print(tulos)
```
```
(292, 708, 0)
(249, 273, 478)
```

[Vastaus](osa07-07_noppasimulaatio/src)

## Satunnaiset sanat
Tehtäväpohjassa on annettu tiedosto sanat.txt, joka sisältää englannin kielen sanoja, yksi sana joka rivillä.

Kirjoita funktio sanat(n: int, alku: str), joka palauttaa listassa n kappaletta satunnaisia sanoja tiedostosta. Kaikkien palautettujen sanojen tulee alkaa annetulla merkkijonolla.

Jos funktiota esim. kutsuttaisiin parametreilla sanat(3, "ca"), se voisi palauttaa listassa esim. sanat "cat", "car" ja "carbon". Sama sana ei saa esiintyä listassa kahdesti.

Jos annetulla merkkijonolla alkavia sanoja ei löydy tarpeeksi annetun kokoisen ryhmän muodostamiseen, funktio tuottaa poikkeuksen ValueError.

Esimerkki:
```python
lista = sanat(3, "ca")
for sana in lista:
    print(sana)
```
```
cat
car
carbon
```

[Vastaus](osa07-08_satunnaiset_sanat/src)

## Kuinka vanha
Tee ohjelma, joka kysyy käyttäjän syntymäajan (erikseen päivä, kuukausi ja vuosi) ja tulostaa, kuinka monta päivää vanha käyttäjä oli 31.12.1999 seuraavan esimerkin mukaisesti:
```
Päivä: 10
Kuukausi: 9
Vuosi: 1979
Olit 7417 päivää vanha, kun vuosituhat vaihtui.
```
```
Päivä: 28
Kuukausi: 3
Vuosi: 2005
Et ollut syntynyt, kun vuosituhat vaihtui.
```
Voit olettaa, että kaikki annetut päivä-kuukausi-vuosi-yhdistelmät ovat mahdollisia (eli käyttäjä ei siis anna esim. syötettä 31.2.1999).

[Vastaus](osa07-09_kuinka_vanha/src)

## Henkilötunnus oikein?
Tee funktio onko_validi(hetu: str), joka palauttaa True tai False sen mukaan, onko annettu henkilötunnus oikea. Henkilötunnus on muotoa ppkkvvXyyyz, jossa ppkkvv kertoo syntymäajan (päivä/kuukausi/vuosi), X on syntymävuosisadasta riippuva välimerkki, yyy henkilökohtainen yksilönumero ja z tarkistemerkki.

Ohjelman tulee tarkastaa, että

- alkuosassa on ppkkvv-muodossa oleva päivämäärä, joka on olemassa oleva päivämäärä
- välimerkki on + (1800-luku), - (1900-luku) tai A (2000-luku) ja
- lopussa oleva tarkastusmerkki on oikein.

Tarkastusmerkki lasketaan jakamalla syntymäajasta ja yksilönumerosta muodostuva numerosarja 31:llä ja ottamalla tästä jakojäännös. Merkki valitaan sitten jakojäännöksen mukaisesta indeksistä merkkijonosta 0123456789ABCDEFHJKLMNPRSTUVWXY. Esimerkiksi jos jakojäännös on 12, valitaan indeksissä 12 oleva merkki C.

Lisätietoa laskemisesta löydät esimerkiksi Digi- ja väestötietoviraston sivuilta.

HUOM! Pidä huolta, ettet jaa omaa henkilötunnustasi esimerkiksi testikoodin mukana, jos kysyt neuvoja tehtävään kurssin keskustelualueella tai muualla.

Oikeamuotoisia henkilötunnuksia testaamiseen ovat esimerkiksi seuraavat:

- 230827-906F
- 120488+246L
- 310823A9877

[Vastaus](osa07-10_henkilotunnus_oikein/src)

## Ruutuaika
Ohjelmassa kirjoitetaan käyttäjän määrittelemään tiedostoon "ruutuaikoja", eli käyttäjän television, tietokoneen ja mobiililaitteen ääressä tiettyinä päivinä viettämää aikaa.

Ohjelma toimii seuraavasti:
```
Tiedosto: kesakuun_loppu.txt
Aloituspäivä: 24.6.2020
Montako päivää: 5
Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):
Ruutuaika 24.06.2020: 60 120 0
Ruutuaika 25.06.2020: 0 0 0
Ruutuaika 26.06.2020: 180 0 0
Ruutuaika 27.06.2020: 25 240 15
Ruutuaika 28.06.2020: 45 90 5
Tiedot tallennettu tiedostoon kesakuun_loppu.txt
```
Kunkin päivän riville on siis annettu välilyönnillä eroteltuna kolme minuuttimäärää.

Ohjelma tallentaa tilaston ruutuajoista tiedostoon kesakuun_loppu.txt, joka näyttää yllä olevalla syötteellä seuraavalta:
```
Ajanjakso: 24.06.2020-28.06.2020
Yht. minuutteja: 780
Keskim. minuutteja: 156.0
24.06.2020: 60/120/0
25.06.2020: 0/0/0
26.06.2020: 180/0/0
27.06.2020: 25/240/15
28.06.2020: 45/90/5
```

[Vastaus](osa07-11_ruutuaika/src)

## JSON-tiedoston käsittely
Tarkastellaan JSON-tiedostoa, jossa on tietoa opiskelijoista seuraavassa muodossa:
```
[
    {
        "nimi": "Pekka Pythonisti",
        "ika": 27,
        "harrastukset": [
            "koodaus",
            "kutominen"
        ]
    },
    {
        "nimi": "Jaana Javanainen",
        "ika": 24,
        "harrastukset": [
            "koodaus",
            "kalliokiipeily",
            "lukeminen"
        ]
    }
]
```
Toteuta funktio tulosta_henkilot(tiedosto: str), joka lukee esimerkin tavalla muodostetun JSON-tiedoston (jonka sisältönä voi olla mielivaltainen määrä henkilöitä) ja tulostaa ne seuraavassa muodossa:
```
Pekka Pythonisti 27 vuotta (koodaus, kutominen)
Jaana Javanainen 24 vuotta (koodaus, kalliokiipeily, lukeminen)
```

Harrastukset tulee luetella samassa järjestyksessä kuin ne on annettu JSON-tiedostossa.

[Vastaus](osa07-12_jsontiedostot/src)

## Kurssien tilastot
### Osa 1: tieto kursseista
Osoitteesta https://studies.cs.helsinki.fi/stats-mock/api/courses löytyy JSON-muodossa muutaman laitoksen verkkokurssin perustiedot.

Tee funktio hae_kaikki() joka hakee ja palauttaa kaikkien menossa olevien kurssien (kentän enabled arvona True) tiedot listana tupleja. Paluuarvon muoto on seuraava:
```
[
    ('Full Stack Open 2020', 'ofs2019', 2020, 201),
    ('DevOps with Docker 2019', 'docker2019', 2019, 36),
    ('DevOps with Docker 2020', 'docker2020', 2020, 36),
    ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
]
```
Jokainen tuple siis sisältää seuraavat arvot:

- kurssin koko nimi (fullName)
- nimi (name)
- vuosi (year)
- harjoitusten (exercises) yhteenlaskettu määrä

Huom: Tämän tehtävän testien toimivuuden osalta on oleellista, että haet tiedot funktiolla urllib.request.urlopen.

Huom2: Testeissä käytetään myös ovelaa kikkaa, joka hieman muuttaa internetistä tulevaa dataa ja tämän avulla varmistaa, että et huijaa tehtävässäsi palauttamalla "kovakoodattua" dataa.

Huom3: Jotkut Mac-käyttäjät ovat törmänneet tehtävässä seuraavaan ongelmaan:
```
File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/urllib/request.py", line 1353, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1124)>
```
Ongelman ratkaisutapa riippuu siitä miten python on asennettu koneellesi. Joissain tapauksissa toimii seuraava:
```
cd "/Applications/Python 3.8/"
sudo "./Install Certificates.command
```
Huomaa, että cd-komennon polku riippuu käyttämästäsi Pythonin versiosta. Se voi olla myös "/Applications/Python 3.8/".

Täällä on ehdotettu useita erilaisia ratkaisuja ongelmaan.

Eräs kikka jota voit kokeilla, on seuraava:
```python
import urllib.request
import json
import ssl # lisää tämä kirjasto importeihin

def hae_kaikki():
    # ja tämä rivi funktioiden alkuun
    context = ssl._create_unverified_context()
    # muu koodi
```
Toinen tapa kiertää ongelma on seuraava:
```python
import urllib.request
import certifi # lisää tämä kirjasto importeihin
import json

def hae_kaikki():
   osoite = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
   # lisätään kutsuun toinen parametri
   pyynto = urllib.request.urlopen(osoite, cafile=certifi.where())
   # muu koodi
```
### Osa 2: yhden kurssin tiedot
Kunkin kurssin JSON-muotoinen tehtävästatistiikka löytyy omasta osoitteesta, joka saadaan vaihtamalla kurssin kenttä name seuraavassa tähtien paikalle https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats

Esimerkiksi kurssin docker2019 tiedot ovat osoitteessa https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats

Tee ohjelmaasi funktio hae_kurssi(kurssi: str), joka palauttaa kurssin tarkemman tehtävästatistiikan.

Kun kutsutaan hae_kurssi("docker2019"), funktio palauttaa sanakirjan, jonka sisältö on seuraava:
```
{
    'viikkoja': 4,
    'opiskelijoita': 220,
    'tunteja': 5966,
    'tunteja_keskimaarin': 27,
    'tehtavia': 4988,
    'tehtavia_keskimaarin': 22
}
```
Sanakirjaan tallennetut arvot määrittyvät seuraavasti:

- viikkoja: kurssia vastaavan JSON-olioiden määrä
- opiskelijoita viikkojen opiskelijamäärien maksimi
- tunteja: kakkien viikkojen tuntimäärien (hour_total) summa
 - tunteja_keskimaarin: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)
- tehtavia: kakkien viikkojen tehtävämäärien (exercise_total) summa
- tehtavia_keskimaarin: edellinen jaettuna opiskelijamäärällä (kokonaislukuna pyöristettynä alaspäin)

Huom: Samat huomiot pätevät tähän osaan kuin edelliseen!

Huom2: löydät math -moduulista funktion, jonka avulla kokonaisluvun alaspäin pyöristäminen on helppoa


[Vastaus](osa07-13_kurssistatistiikka/src)

## Kuka huijasi
Tiedostossa tentin_aloitus.csv on tenttien aloitusaikoja muodossa tunnus;hh:mm. Esimerkiksi:
```
jarmo;09:00
timo;18:42
kalle;13:23
```
Lisäksi tiedostossa palautus.csv on tehtävien palautusaikoja muodossa tunnus;tehtävä;pisteet;hh:mm. Esimerkiksi:
```
jarmo;1;8;16:05
timo;2;10;21:22
jarmo;2;10;19:15
jne...
```
Tehtäväsi on etsiä ne opiskelijat, jotka ovat käyttäneet tenttiin yli 3 tuntia aikaa, eli opiskelijat, joiden jonkin tehtävän palautus on tehty yli 3 tuntia tentin aloitusajasta. Palautuksia voi siis olla useampi. Voit olettaa, että kaikki ajat ovat saman vuorokauden puolella.

Kirjoita funktio huijarit(), joka palauttaa listan huijanneiden opiskelijoiden käyttäjätunnuksista.

[Vastaus](osa07-14_kuka_huijasi/src)

## Kuka huijasi, versio 2
Käytössäsi on edellisessä tehtävässä määritellyt datatiedostot. Kirjoita funktio viralliset_pisteet(), joka palauttaa sanakirjassa (dict) opiskelijoiden koepisteet seuraavien sääntöjen mukaan:

- Jos samaan tehtävänumeroon on tehty useita palautuksia, korkeimman pistemäärän palautus otetaan huomioon
- Jos tehtäväpalautus on tehty yli 3 tuntia tentin aloittamisen jälkeen, palautusta ei huomioida ollenkaan

Tehtävät on numeroitu 1–8 ja jokaisesta tehtävästä voi saada 0–6 pistettä.

Palautetussa sanakirjassa tunnus on avain ja tehtävien yhteispistemäärä arvo.

Vinkki: sisäkkäiset sanakirjat (dict) ovat mainio työkalua tallennettaessa eri opiskelijoiden pisteitä ja aikoja.

[Vastaus](osa07-15_kuka_huijasi_2/src)

## Spellchecker, versio 2
Teemme tässä tehtävässä hieman parannellun version edellisen osan tehtävästä Spellchecker.

Edellisen osan version tapaan ohjelma pyytää käyttäjää kirjoittamaan rivin englanninkielistä tekstiä. Ohjelma suorittaa tekstille oikeinkirjoitustarkistuksen ja tulostaa saman tekstin siten, että kaikki väärin kirjoitetut sanat on ympäröity tähdillä. Tämän lisäksi ohjelma antaa listan korjausehdotuksia väärin kirjotettuihin sanoihin.

Seuraavassa kaksi käyttöesimerkkiä:
```
write text: We use ptython to make a spell checker

We use *ptython* to make a spell checker
korjausehdotukset:
ptython: python, pythons, typhon
```
```
write text: this is acually a good and usefull program

this is *acually* a good and *usefull* program
korjausehdotukset:
acually: actually, tactually, factually
usefull: usefully, useful, museful
```
Korjausehdotukset etsitään standardikirjaston moduulin difflib tarjoaman funktion get_close_matches avulla.

Huom: jotta testit toimisivat, käytä funktiota "oletusasetuksilla", eli antamalla sille kaksi parametria: virheellinen sana ja lista oikeista sanoista.

[Vastaus](osa07-16_spellchecker_versio2/src)

## Merkkiapuri
Tee moduuli merkkiapuri, joka sisältää seuraavat funktiot:

Funktio vaihda_koko(merkkijono: str) saa parametrikseen merkkijonon. Funktio luo ja palauttaa uuden merkkijonon, jossa alkuperäisen merkkijonon pienet kirjaimet on muutettu isoiksi kirjaimiksi ja päinvastoin.

Funktio puolita(merkkijono: str) palauttaa tuplessa parametrinaan saamansa merkkijonon ensimmäisen ja toisen puolikkaan. Jos merkkijonossa on pariton määrä kirjaimia, ensimmäinen puolikas on lyhyempi.

Funktio poista_erikoismerkit(merkkijono: str) palauttaa merkkijonon, josta on poistettu kaikki muut merkit paitsi aakkoset [a...ö, A...Ö], numerot ja välilyönnit.

Esimerkkejä moduulin toiminnasta:
```python
import merkkiapuri

mjono = "Moi kaikki!"

print(merkkiapuri.vaihda_koko(mjono))

p1, p2 = merkkiapuri.puolita(mjono)

print(p1)
print(p2)

m2 = merkkiapuri.poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
print(m2)
```
```
mOI KAIKKI!
Moi k
aikki!
Tämä on testi katsotaan miten käy11
```

[Vastaus](osa07-17_merkkiapuri/src)

## Oma ohjelmointikieli


[Vastaus](osa07-18_oma_ohjelmointikieli/src)


# Osa 6 - Tehtävien vastaukset
## Suurin luku
Tiedostoon luvut.txt on tallennettu lukuja, yksi luku per rivi seuraavan esimerkin mukaisesti:
```
2
45
108
3
-10
1100
...jne...
```
Kirjoita funktio suurin, joka lukee tiedoston ja palauttaa suurimman tiedostosta löytyvän luvun.

Huomaa, että tiedoston nimi on aina luvut.txt eikä funktiolle anneta parametria.

Huom! Jos VS Code ei löydä tiedostoa vaikka olet tarkastanut tiedoston nimen kirjoitusasun, voit kokeilla seuraavaa heti tehtävän jälkeen olevaa ohjetta.

[Vastaus](osa06-01_suurin_luku/src)

## Hedelmäkauppa
Tiedostossa hedelmat.csv on hedelmiä hintoineen seuraavan esimerkin mukaisesti:
```
banaani;6.50
omena;4.95
appelsiini;8.0
...jne...
```
Kirjoita funktio lue_hedelmat, joka lukee hedelmätiedoston ja muodostaa siitä sanakirjan, jossa hedelmän nimi on avain ja hinta arvo. Hinnan tulee olla float-arvona sanakirjassa.

Huomaa, että tiedoston nimi on aina hedelmat.csv eikä funktiolle anneta parametria.

Lopuksi funktio palauttaa tämän sanakirjan.

Huom! Jos VS Code ei löydä tiedostoa vaikka olet tarkastanut tiedoston nimen kirjoitusasun, voit kokeilla täällä olevaa ohjetta.

[Vastaus](osa06-02_hedelmakauppa/src)

## Matriisi
Tiedostossa matriisi.txt on seuraavan esimerkin kaltainen matriisi:
```
1,0,2,8,2,1,3,2,5,2,2,2
9,2,4,5,2,4,2,4,1,10,4,2
...jne...
```
Kirjoita funktiot summa ja maksimi, jotka lukevat ja palauttavat nimensä mukaisesti matriisin kaikkien alkioiden summan ja suurimman alkion.

Kirjoita lisäksi funktio rivisummat, joka palauttaa listassa kaikkien matriisin rivien summat. Esimerkiksi matriisille
```
1,2,3
2,3,4
```
funktio palauttaisi listan [6, 9].

Vinkki: Voit kirjoittaa ohjelmaan myös muita funktioita – kannattaa siis miettiä, mitä kaikkia yhteisiä toimintoja kolmea funktiota varten vaaditaan. Huomaa, että tiedoston nimi on aina matriisi.txt eikä tehtävänannossa määritellyille funktioille anneta parametreja. Itse lisäämäsi funktiot voivat hyödyntää myös parametreja.

Huom! Jos VS Code ei löydä tiedostoa vaikka olet tarkastanut tiedoston nimen kirjoitusasun, voit kokeilla täällä olevaa ohjetta.

[Vastaus](osa06-03_matriisi/src)

## Kurssin tulokset, osa 1
Ohjelma käsittelee kahta CSV-muotoista tiedostoa. Toisessa on tieto opiskelijoista:
```
opnro;etunimi;sukunimi
12345678;pekka;peloton
12345687;jaana;javanainen
12345699;liisa;virtanen
```
ja toisessa opiskelijoiden viikoittaisesta tehtävien lukumäärästä:
```
opnro;v1;v2;v3;v4;v5;v6;v7
12345678;4;1;1;4;5;2;4
12345687;3;5;3;1;5;4;6
12345699;10;2;2;7;10;2;2
```
Molempien CSV-tiedostojen ensimmäinen rivi on otsikkorivi, joka kertoo kunkin kentän sisällön.

Tee ohjelma, joka kysyy tiedostojen nimet ja tämän jälkeen tulostaa kunkin opiskelijan tehtävien yhteenlasketun määrän. Ohjelma toimii seuraavasti, kun tiedostojen sisältö on yllä oleva:
```
Opiskelijatiedot: opiskelijat1.csv
Tehtävätiedot: tehtavat1.csv
pekka peloton 21
jaana javanainen 27
liisa virtanen 35
```
Vinkki: Ohjelman testaileminen on toivottoman hidasta, jos käyttäjä joutuu kirjoittamaan syötteen aina käsin. Testausvaiheessa syötteet kannattaakin antaa "kovakoodaamalla" ne esim. seuraavasti:
```python
if False:
    # tänne ei tulla
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # kovakoodatut syötteet
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
```
Ohjelman varsinainen toiminnallisuus on nyt "piilotettu" ehdon False-haaraan, jota ei suoriteta koskaan.

Jos taas halutaan nopeasti tarkastaa, toimiiko ohjelma myös käyttäjän kirjoittaessa syötteen, voidaan arvo False muuttaa arvoksi True:
```python
if True:
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
else:
    # tänne ei tulla!
    opiskelijatiedot = "opiskelijat1.csv"
    tehtavatiedot = "tehtavat1.csv"
```
Kun koodi on kunnossa, voi ehtorakenteen poistaa.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

Toinen huomio Jos VS Code ei löydä tiedostoa vaikka olet tarkastanut tiedoston nimen kirjoitusasun, voit täällä kokeilla olevaa ohjetta.

[Vastaus](osa06-04_kurssin_tulokset_osa1/src)

## Kurssin tulokset, osa 2
Edellinen tehtävä laajenee vielä siten, että myös opiskelijan koepisteet luetaan CSV-tiedostosta. Tiedoston sisältö näyttää seuraavalta:
```
opnro;k1;k2;k3
12345678;4;1;4
12345687;3;5;3
12345699;10;2;2
```
Esimerkiksi opiskelija jonka opiskelijanumero on 12345678 on saanut kokeesta 4+1+4 eli yhteensä 9 pistettä.

Ohjelma kysyy tiedostojen nimet ja tulostaa jokaisen opiskelijan arvosanan:
```
Opiskelijatiedot: opiskelijat1.csv
Tehtävätiedot: tehtavat1.csv
Koepisteet: koepisteet1.csv
pekka peloton 0
jaana javanainen 1
liisa virtanen 3
```
Tehtyjen harjoitustehtävien määrästä saa pisteitä siten, että vähintään 10 % tehtävämäärästä tuo 1 pisteen, vähintään 20% tuo 2 pistettä jne., ja 100 % eli 40 harjoitustehtävää tuo 10 pistettä. Harjoitustehtävistä saatava pistemäärä on kokonaisluku.

Kurssin arvosana määräytyy kokeen ja harjoituspisteiden summan perusteella seuraavan taulukon mukaan:

| kokeen pisteet + harjoitusten pisteet |	arvosana        |
|---------------------------------------|-----------------|
| 0-14	                                | 0 (eli hylätty) |
| 15-17	                                | 1               |
| 18-20	                                | 2               |
| 21-23	                                | 3               |
| 24-27	                                | 4               |
| 28-	                                  | 5               |

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa06-05_kurssin_tulokset_osa2/src)

## Kurssin tulokset, osa 3
Tässä tehtävässä muotoillaan edellisen tehtävän tulostus parempaan muotoon:
```
Opiskelijatiedot: opiskelijat1.csv
Tehtävätiedot: tehtavat1.csv
Koepisteet: koepisteet1.csv

nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3
```
Jokaisella rivillä siis tulostetaan opiskelijan tehtävien lukumäärä, tehtävistä saatavat pisteet, kokeen pisteet, yhteispisteet (koe+harjoitukset) sekä arvosana "siististi" siten, että tulostus on jaoteltu sarakkeisiin. Nimisarakkeen leveys on 30 merkkiä ja muiden sarakkeiden leveys on tasan 10 merkkiä.

Tehtävässä kannattaa käyttää osassa 4 käsiteltyjä f-merkkijonoja.

Kannattaa huomata, että merkkijonojen ja lukujen tulostaminen noudattaa hieman erilaista logiikkaa f-merkkijonoissa:
```python
sana = "python"
print(f"{sana:10}jatkuu")
print(f"{sana:>10}jatkuu")
```
```
python    jatkuu
    pythonjatkuu
```
Oletusarvoisesti siis merkkijono sisentyy määritellyn levyisen alueen vasempaan reunaan. Merkillä >voidaan ohjata tulostus sisentymään oikeaan reunaan.

Lukuja tulostettaessa logiikka on päinvastainen
```python
luku = 42
print(f"{luku:10}jatkuu")
print(f"{luku:<10}jatkuu")
```
```
        42jatkuu
42        jatkuu
```
Oletusarvo lukujen yhteydessä on tulostuksen sisentyminen oikeaan reunaan. Merkillä < voidaan ohjata luvun tulostus sisentymään vasempaan reunaan.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa06-06_kurssin_tulokset_osa3/src)

## Spell checker
Tee ohjelma, joka pyytää käyttäjää kirjoittamaan rivin englanninkielistä tekstiä. Ohjelma suorittaa tekstille oikeinkirjoitustarkistuksen ja tulostaa saman tekstin siten, että kaikki väärin kirjoitetut sanat on ympäröity tähdillä. Seuraavassa kaksi käyttöesimerkkiä:
```
Write text: We use ptython to make a spell checker

We use *ptython* to make a spell checker
```
```
Write text: This is acually a good and usefull program

This is *acually* good and *usefull* program
```
Kirjainten koolla ei ole merkitystä ohjelman toiminnan kannalta.

Ohjelma tunnistaa oikein kirjoitetut sanat käyttämällä tehtäväpohjassa olevaa tiedostoa wordlist.txt.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

Toinen huomio Jos VS Code ei löydä tiedostoa vaikka olet tarkastanut tiedoston nimen kirjoitusasun, voit täällä kokeilla olevaa ohjetta.

[Vastaus](osa06-07_spellchecker/src)

## Reseptihaku
Tässä tehtävässä tehdään ohjelma, joka tarjoaa käyttäjälle mahdollisuuden reseptien hakuun reseptin nimen, valmistusajan tai raaka-aineen nimen perusteella. Ohjelma lukee reseptit käyttäjän antamasta tiedostosta.

Jokainen resepti koostuu kolmesta tai useammasta rivistä reseptitiedostossa. Ensimmäisellä rivillä on reseptin nimi, toisella rivillä reseptin valmistusaika (kokonaisluku), ja kolmas ja sitä seuraavat rivit kertovat reseptin raaka-aineet. Reseptin raaka-aineiden kuvaus päättyy tyhjään riviin, poislukien viimeinen resepti. Tiedostossa voi olla useampia reseptejä. Alla kuvattuna esimerkkitiedosto.
```
Lettutaikina
15
maito
kananmuna
jauho
sokeri
suola
voi

Lihapullat
45
jauheliha
kananmuna
korppujauho

Tofurullat
30
tofu
riisi
vesi
porkkana
kurkku
avokado
wasabi

Pullataikina
60
maito
hiiva
kananmuna
suola
sokeri
kardemumma
voi
```
Vihje tässä tehtävässä lienee järkevintä lukea ensin tiedoston rivit listalle ja käsitellä sitten tätä listaa tehtävän edellyttämällä tavalla.

### Osa 1: reseptien haku nimen perusteella
Tee funktio hae_nimi(tiedosto: str, sana: str) joka hakee parametrina annetun nimisestä tiedostosta reseptit, joiden nimessä esiintyy toisena parametrina annettu merkkijono. Funktio palauttaa listan, jossa kutakin löydettyä reseptiä vastaa merkkijono, joka kertoo reseptin nimen.

Esimerkki funktion käytöstä:
```python
loydetyt = hae_nimi("reseptit1.txt", "pulla")

for resepti in loydetyt:
    print(resepti)
```
```
Lihapullat
Pullataikina
```

Huomaa, että hakusanojen kirjainten koolla ei ole merkitystä, eli hakusana pulla löytää myös reseptin Pullataikina, joka alkaa isolla kirjaimella.

Huom! Jos VS Code ei löydä tiedostoa vaikka olet tarkastanut tiedoston nimen kirjoitusasun, voit täällä kokeilla olevaa ohjetta.

### Osa 2: reseptien hakeminen valmistusajan perusteella
Tee funktio hae_aika(tiedosto: str, aika: int) joka hakee parametrina annetun nimisestä tiedostosta reseptit, joiden valmistusaika on korkeintaan parametrina kerrottu minuuttimäärä.

Kriteerin täyttävät reseptit palautetaan edellisen tehtävän tapaan listana, nyt kerrotaan myös reseptin valmistumisaika. Esimerkki funktion käytöstä:
```python
loydetyt = hae_aika("reseptit1.txt", 20)

for resepti in loydetyt:
    print(resepti)
```
```
Lettutaikina, valmistusaika 15 min
```

### Osa3: reseptien hakeminen raaka-aineen perusteella
Varoitus tämä osa on edellisiä selvästi haastavampi. Jos tehtävä ei lähde heti aukenemaan, kannattanee tehdä ensin osan muut tehtävät ja palata lopuksi takaisin tähän. Huomaa, että voit lähettää moniosaisessa tehtävässä palvelimelle myös yksittäiset osat

Tee funktio hae_raakaaine(tiedosto: str, aine: str) joka hakee parametrina annetun nimisestä tiedostosta reseptit, jotka sisältävät toisena parametrina annetun raaka-aineen.

Kriteerin täyttävät reseptit palautetaan edellisen tehtävän tapaan listana. Esimerkki funktion käytöstä:
```python
loydetyt = hae_raakaaine("reseptit1.txt", "maito")

for resepti in loydetyt:
    print(resepti)
```
```
Lettutaikina, valmistusaika 15 min
Pullataikina, valmistusaika 60 min
```

[Vastaus](osa06-08_reseptihaku/src)

## Kaupunkipyörät
Tässä tehtävässä tehdään muutama funktio, joiden avulla voidaan tarkastella kaupunkipyörien asemien sijaintia sisältävää tiedostoa.

Tiedostot näyttävät seuraavilta:
```
Longitude;Latitude;FID;name;total_slot;operative;id
24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
```
Kutakin asemaa kohti tiedostossa on yksi rivi, joka kertoo aseman koordinaatit, aseman nimen ja muuta tunnistetietoa.

### Osa 1: asemien välinen etäisyys
Tee ensin funktio hae_asematiedot(tiedosto: str), joka lukee asematiedot tiedostosta ja palauttaa ne sanakirjana, joka näyttää tältä:
```
{
  "Kaivopuisto: (24.950292890004903, 60.155444793742276),
  "Laivasillankatu: (24.956347471358754, 60.160959093887129),
  "Kapteeninpuistikko: (24.944927399779715, 60.158189199971673)
}
```
Eli sanakirjan avaimena on aseman nimi ja arvona tuple, joka koostuu aseman koordinaateista, ensimmäisenä Longitude ja toisena Latitude.

Tee seuraavaksi funktio etaisyys(asemat: dict, asema1: str, asema2: str), joka palauttaa parametrina kerrottujen asemien välisen etäisyyden.

Etäisyys lasketaan seuraavalla kaavalla (hyödyntäen Pythagoraan lausetta):
```python
# tämä rivi tarvitaan, jotta saadaan käyttöön metodi sqrt
import math

x_kilometreina = (longitude1 - longitude2) * 55.26
y_kilometreina = (latitude1 - latitude2) * 111.2
etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
```
Esimerkkisuorituksia:
```python
asemat = hae_asematiedot('stations1.csv')
e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
print(e)
e = etaisyys(asemat, "Viiskulma", "Kaivopuisto")
print(e)
```
```
0.9032737292463177
0.7753594392019532
```
Huom! Jos VS Code ei löydä tiedostoa vaikka olet tarkastanut tiedoston nimen kirjoitusasun, voit täällä kokeilla olevaa ohjetta.

### Osa 2: pisin välimatka
Tee funktio suurin_etaisyys(asemat: dict), joka selvittää, mitkä kaksi asemaa ovat kauimpana toisistaan. Funktio palauttaa tuplen, jonka ensimmäiset kaksi arvoa kertovat asemien nimet ja kolmas arvo niiden välisen etäisyyden.
```python
asemat = hae_asematiedot('stations1.csv')
asema1, asema2, suurin = suurin_etaisyys(asemat)
print(asema1, asema2, suurin)
```
```
Laivasillankatu Hietalahdentori 1.478708873076181
```

[Vastaus](osa06-09_kaupunkipyorat/src)

## Omistuskirjoitus
Tee ohjelma, joka kysyy nimeä ja luo "omistuskirjoituksen" käyttäjän haluamaan tiedostoon. Seuraavassa ohjelman esimerkkisuoritus:
```
Kenelle teos omistetaan: Arto
Mihin kirjoitetaan: omistettu.txt
```
Tiedoston omistettu.txt sisällöksi tulee
```
Hei Arto, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa06-10_omistuskirjoitus/src)

## Päiväkirja
Tee ohjelma, joka mallintaa yksinkertaista päiväkirjaa. Ohjelman tulee tallentaa päiväkirjamerkinnät tiedostoon paivakirja.txt. Kun ohjelma käynnistetään, se lukee merkinnät tiedostosta.

Huom! Paikalliset testit voivat muuttaa tiedoston sisältöä - kopioi siis tiedosto talteen ennen testien ajamista, jos haluat säilyttää sen sisällön.

Ohjelman tulee toimia seuraavan esimerkin mukaisesti:
```
1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta
Valinta: 1
Anna merkintä: Tänään söin puuroa
Päiväkirja tallennettu

1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta
Valinta: 2
Merkinnät:
Tänään söin puuroa
1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta
Valinta: 1
Anna merkintä: Illalla kävin saunassa
Päiväkirja tallennettu

1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta
Valinta: 2
Merkinnät:
Tänään söin puuroa
Illalla kävin saunassa
1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta
Valinta: 0
Heippa!
```
Uusi käynnistys:
```
Esimerkkitulostus
1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta
Valinta: 2
Merkinnät:
Tänään söin puuroa
Illalla kävin saunassa
1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta
Valinta: 0
Heippa!
```

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa06-11_paivakirja/src)

## Aineiston suodatus
Tiedostossa laskut.csv on tehtävien ratkaisuja seuraavan esimerkin mukaisesti:
```
Arto;2+5;7
Pekka;3-2;1
Erkki;9+3;11
Arto;8-3;4
Pekka;5+5;10
...jne...
```
Jokaisella rivin muoto on siis oppilaan_nimi;lasku;lopputulos. Laskut ovat kaikki esimerkin mukaisesti joko yhteen- tai vähennyslaskuja, ja kaikissa on kaksi operandia.

Kirjoita funktio suodata_laskut(), joka

- Lukee tiedoston laskut.csv sisällön ja
- kirjoittaa tiedostoon oikeat.csv ne rivit, joilla laskutoimituksen lopputulos on oikein sekä
- kirjoittaa tiedostoon vaarat.csv ne rivit, joilla laskutoimituksen lopputulos on väärin.

Edellisestä esimerkistä tiedostoon oikeat.csv olisi siis kirjoitettu rivit
```
Arto;2+5;7
Pekka;3-2;1
Pekka;5+5;10
```
Kaksi muuta riviä olisi kirjoitettu tiedostoon vaarat.csv.

Kirjoita rivit samassa järjestyksessä kuin ne esiintyvät alkuperäisessä tiedostossa. Älä muuta alkuperäistä tiedostoa.

Huomaa että funktion tulee toimia oikein siinäkin tapauksessa että funktiota kutsutaan monta kertaa perkkäin. Eli riippumatta siitä suoritatko funktion vain kerran
```python
suodata_laskut()
```
tai useita kertoja peräkkän
```python
suodata_laskut()
suodata_laskut()
suodata_laskut()
suodata_laskut()
```
tiedostojen sisältöjen tulee lopulta olla samat.

[Vastaus](osa06-12_aineiston_suodatus/src)

## Henkilöt talteen
Kirjoita funktio tallenna_henkilo(henkilo: tuple) joka saa parametrikseen henkilöä kuvaavan tuplen. Tuplessa on seuraavat tiedot tässä järjestyksessä:

- Nimi (merkkijono)
- Ikä (kokonaisluku)
- Pituus (liukuluku)

Tallenna henkilön tiedot tiedostoon henkilot.csv olemassa olevien tietojen perään. Tiedot tulee tallentaa muodosssa

nimi;ikä;pituus

eli yhden henkilön tiedot tulevat yhdelle riville. Jos funktiota esim. kutsuttaisiin parametrien arvoilla ("Kimmo Kimmonen", 37, 175.5), ohjelma kirjoittaisi tiedoston loppuun rivin
```
Kimmo Kimmonen;37;175.5
```

[Vastaus](osa06-13_henkilot_talteen/src)

## Kurssin tulokset, osa 4
Laajennetaan vielä hieman aiemmin kurssien tulokset generoivaa sovellusta.

Tällä hetkellä tiedostosta luetaan opiskelijoiden nimet, tehtäväpisteet sekä koepisteet. Laajennetaan ohjelmaa siten, että myös kurssin nimi ja laajuus luetaan tiedostosta, jonka muoto on seuraava (tiedosto on kirjoitettu ilman ääkkösiä, jotta se ei aiheuttaisi ongelmia Windowsissa):

Esimerkkidata

nimi: Ohjelmoinnin perusteet
laajuus opintopisteina: 5
Ohjelma luo kaksi tiedostoa. Tiedoston tulos.txt muoto on seuraava:
```
Esimerkkidata
Ohjelmoinnin perusteet, 5 opintopistettä
========================================
nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana
pekka peloton                 21        5         9         14        0
jaana javanainen              27        6         11        17        1
liisa virtanen                35        8         14        22        3
```

Tulokset kertova osa on siis samanlainen kuin tehtävän edellisen osan tulostus.

Tämän lisäksi luodaan tiedosto tulos.csv, jonka muoto on seuraava:
```
12345678;pekka peloton;0
12345687;jaana javanainen;1
12345699;liisa virtanen;3
```
Ohjelman suoritus näyttää seuraavalta:
```
opiskelijatiedot: opiskelijat1.csv
tehtävätiedot: tehtavat1.csv
koepisteet: koepisteet1.csv
kurssin tiedot: kurssi1.txt
Tulokset talletettu tiedostoihin tulos.txt ja tulos.csv
```

Ohjelma siis ainoastaan kyselee tiedostojen nimet ja varsinaiset tulokset tallennetaan vain tiedostoihin.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa06-14_kurssin_tulokset_osa4/src)

## Sanahaku
Tehtäväpohjasta löytyy tiedosto sanat.txt, joka sisältää englanninkielisiä sanoja.

Tehtäväsi on kirjoittaa funktio hae_sanat(hakusana: str), joka palauttaa listana annetun hakusanan mukaiset sanat tiedostosta.

Hakusanassa voi käyttää pienten kirjainten lisäksi seuraavia erikoismerkkejä:

- Piste . tarkoittaa, että mikä tahansa merkki käy (esim ca. vastaa vaikkapa sanoja cat ja car, p.ng sanoja ping ja pong ja .a.e sanoja sane, care tai late.
- Asteriski * tarkoittaa, että sanan alku- tai loppuosaksi käy mikä tahansa jono, esim. ca* vastaa vaikkapa sanoja california, cat, caring tai catapult. Vastaavasti hakusana *ane vastaa vaikkapa sanoja crane, insane tai aeroplane. Voit olettaa, että asteriski on aina joko hakusanan alussa tai lopussa, ja että hakusanassa esiintyy korkeintaan yksi asteriski.
- Jos hakusanassa ei ole erikoismerkkejä, haetaan vain täsmälleen hakusanaa vastaava sana.

Sovitaan, että samassa hakusanassa ei voi käyttää molempia erikoismerkkejä.

Sanat ovat tiedostossa kokonaan pienillä kirjaimilla kirjoitettuna. Voit myös olettaa, että funktion parametri on annettu kokonaan pienillä kirjaimilla.

Jos yhtään tulosta ei löydy, funktio palauttaa tyhjän listan.

Vinkki: Pythonin merkkijonometodeista startswith() ja endswith() saattaa olla hyötyä tehtävässä, googlaa niiden toiminta tarvittaessa tarkemmin!

Esimerkki funktion kutsumisesta:
```python
print(hae_sanat("*vokes"))
```

[Vastaus](osa06-15_sanahaku/src)

## Muistava sanakirja
Tee sanakirjaa mallintava ohjelma, johon voi syöttää uusia sanoja tai josta voi hakea syötettyjä sanoja.

Ohjelman tulee toimia näin:
```
1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
Valinta: 1
Anna sana suomeksi: auto
Anna sana englanniksi: car
Sanapari lisätty
1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
Valinta: 1
Anna sana suomeksi: roska
Anna sana englanniksi: garbage
Sanapari lisätty
1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
Valinta: 1
Anna sana suomeksi: laukku
Anna sana englanniksi: bag
Sanapari lisätty
1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
Valinta: 2
Anna sana: bag
roska - garbage
laukku - bag
1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
Valinta: 2
Anna sana: car
auto - car
1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
Valinta: 2
Anna sana: laukku
laukku - bag
1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu
Valinta: 3
Moi!
```
Sanat tallennetaan tiedostoon sanakirja.txt. Ohjelma lukee tiedoston sisällön kun se käynnistetään. Uudet sanaparit lisätään tiedostoon aina tallennuksen yhteydessä.

Voit itse päättää tiedostoon tallennettavan tiedon muodon.

Huomaa, että paikallisten TMC-testien ajaminen voi tyhjentää sanakirja-tiedoston.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa06-16_muistava_sanakirja/src)

## Syötteen luku


[Vastaus](osa06-17_syotteen_luku/src)

## Parametrien validointi


[Vastaus](osa06-18_parametrien_validointi/src)

## Virheelliset lottonumerot


[Vastaus](osa06-19_virheelliset_lottonumerot/src)



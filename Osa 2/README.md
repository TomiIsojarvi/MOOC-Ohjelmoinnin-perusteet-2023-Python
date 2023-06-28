# Osa 2 - Tehtävien vastaukset
## Korjaa virheet
Seuraavassa ohjelmassa on useita syntaksivirheitä. Korjaa ohjelma siten, että syntaksi on kunnossa ja se toimii alla olevien esimerkkien mukaisesti.
```
  luku = input("Anna luku: ")
  if luku>100
    print("Luku oli suurempi kuin sata")
    luku - 100
    print("Nyt luvun arvo on pienentynyt sadalla)
     print("Arvo on nyt"+ luku)
 print(luku + " taitaa olla onnenlukuni!")
 print("Hyvää päivänjatkoa!)
```
```
Anna luku: 13
13 taitaa olla onnenlukuni!
Hyvää päivänjatkoa!
```
```
Anna luku: 101
Luku oli suurempi kuin sata
Nyt luvun arvo on pienentynyt sadalla
Arvo on nyt 1
1 taitaa olla onnenlukuni!
Hyvää päivänjatkoa!
```
## Merkkien määrä
Funktiolla len voidaan laskea (muun muassa) merkkijonon pituus. Funktio palauttaa merkkijonossa olevien merkkien määrän.

Esimerkkejä funktion toiminnasta:
```
sana = "abcd"
print(len(sana))

print(len("moikka"))

sana2 = "heipparallaa"
pituus = len(sana2)
print(pituus)

tyhja_merkkijono = ""
pituus = len(tyhja_merkkijono)
print(pituus)
```
```
4
6
12
0
```

Tee ohjelma, joka lukee käyttäjältä sanan ja tulostaa sanan merkkien määrän, mikäli niitä on enemmän kuin yksi.

Esimerkkisuorituksia:

```
Anna sana: hei
Sanassa hei on 3 kirjainta
Kiitos!
```
```
Anna sana: banaani
Sanassa banaani on 7 kirjainta
Kiitos!
```
```
Anna sana: b
Kiitos!
```
## Tyyppimuunnos
Pythonissa voidaan usein muuntaa jokin arvo tyypistä toiseen. Esimerkiksi liukuluku voidaan muuntaa kokonaisluvuksi funktion int avulla:
```
lampo = float(input("Anna lämpötila: "))

print("Lämpötila on", lampo)

print("...eli pyöreästi", int(lampo))
```
```
Anna lämpötila: 5.15
Lämpötila on 5.15
...eli pyöreästi 5
```

Huomaa, että funktio ei pyöristä arvoa matematiikasta tutulla tavalla, vaan pyöristää luvun alaspäin (kyse on siis ns. lattiafunktiosta):

```
Anna lämpötila: 8.99
Lämpötila on 8.99
...eli pyöreästi 8
```

Tee int-funktiota hyödyntäen ohjelma, joka kysyy käyttäjältä desimaaliluvun ja tulostaa erikseen luvun kokonaisosan ja desimaaliosan.

Huom! Voit olettaa, että annettu desimaaliluku on suurempi kuin nolla.

Esimerkiksi

```
Anna luku: 1.34
Kokonaisosa: 1
Desimaaliosa: 0.34
```
## Täysi-ikäisyys
Tee ohjelma, joka kysyy käyttäjän ikää ja kertoo, onko tämä täysi-ikäinen (eli 18-vuotias tai vanhempi).

Esimerkkitulostuksia:
```
Kuinka vanha olet? 12
Et ole täysi-ikäinen!
```
```
Kuinka vanha olet? 32
Olet täysi-ikäinen!
```
## Suurempi tai yhtäsuuri
Tee ohjelma, joka kysyy käyttäjältä kaksi kokonaislukua ja tulostaa niistä suuremman. Jos luvut ovat yhtä suuret, ohjelma huomaa myös tämän.

Esimerkkitulostuksia:
```
Anna ensimmäinen luku: 5
Anna toinen luku: 3
Suurempi luku: 5
```
```
Anna ensimmäinen luku: 5
Anna toinen luku: 8
Suurempi luku: 8
```
```
Anna ensimmäinen luku: 5
Anna toinen luku: 5
Luvut ovat yhtä suuret!
```
## Vanhempi
Tee ohjelma, joka kysyy kahden henkilön nimen ja iän ja tulostaa vanhemman henkilön nimen.

Esimerkkisyötteitä
```
Henkilö 1:
Nimi: Teppo
Ikä: 26
Henkilö 2:
Nimi: Tiina
Ikä: 27
Vanhempi on Tiina
```
```
Henkilö 1:
Nimi: Antti
Ikä: 1
Henkilö 2:
Nimi: Venla
Ikä: 1
Antti ja Venla ovat yhtä vanhoja
```
## Aakkosjärjestyksessä viimeinen
Lukujen lisäksi Python osaa vertailla myös merkkijonojen suuruusjärjestystä. Merkkijono a on pienempi kuin merkkijono b, jos merkkijono a tulee aakkosjärjestyksessä ennen jonoa b. Huomaa kuitenkin, että tämä pätee varmasti vain kun

vertaillaan samankokoisia kirjaimia (eli ISOJA tai pieniä kirjaimia) keskenään ja
vertailtavissa sanoissa on vain englannin kielestä tuttuja kirjaimia (eli a-z tai A-Z).
Tee ohjelma, joka kysyy käyttäjältä kahta sanaa. Ohjelma tulostaa sanoista sen, joka on aakkosjärjestyksessä jälkimmäinen.

Voit olettaa, että sanat on syötetty kokonaan pienillä kirjaimilla.

Esimerkkisuorituksia eri syötteillä:
```
Anna 1. sana: auto
Anna 2. sana: mopo
mopo on aakkosjärjestyksessä viimeinen.
```
```
Anna 1. sana: zorro
Anna 2. sana: batman
zorro on aakkosjärjestyksessä viimeinen.
```
```
Anna 1. sana: python
Anna 2. sana: python
Annoit saman sanan kahdesti.
```
## Iän tarkistus
Tee ohjelma, joka kysyy käyttäjän ikää. Jos ikä ei ole uskottava (se on alle 5 tai mahdoton luku iälle), antaa ohjelma siihen liittyvän kommentin.

Vinkki: tarkastele esimerkkisuorituksia löytääksesi oikean vastineen eri vaihtoehdoille.

Esimerkkitulostuksia:
```
Kerro ikäsi? 13
Ok, olet siis 13-vuotias
```
```
Kerro ikäsi? 2
En usko, että osaat kirjoittaa...
```
```
Kerro ikäsi? -4
Taitaa olla virhe
```
## Veljenpojat
Tee ohjelma, joka kysyy käyttäjän nimeä. Jos nimeksi syötetään Tupu, Hupu tai Lupu, ohjelma tunnistaa käyttäjän Aku Ankan veljenpojaksi.

Jos nimeksi annetaan Mortti tai Vertti, ohjelma vastaavasti tunnistaa käyttäjän Mikki Hiiren veljenpojaksi.

Esimerkkitulostuksia:
```
Anna nimesi: Mortti
Olet luultavasti Mikki Hiiren veljenpoika.
```
```
Anna nimesi: Hupu
Olet luultavasti Aku Ankan veljenpoika.
```
```
Anna nimesi: Keijo
Et ole kenenkään tuntemani hahmon veljenpoika.
```
## Arvosana ja pisteet
Alla oleva taulukko kuvaa erään kurssin arvosanan muodostumista. Tee ohjelma, joka ilmoittaa kurssiarvosanan annetun taulukon mukaisesti.

| pistemäärä | arvosana    |
|------------|-------------|
| < 0	       | mahdotonta! |
| 0-49	     | hylätty     |
| 50-59	     | 1           |
| 60-69	     | 2           |
| 70-79	     | 3           |
| 80-89	     | 4           |
| 90-100	   | 5           |
| > 100	     | mahdotonta! |


Esimerkkitulostuksia:
```
Anna pisteet [0-100]: 37
Arvosana: hylätty
```
```
Anna pisteet [0-100]: 76
Arvosana: 3
```
```
Anna pisteet [0-100]: -3
Arvosana: mahdotonta!
```
## FizzBuzz
Ohjelma kysyy käyttäjältä lukua. Jos luku on jaollinen kolmella, tulostetaan Fizz. Jos luku on jaollinen viidellä, tulostetaan Buzz. Jos luku on jaollinen sekä kolmella, että viidellä, tulostetaan FizzBuzz

Esimerkkitulostuksia:
```
Luku: 9
Fizz
```
```
Luku: 7
```
```
Luku: 20
Buzz
```
```
Luku: 45
FizzBuzz
```
## Karkausvuosi
Vuosi on karkausvuosi, jos se on jaollinen 4:llä. Kuitenkin jos vuosi on jaollinen 100:lla, se on karkausvuosi vain silloin, kun se on jaollinen myös 400:lla.

Tee ohjelma, joka lukee käyttäjältä vuosiluvun, ja tarkistaa, onko vuosi karkausvuosi.
```
Anna vuosi: 2011
Vuosi ei ole karkausvuosi.
```
```
Anna vuosi: 2020
Vuosi on karkausvuosi.
```
```
Anna vuosi: 1800
Vuosi ei ole karkausvuosi.
```
## Aakkosjärjestyksessä keskimmäinen
Tee ohjelma, joka kysyy käyttäjältä kolme kirjainta. Ohjelma tulostaa kirjaimista aakkosjärjestyksessä keskimmäisen.

Voit olettaa, että kirjaimet ovat joko kaikki isoja tai kaikki pieniä kirjaimia.

Esimerkkisuorituksia:
```
Anna 1. kirjain: x
Anna 2. kirjain: c
Anna 3. kirjain: p
Keskimmäinen kirjain on p
```
```
Anna 1. kirjain: C
Anna 2. kirjain: B
Anna 3. kirjain: A
Keskimmäinen kirjain on B
```
## Lahjaverolaskuri
Verottajan mukaan lahja tarkoittaa sitä, että omaisuus siirtyy toiselle henkilölle ilman korvausta. Lahjasta pitää maksaa lahjaveroa, jos samalta lahjanantajalta saatujen lahjojen arvo on kolmen vuoden aikana 5 000 euroa tai enemmän.

Kun lahja tulee lähimmiltä sukulaisilta, lahjaveron määrä määräytyy seuraavan taulukon mukaan:

| Lahja               |	Vero alarajalla |	Veroprosentti ylimenevästä |
|---------------------|-----------------|----------------------------|
| 5 000 — 25 000	    | 100	            | 8                          |
| 25 000 — 55 000	    | 1 700	          | 10                         |
| 55 000 — 200 000	  | 4 700	          | 12                         |
| 200 000 — 1 000 000 |	22 100	        | 15                         |
| 1 000 000 —	        | 142 100 	      | 17                         |

Esimerkiksi 6000 euron lahjasta tulee maksaa veroa 180 euroa (100 + (6000-5000) * 0.08) ja 75000 euron lahjasta tulee maksaa veroa 7100 euroa (4700 + (75000-55000) * 0.12).

Tee ohjelma, joka laskee lahjaveron lähimpien sukulaisten antamalle lahjalle. Alla on muutama esimerkki ohjelman toiminnasta.
```
Lahjan suuruus? 3500
Ei veroa!
```
```
Lahjan suuruus? 5000
Vero: 100.0 euroa
```
```
Lahjan suuruus? 27500
Vero: 1950.0 euroa
```
## Jatketaanko
Kirjoita edellä olevaa toistolause-esimerkkiä mukaillen ohjelma, joka tulostaa viestin "moi" ja kysyy käyttäjältä "Jatketaanko?" kunnes käyttäjä syöttää merkkijonon "ei". Tämän jälkeen tulostetaan merkkijono "ei sitten" ja suoritus päättyy.

Esimerkkitulostus
```
moi
Jatketaanko? kyllä
moi
Jatketaanko? yes
moi
Jatketaanko? jawohl
moi
Jatketaanko? ei
ei sitten
```
## Syötteen rajaus
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja. Mikäli luku on negatiivinen (eli pienempi kuin nolla), käyttäjälle tulostetaan viesti "Epäkelpo luku" ja käyttäjältä kysytään uutta lukua. Jos taas luku on nolla, lukujen lukeminen lopetetaan ja ohjelma poistuu toistolauseesta.

Mikäli luku on positiivinen, ohjelma tulostaa luvun neliöjuuren käyttäen sqrt-funktiota, joka on tuotu ohjelmaan import-lauseella. Esimerkki funktion käytöstä:
```
# Tämä pitää olla ohjelman alussa, jotta sqrt toimii
from math import sqrt

print(sqrt(9))
```
```
3.0
```
Esimerkki ohjelman suorituksesta:
```
Syötä luku: 16
4.0
Syötä luku: 4
2.0
Syötä luku: -3
Epäkelpo luku
Syötä luku: 1
1.0
Syötä luku: 0
Lopetetaan...
```
## Lähtölaskenta
Tehtäväpohjassa olevan ohjelman
```
luku = 5
print("Lähtölaskenta!")
while True:
  print(luku)
  luku = luku - 1
  if luku > 0:
    break

print("Nyt!")
```
olisi tarkoitus toimia seuraavasti:
```
Lähtölaskenta!
5
4
3
2
1
Nyt!
```
Korjaa ohjelmassa oleva ongelma.
## Salasana uudelleen
Tee ohjelma, joka kysyy käyttäjältä salasanaa ja tämän jälkeen pyytää toistamaan salasanan niin kauan, kunnes käyttäjä syöttää ensimmäisenä annetun salasanan uudelleen.
```
Salasana: sekred
Toista salasana: salainen
Ei ollut sama!
Toista salasana: enmuistaenää123
Ei ollut sama!
Toista salasana: sekred
Käyttäjätunnus luotu!
```
## PIN ja yritysten määrä
Tee sovellus, joka kysyy käyttäjältä PIN-koodia niin kauan, kunnes käyttäjä antaa oikean PIN-koodin 4321. Ohjelma kertoo yritysten lukumäärän:
```
PIN-koodi: 3245
Väärin
PIN-koodi: 1234
Väärin
PIN-koodi: 0000
Väärin
PIN-koodi: 4321
Oikein, tarvitsit 4 yritystä
```
Tulostus on hieman erilainen jos PIN-koodi on oikea heti ensimmäisellä yrityksellä:
```
PIN-koodi: 4321
Oikein, tarvitsit vain yhden yrityksen!
```
## Seuraava karkausvuosi
Tee ohjelma, joka kyselee käyttäjältä vuosilukua ja kertoo, milloin on seuraava karkausvuosi.
```
Vuosi: 2019
Vuotta 2019 seuraava karkausvuosi on 2020
```
Jos käyttäjän syöttämä vuosi on karkausvuosi (kuten 2020), ohjelma ei kerro tätä vuotta vaan sitä seuraavan karkausvuoden:
```
Vuosi: 2020
Vuotta 2020 seuraava karkausvuosi on 2024
```
## Tarina
### Osa 1
Tee ohjelma, joka pyytää käyttäjää syöttämään sanoja. Kun käyttäjä syöttää sanan loppu, ohjelma tulostaa sanoista muodostuneen tarinan ja suoritus päättyy.
```
Anna sana: Olipa
Anna sana: kerran
Anna sana: pieni
Anna sana: talo
Anna sana: preerialla
Anna sana: loppu
Olipa kerran pieni talo preerialla
```
### Osa 2
Muokkaa edellisen tehtävän ohjelmaa niin, että sanojen syöttäminen päättyy, jos käyttäjä syöttää sanan loppu tai käyttäjä syöttää saman sanan kaksi kertaa peräkkäin.
```
Anna sana: Alussa
Anna sana: oli
Anna sana: suo
Anna sana: kuokka
Anna sana: ja
Anna sana: Jussi
Anna sana: Jussi
Alussa oli suo kuokka ja Jussi
```
## Lukujen käsittelyä
Tee ohjelma, joka pyytää käyttäjää syöttämään kokonaislukuja. Ohjelma pyytää lukuja niin kauan kunnes käyttäjä syöttää nollan.
```
Syötä kokonaislukuja, 0 lopettaa:
Luku: 5
Luku: 22
Luku: 9
Luku: -2
Luku: 0
```
### Osa 1: lukumäärä
Syötteiden lukemisen jälkeen ohjelman tulee tulostaa syötettyjen lukujen lukumäärä. Syötteen loppumisesta kertovaa nollaa ei tule ottaa huomioon lukumäärässä.

Tarvitset tässä uuden muuttujan, jonka avulla pidät kirjaa luettujen lukujen määrästä.
```
... lukujen kysely
Lukuja yhteensä 4
```
### Osa 2: summa
Laajenna ohjelmaa siten, että se tulostaa syötettyjen lukujen summa. Syötteen loppumisesta kertovaa nollaa ei tule ottaa huomioon summan laskemisessa.

Ohjelman tulostus laajenee seuraavasti:
```
... lukujen kysely
Lukuja yhteensä 4
Lukujen summa 34
```
### Osa 3: keskiarvo
Laajenna ohjelmaa siten, että se tulostaa syötettyjen lukujen keskiarvon. Syötteen loppumisesta kertovaa nollaa ei tule ottaa huomioon keskiarvon laskemisessa. Voit olettaa, että käyttäjä syöttää aina vähintään yhden luvun.
```
... lukujen kysely
Lukuja yhteensä 4
Lukujen summa 34
Lukujen keskiarvo 8.5
```
### Osa 4: positiiviset ja negatiiviset
Laajenna ohjelmaa siten, että se tulostaa positiivisten ja negatiivisten lukujen lukumäärät
```
... lukujen kysely
Lukuja yhteensä 4
Lukujen summa 34
Lukujen keskiarvo 8.5
Positiivisia 3
Negatiivisia 1
```

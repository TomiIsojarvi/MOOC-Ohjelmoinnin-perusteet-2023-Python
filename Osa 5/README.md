# Osa 5 - Tehtävien vastaukset
## Pisin merkkijono
HUOM: tämä ja seuraava tehtävä ovat väärässä järjestyksessä VS Coden sivupalkissa

Tee funktio pisin(merkkijonot: list), joka saa parametrikseen listan merkkijonoja. Funktio etsii ja palauttaa listalta pisimmän merkkijonon. Voit olettaa, että vain yksi jonoista on pisin.

Esimerkkikutsu:
```python
if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))
```
```
hellurei
```

[Vastaus](osa05-01a_pisin_merkkijono/src)

## Alkioiden määrä
HUOM: tämä ja edellinen tehtävä ovat väärässä järjestyksessä VS Coden sivupalkissa

Tee funktio laske_alkiot(matriisi: list, alkio: int), joka saa parametrikseen kaksiulotteisen kokonaislukutaulukon. Funktio laskee, kuinka monta annetun alkion mukaista arvoa taulukosta löytyy.

Esimerkiksi
```python
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(laske_alkiot(m, 1))
```
```
3
```

[Vastaus](osa05-01_alkoiden_maara/src)

## Go
Go-pelissä lisätään vuorotellen mustia ja valkoisia kiviä pelilaudalle. Pelin voittaa se pelaaja, joka saa omilla kivillään rajattua enemmän aluetta pelilaudalta.

Kirjoita funktio kumpi_voitti(pelilauta: list), joka saa parametrikseen kaksiulotteisen taulukon, joka kuvaa pelilautaa. Taulukko koostuu kokonaisluvuista seuraavasti:

- 0: tyhjä ruutu
- 1: pelaajan 1 nappula
- 2: pelaajan 2 nappula
Esimerkissä pelilaudan koko voi olla mikä tahansa.

Funktio palauttaa arvon 1, jos pelaaja 1 on voittanut pelin, ja arvon 2, jos pelaaja 2 on voittanut pelin. Jos molemmilla pelaajilla on yhtä paljon nappuloita laudalla, funktio palauttaa arvon 0.

[Vastaus](osa05-02_go/src)

## Sudoku: rivit oikein
Tee funktio rivi_oikein(sudoku: list, rivi_nro: int), joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen taulukon ja rivin numeron kertovan kokonaisluvun (rivit on numeroitu nollasta alkaen). Metodi palauttaa tiedon, onko rivi oikein täytetty eli onko siinä kukin luvuista 1–9 korkeintaan kerran.
```python
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(rivi_oikein(sudoku, 0))
print(rivi_oikein(sudoku, 1))
```
```
True
False
```

[Vastaus](osa05-03_sudoku_osa1/src)

## Sudoku: sarakkeet oikein
Tee funktio sarake_oikein(sudoku: list, sarake_nro: int), joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen taulukon ja sarakkeen (eli pystyrivin) numeron kertovan kokonaisluvun. Metodi palauttaa tiedon, onko sarake oikein täytetty eli onko siinä kukin luvuista 1–9 korkeintaan kerran.
```python
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sarake_oikein(sudoku, 0))
print(sarake_oikein(sudoku, 1))
```
```
False
True
```

[Vastaus](osa05-04_sudoku_osa2/src)

## Sudoku: neliöt oikein
Tee funktio nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int), joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen taulukon sekä yhden ruudun paikan kertovat rivi- ja sarakenumerot.

Funktio kertoo onko parametrina saadusta rivi/sarakenumerosta alkava 3x3-kokoinen neliö oikein täytetty eli onko siinä kukin luvuista 1–9 korkeintaan kerran.

Huomaa, että tässä tehtävässä toteutettava funktio on hieman yleiskäyttöisempi kuin sudokussa oikeasti tarvitaan. Todellisuudessahan oikeassa sudokussa tarkastellaan ainoastaan kohdista (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) ja (6, 6) alkavia neliöitä.
```python
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(nelio_oikein(sudoku, 0, 0))
print(nelio_oikein(sudoku, 1, 2))
```
```
False
True
```
Ensimmäisen funktiokutsun tarkastelema kohdasta 0, 0 alkava neliö on
```
9 0 0
2 0 0
0 2 0
```
Toisen funktiokutsun tarkastelema kohdasta riviltä 1 ja sarakkeesta 2 alkava neliö on
```
0 2 5
0 3 0
4 0 0
```
Tämä neliö on siis sellainen, jota oikeassa sudokussa ei tarkasteltaisi.

[Vastaus](osa05-05_sudoku_osa3/src)

## Sudoku: ruudukko oikein
Tee funktio sudoku_oikein(sudoku: list), joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen taulukon. Funktio kertoo käyttäen edellisen kolmen tehtävän funktioita (kopioi ne tämän tehtävän koodin joukkoon), onko parametrina saatu ruudukko täytetty oikein, eli sen jokainen rivi, jokainen sarake sekä kaikki erilliset 3x3-neliöt sisältävät korkeintaan kertaalleen jokaisen luvuista 1–9.

Huom: ylempänä olevaan sudokuruudukkoa esittävään kuvaan on merkitty ne 3x3-neliöt, joita sudokua ratkaistessa tulee tarkastella. Nämä ovat siis kohdista (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) ja (6, 6) alkavat yhdeksän neliöä.
```python
sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_oikein(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_oikein(sudoku2))
```
```
False
True
```

[Vastaus](osa05-06_sudoku_osa4/src)

## Alkiot tuplana
Tee funktio tuplaa_alkiot(luvut: list), joka saa parametrikseen lukuja sisältävän listan.

Funktio palauttaa uuden listan, jossa alkuperäisen listan alkiot on kerrottu kahdella. Funkto ei saa muuttaa alkuperäistä listaa.

Esimerkki funktion kutsumisesta:
```python
if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)
```
```
alkuperäinen: [2, 4, 5, 3, 11, -4]
tuplattu: [4, 8, 10, 6, 22, -8]
```

[Vastaus](osa05-06a_alkiot_tuplana/src)

## Poista pienin
Tee funktio poista_pienin(luvut: list), joka saa parametrikseen lukuja sisältävän listan.

Funktio etsii ja poistaa listasta pienimmän alkion. Voit olettaa, että pienin alkio esiintyy listassa vain kerran.

Funktio ei siis palauta mitään, vaan muokkaa parametrinaan saamaansa listaa!

Esimerkki funktion kutsumisesta:
```python
if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)
```
```
[2, 4, 6, 3, 5]
```

[Vastaus](osa05-06b_poista_pienin/src)

## Sudoku: ruudukon tulostus ja luvun lisäys
Tässä tehtävässä toteutetaan vielä kaksi funktiota sudokua varten: tulosta ja lisays.

Funktio tulosta saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen listan ja tulostaa sen alla olevan esimerkkitulostuksen mukaisessa muodossa.

Funktio lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int) saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen listan, rivi- ja sarakenumerot sekä luvun väliltä 1–9. Funktio lisää luvun parametrien ilmoittamaan kohtaan sudokuruudukkoa.
```python
sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

tulosta(sudoku)
lisays(sudoku, 0, 0, 2)
lisays(sudoku, 1, 2, 7)
lisays(sudoku, 5, 7, 3)
print()
print("Kolme numeroa lisätty:")
print()
tulosta(sudoku)
```
```
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Kolme numeroa lisätty:

2 _ _  _ _ _  _ _ _
_ _ 7  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ 3 _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
```
Vihje

Saatat tässä tehtävässä hyötyä siitä, että print-komentoa on mahdollista käyttää myös siten, että se ei aiheuta rivinvaihtoa:
```python
print("merkkejä ", end="")
print("ilman välejä", end="")
```
```
merkkejä ilman välejä
```
Joskus taas tarvitaan pelkkää rivinvaihtoa, ja se onnistuu seuraavasti:
```python
print()
```

[Vastaus](osa05-07_sudoku_osa5/src)

## Sudoku: luvun lisäys ruudukon kopioon
Viimeisessä sudokua käsittelevässä tehtävässä toteutetaan hieman erilainen versio funktiosta, jonka avulla sudokuruudukkoon lisätään uusia lukuja.

Funktio kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int) saa parametreikseen sudokuruudukkoa esittävän kaksiulotteisen listan, rivinumeron, sarakenumeron sekä luvun väliltä 1–9. Funktio palauttaa parametrina saadusta sudokuruudukosta kopion, johon on lisätty parametrina saatu luku parametrina saatuun sijaintiin sijoitettuna. Funktio ei saa muuttaa parametrina annettua sudokuruudukkoa.

Seuraavassa on edellisen tehtävän funktiota tulosta hyödyntävä käyttöesimerkki:
```python
sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
print("Alkuperäinen:")
tulosta(sudoku)
print()
print("Kopio:")
tulosta(kopio)
```
```
Alkuperäinen:
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

Kopio:
2 _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _

_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
_ _ _  _ _ _  _ _ _
```
Vihje tässä tehtävässä pitää olla tarkkana mitä kaikkea tulee kopioida, ja mihin lisäys lopulta kohdistuu. Kuten yleensäkin, visualisaattori auttaa myös nyt. Sudokuruudukon koon takia näkymä tosin on hieman normaalia sekavampi.

[Vastaus](osa05-08_sudoku_osa6/src)

## Ristinolla
Ristinollaa pelataan 3 x 3 -kokoisella ruudukolla, johon pelaajat merkitsevät vuorotellen ristin tai nollan. Pelin voittaa se pelaaja, joka saa ensimmäisenä kolme merkkiä pystyyn, vaakaan tai kulmittain. Peli päättyy tasapeliin, jos kumpikaan pelaaja ei saa kolmen sarjaa.

Kirjoita funktio pelaa_siirto(lauta: list, x: int, y: int, nappula: str), jossa sijoitetaan annettu pelinappula annettuihin koordinaatteihin pelilaudalla. Koordinaattien arvot ovat väliltä 0..2.

Huomaa että tässä tehtävässä parametrit ovat eri päin kuin sudokussa, ensin annetaan saraketta kuvaava x ja sen jälkeen riviä kuvaava y.

Pelilauta koostuu merkkijonoista seuraavasti:

"": tyhjä ruutu
"X": pelaajan 1 merkki
"O": pelaajan 2 merkki
Funktio palauttaa arvon True, jos nappula saatiin sijoitettua laudalle (eli jos paikka oli tyhjä), ja arvon False, jos paikka oli varattu TAI jos koordinaatin arvo oli liian pieni tai suuri (eli ei väliltä 0..2).

Esimerkiksi:
```python
lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
print(pelaa_siirto(lauta, 2, 0, "X"))
print(lauta)
```
```
True
[['', '', 'X'], ['', '', ''], ['', '', '']]
```

[Vastaus](osa05-09_ristinolla/src)

## Matriisin kääntö
Kirjoita funktio transponoi(matriisi: list), joka saa parametrikseen kaksiulotteisen kokonaislukuja sisältävän taulukon eli matriisin. Funktio transponoi matriisin eli muuntaa rivit sarakkeiksi ja päinvastoin.

Voit olettaa, että matriisissa on yhtä monta riviä kuin sarakettakin (eli matriisi on neliömatriisi).

Esimerkiksi matriisista
```
1 2 3
4 5 6
7 8 9
```
tulisi transponoinnin jälkeen tällainen:
```
1 4 7
2 5 8
3 6 9
```
Funktio ei palauta mitään, vaan muokkaa parametrinaan saamaansa matriisia.

[Vastaus](osa05-10_matriisin_kaanto/src)

## Kertaa kymmenen
Tee funktio kertaa_kymmenen(alku: int, loppu: int), joka muodostaa ja palauttaa uuden sanakirjan. Sanakirjassa on avaimina luvut väliltä alku..loppu.

Jokaisen avaimen arvona on avain kerrottuna kymmenellä.

Esimerkiksi:
```python
d = kertaa_kymmenen(3, 6)
print(d)
```
```
{3: 30, 4: 40, 5: 50, 6: 60}
```

[Vastaus](osa05-10b_kertaa_kymmenen/src)

## Kertomat
Tee funktio kertomat(n: int), joka palauttaa lukujen 1..n kertomat sanakirjassa siten, että luku on avain ja luvun kertoma arvo, johon avain viittaa.

Muistutuksena: luvun n kertoma n! lasketaan kertomalla luku kaikilla itseään pienemmillä positiivisilla kokonaisluvuilla. Luvun 4 kertoma on siis 4 * 3 * 2 * 1 = 24.

Esimerkki käytöstä:
```python
k = kertomat(5)
print(k[1])
print(k[3])
print(k[5])
```
```
1
6
120
```

[Vastaus](osa05-11_kertomat/src)

## Histogrammi
Tee funktio histogrammi, joka saa parametrina merkkijonon ja tulostaa merkkijonon eri kirjainten lukumäärää kuvaavan histogrammin, jossa kirjaimen jokaista esiintymää kohti tulostuu yksi tähti kirjaimen riville.

Esimerkiksi kutsuttaessa histogrammi("abba") tulostus on:
```
a **
b **
```
Vastaavasti kutsuttaessa histogrammi("saippuakauppias") tulostus on:
```
s **
a ****
i **
p ****
u **
k *
```

[Vastaus](osa05-12_histogrammi/src)

## Puhelinluettelo, versio 1
Tee puhelinluettelo, joka toimii seuraavasti:
```
komento (1 hae, 2 lisää, 3 lopeta): 2
nimi: pekka
numero: 040-5466745
ok!
komento (1 hae, 2 lisää, 3 lopeta): 2
nimi: emilia
numero: 045-1212344
ok!
komento (1 hae, 2 lisää, 3 lopeta): 1
nimi: pekka
040-5466745
komento (1 hae, 2 lisää, 3 lopeta): 1
nimi: maija
ei numeroa
komento (1 hae, 2 lisää, 3 lopeta): 2
nimi: pekka
numero: 09-22223333
ok!
komento (1 hae, 2 lisää, 3 lopeta): 1
nimi: pekka
09-22223333
komento (1 hae, 2 lisää, 3 lopeta): 3
lopetetaan...
```

Huomaa, että jokaiseen nimeen voi liittyä vain yksi puhelinnumero. Jos samalle henkilölle lisätään uusi numero, se korvaa aiemmin lisätyn numeron.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa05-13_puhelinluettelo_versio1/src)

## Puhelinluettelo, versio 2
Tee puhelinluettelosta paranneltu versio, missä jokaisella henkilöllä voi olla useampia puhelinnumeroita. Ohjelma toimii kuten edellisessä tehtävässä, mutta nyt se listaa jokaisen numeron:
```
komento (1 hae, 2 lisää, 3 lopeta): 2
nimi: pekka
numero: 040-5466745
ok!
komento (1 hae, 2 lisää, 3 lopeta): 2
nimi: emilia
numero: 045-1212344
ok!
komento (1 hae, 2 lisää, 3 lopeta): 1
nimi: pekka
040-5466745
komento (1 hae, 2 lisää, 3 lopeta): 1
nimi: maija
ei numeroa
komento (1 hae, 2 lisää, 3 lopeta): 2
nimi: pekka
numero: 09-22223333
ok!
komento (1 hae, 2 lisää, 3 lopeta): 1
nimi: pekka
040-5466745
09-22223333
komento (1 hae, 2 lisää, 3 lopeta): 3
lopetetaan...
```

[Vastaus](osa05-14_puhelinluettelo_versio2/src)

## Sanakirjan kääntö
Kirjoita funktio kaanna(sanakirja: dict), joka saa parametrikseen sanakirjan ja kääntää sen niin, että arvoista tulee avaimia ja päinvastoin.

Esimerkki funktion käytöstä:
```python
s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
kaanna(s)
print(s)
```
```
{"eka": 1, "toka": 2, "kolmas": 3, "neljas": 4}
```

Huomaa, että tämä pitää paikkansa myös parametrina oleville sanakirjoille!

Jos kohtaat tehtävässä ongelmia, katso visualisaattorilla mitä koodisi tekee.

[Vastaus](osa05-15_sanakirjan_kaanto/src)

## Luvut sanoina
Kirjoita funktio lukukirja(), joka palauttaa uuden sanakirjan. Palautettu rakenne sisältää avaimina luvut nollasta 99:ään. Sanakirjan arvoina ovat luvut kirjaimin kirjoitettuna. Katso esimerkkiä alla:
```python
luvut = lukukirja()
print(luvut[2])
print(luvut[11])
print(luvut[45])
print(luvut[99])
print(luvut[0])
```
```
kaksi
yksitoista
neljäkymmentäviisi
yhdensänkymmentäyhdeksän
nolla
```
HUOM! Älä muodosta jokaista lukusanaa yksitellen, vaan mieti, miten voisit hyödyntää silmukoita ja sanakirjaa jotenkin ratkaisussasi!

[Vastaus](osa05-16_luvut_sanoina/src)

## Elokuvarekisteri
Kirjoita funktio lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int), joka lisää yhden elokuvaolion elokuvarekisteriin.

Rekisteri on toteutettu listana, ja jokainen listan alkio on yksi sanakirja. Sanakirjassa on seuraavat avaimet:

- nimi
- ohjaaja
- vuosi
- pituus
  
Arvot tulevat metodin parametreina.

Esimerkki:
```python
rekisteri = []
lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
lisaa_elokuva(rekisteri, "Python lentokoneessa", "Renny Pytholin", 2001, 94)
print(rekisteri)
```
```
[{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116}, {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pytholin", "vuosi": 2001, "pituus": 94}]
```

[Vastaus](osa05-17_elokuvarekisteri/src)

## Etsi elokuvat
Kirjoita funktio etsi_elokuvat(rekisteri: list, hakusana: str), joka käsittelee edellisessä tehtävässä luotua elokuvarekisteriä. Funktio muodostaa uuden listan, jolle kopioidaan rekisteristä ne elokuvat, joiden nimestä löytyy hakusana. Pienet ja isot kirjaimet eivät merkitse haussa, joten hakusanalla paj pitää löytyä sekä elokuva Tappajahai että elokuva Pajatoiminnan historia.

Esimerkki:
```python
rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
{"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
{"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

lista = etsi_elokuvat(rekisteri, "python")
print(lista)
```
```
[{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116}, {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94}]
```

[Vastaus](osa05-17b_etsi_elokuvat/src)

## Muodosta tuple
Tee funktio tee_tuple(x: int, y: int, z: int), joka muodostaa ja palauttaa parametrinaan saamistaan kokonaisluvuista tuplen seuraavien sääntöjen mukaaan:

1. Tuplen ensimmäinen alkio on parametreista pienin
2. Tuplen toinen alkio on parametreista suurin
3. Tuplen kolmas alkio on parametrien summa

Esimerkki funktion kutsumisesta:
```python
if __name__ == "__main__":
    print(tee_tuple(5, 3, -1))
```
```
(-1, 5, 7)
```

[Vastaus](osa05-17c_muodosta_tuple/src)

## Vanhin henkilöistä
Tee funktio vanhin(henkilot: list), joka saa parametrikseen listan henkilöitä esittäviä tupleja. Funktio etsii ja palauttaa vanhimman henkilön nimen.

Henkilötuplessa on ensin henkilön nimi merkkijonona ja toisena alkiona henkilön syntymävuosi.

Esimerkiksi:
```python
h1 = ("Arto", 1977)
h2 = ("Einari", 1985)
h3 = ("Maija", 1953)
h4 = ("Essi", 1997)
hlista = [h1, h2, h3, h4]

print(vanhin(hlista))
```
```
Maija
```

[Vastaus](osa05-18_vanhin_henkiloista/src)

## Vanhemmat henkilöt
Oletetaan, että meillä on edelleen käytössä edellisessä tehtävässä esitellyt henkilö-tuplet.

Kirjoita funktio vanhemmat(henkilot: list, vuosi: int), joka palauttaa uuden listan, jolle on tallennettu kaikki ennen annettua vuotta syntyneet henkilöiden nimet parametrina saadulta henkilöiden listalta.

Esimerkiksi:
```python
h1 = ("Arto", 1977)
h2 = ("Einari", 1985)
h3 = ("Maija", 1953)
h4 = ("Essi", 1997)
hlista = [h1, h2, h3, h4]

vanhemmat_henkilot = vanhemmat(hlista, 1979)
print(vanhemmat_henkilot)
```
```
[ 'Arto', Maija' ]
```

[Vastaus](osa05-19_vanhemmat_henkilot/src)

## Opiskelijarekisteri
Tässä tehtäväsarjassa toteutetaan yksinkertainen opiskelijarekisteri. Ennen ohjelmoinnin aloittamista kannattanee hetki miettiä, minkälaisen tietorakenteen tarvitset ohjelman tallentamien tietojen organisointiin.

### Osa 1: opiskelijoiden lisäys
Toteuta ensin funktio lisaa_opiskelija uuden opiskelijan lisäämiseen sekä ensimmäinen versio funktiosta tulosta, joka tulostaa yhden opiskelijan tiedot.

Funktioita käytetään seuraavasti:
```python
opiskelijat = {}
lisaa_opiskelija(opiskelijat, "Pekka")
lisaa_opiskelija(opiskelijat, "Liisa")
tulosta(opiskelijat, "Pekka")
tulosta(opiskelijat, "Liisa")
tulosta(opiskelijat, "Jukka")
```
Ohjelma tulostaa tässä vaiheessa
```
Pekka:
 ei suorituksia
Liisa:
 ei suorituksia
ei löytynyt ketään nimellä Jukka
```
### Osa 2: suoritusten lisäys
Tee funktio lisaa_suoritus, jonka avulla opiskelijalle voidaan lisätä kurssin suoritus. Suoritus on tuple, joka koostuu kurssin nimestä ja arvosanasta:
```python
opiskelijat = {}
lisaa_opiskelija(opiskelijat, "Pekka")
lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
tulosta(opiskelijat, "Pekka")
```
Opiskelijan tietojen tulostus muuttuu, kun suorituksia on lisätty:
```
Pekka:
 suorituksia 2 kurssilta:
  Ohpe 3
  Tira 2
 keskiarvo 2.5
```
### Osa 3: arvosanojen korotus
Suorituksen lisäämisen pitää toimia siten, että se jättää arvosanan 0 suoritukset huomiotta eikä alenna kurssilla ennestään olevaa arvosanaa:
```python
opiskelijat = {}
lisaa_opiskelija(opiskelijat, "Pekka")
lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 2))
tulosta(opiskelijat, "Pekka")
```
```
Pekka:
 suorituksia 2 kurssilta:
  Ohpe 3
  Tira 2
 keskiarvo 2.5
```
### Osa 4: kooste opiskelijoista
Tee funktio kooste, joka tulostaa koosteen opiskelijoiden suorituksista. Esimerkki:
```python
opiskelijat = {}
lisaa_opiskelija(opiskelijat, "Pekka")
lisaa_opiskelija(opiskelijat, "Liisa")
lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
kooste(opiskelijat)
```
tulostus näyttää seuraavalta
```
opiskelijoita 2
eniten suorituksia 3 Pekka
paras keskiarvo 4.5 Liisa
```

[Vastaus](osa05-20_opiskelijarekisteri/src)

## Kirjainruudukko
Tämän osan huipentaa suhteellisen haastava ongelmanratkaisua vaativa tehtävä, jonka voi ratkaista monella eri tavalla. Vaikka tehtävä on tupleja käsittelevässä luvussa, tupleja tässä tuskin kannattaa käyttää.

Tee ohjelma, joka tulostaa kirjainruudukon oheisten esimerkkien mukaisesti. Voit olettaa, että kerroksia on enintään 26.
```
Kerrokset: 3
CCCCC
CBBBC
CBABC
CBBBC
CCCCC
```
```
Kerrokset: 4
DDDDDDD
DCCCCCD
DCBBBCD
DCBABCD
DCBBBCD
DCCCCCD
DDDDDDD
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa05-21_kirjainruudukko/src)


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

## 


[Vastaus](osa03-11_alleviivaus/src)

## 


[Vastaus](osa03-12_tasaus_oikeaan/src)

## 


[Vastaus](osa03-13_sanalaatikko/src)

## 


[Vastaus](osa03-07_osajonot1/src)

## 


[Vastaus](osa03-08_osajonot2/src)

## 


[Vastaus](osa03-13b_loytyvatko_vokaalit/src)

## 


[Vastaus](osa03-13c_osajonon_haku/src)

## 


[Vastaus](osa03-14_osajonojen_haku/src)

## 

[Vastaus](osa03-15_toinen_esiintyma/src)

## 


[Vastaus](osa03-15b_kertotaulut/src)

## 


[Vastaus](osa03-16_sanojen_ensimmaiset_kirjaimet/src)

## 


[Vastaus](osa03-17_kertomat/src)

## 


[Vastaus](osa03-18_parit_ympari/src)

## 


[Vastaus](osa03-19_vuorotellen/src)

## 

[Vastaus](osa03-21_seitseman_veljesta/src)

## 


[Vastaus](osa03-22_ensimmainen_merkki/src)

## 


[Vastaus](osa03-25_keskiarvo/src)

## 


[Vastaus](osa03-24_monta_tulostusta/src)

## 


[Vastaus](osa03-23_risunelio/src)

## 


[Vastaus](osa03-26_shakkilauta/src)

## 


[Vastaus](osa03-27_sananelio/src)


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

## 


[Vastaus](osa03-05a_monistetut_jonot/src)

## 


[Vastaus](osa03-05b_pidempi_jono/src)

## 


[Vastaus](osa03-05c_lopusta_alkuun/src)

## 


[Vastaus](osa03-06_toinen_ja_toiseksi_viimeinen/src)

## 


[Vastaus](osa03-09_risuaitaviiva/src)

## 


[Vastaus](osa03-10_risuaitanelio/src)

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


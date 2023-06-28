# Osa 3 - Tehtävien vastaukset
## Tulosta luvut
Kirjoita ohjelma, joka tulostaa silmukassa luvut kahdesta kolmeenkymmeneen kahden luvun välein. Jokainen luku tulostetaan omalle rivilleen.

Ohjelman tulosteen alku näytää siis tältä:
```

2
4
6
8
jne...
```

[Vastaus](osa03-00_tulosta_luvut/src)

## Lähtölaskenta
Korjaa tehtäväpohjassa oleva ohjelma
```python
print("Valmiina?")
luku = int(input("Anna luku: "))
while luku = 0:
print(luku)
print("Nyt!")
```
siten että se toimii seuraavasti:
```
Valmiina?
Anna luku: 5
5
4
3
2
1
Nyt!
```

Älä tällä kertaa käytä while True -silmukkaa!

[Vastaus](osa03-01_lahtolaskenta/src)

## Luvut
Tee ohjelma, joka tulostaa kaikki käyttäjän antamaa lukua pienemmät luvut alkaen luvusta yksi.
```
Mihin asti: 5
1
2
3
4
```

Älä käytä tässä tehtävässä while-komennon ehtona arvoa True!

[Vastaus](osa03-02_luvut/src)

## Kahden potenssit
Tee ohjelma, joka tulostaa ensin luvun 1 ja sen jälkeen kerta toisensa jälkeen aina kaksi kertaa suuremman luvun. Ohjelma siis tulostaa luvun kaksi potensseja.

Ohjelman suoritus päättyy, kun on tulostettu luku, joka on korkeintaan käyttäjän syötteen suuruinen. Yhtään käyttäjän syötettä suurempaa lukua ei siis tulosteta!
```
Mihin asti: 8
1
2
4
8
```
```
Mihin asti: 20
1
2
4
8
16
```
```
Mihin asti: 100
1
2
4
8
16
32
64
```
Älä käytä tässä tehtävässä while-komennon ehtona arvoa True!

Miten kahden potenssit lasketaan? Ensimmäinen kahden potenssi on luku 1. Seuraava saadaan kertomalla 1 luvulla 2, eli se on 2. Sitä seuraava saadaan taas kertomalla edellinen kahden potenssi kahdella, eli kyseessä on 2 * 2 eli 4, ja seuraava saadaan kertomalla kahdella 4 * 2 eli kyseessä on 8, jne...

[Vastaus](osa03-03_kahden_potenssit/src)

## Luvun n potenssit
Muuta edellistä ohjelmaa siten, että käyttäjä saa määrätä kertoimen (edellisessä ohjelmassa kerroin oli aina 2), eli sen, minkä luvun potensseja ohjelma tulostaa.
```
Mihin asti: 27
Mikä kerroin: 3
1
3
9
27
```
```
Mihin asti: 1234567
Mikä kerroin: 10
1
10
100
1000
10000
100000
1000000
```
Älä käytä tässä tehtävässä while-komennon ehtona arvoa True!

[Vastaus](osa03-04_luvun_n_potenssit/src)

## Peräkkäisten summa, versio 1
Tee ohjelma, joka laskee peräkkäisten lukujen summaa 1 + 2 + 3 + ... kunnes sen arvo on vähintään käyttäjän syöttämä luku. Ohjelma toimii seuraavasti:
```
Mihin asti: 2
3
```
```
Mihin asti: 10
10
```
```
Mihin asti: 18
21
```
Voit olettaa, että käyttäjän antama luku on 2 tai suurempi.

[Vastaus](osa03-04a_perakkaisten_summa_helpompi/src)

## Peräkkäisten summa, versio 2
Tee edellisestä ohjelmasta hieman kehittyneempi versio, joka tulostaa lopputuloksen lisäksi myös sen miten kyseinen summa lasketaan:
```
Mihin asti: 2
Laskettiin 1 + 2 = 3
```
```
Mihin asti: 10
Laskettiin 1 + 2 + 3 + 4 = 10
```
```
Mihin asti: 18
Laskettiin 1 + 2 + 3 + 4 + 5 + 6 = 21
```
Voit olettaa, että käyttäjän antama luku on 2 tai suurempi.

[Vastaus](osa03-05_perakkaisten_summa/src)

## Monta jonoa


[Vastaus](osa03-05a_monistetut_jonot/src)

## Pidempi jono


[Vastaus](osa03-05b_pidempi_jono/src)

## Lopusta alkuun


[Vastaus](osa03-05c_lopusta_alkuun/src)

## Toinen ja toiseksi viimeinen


[Vastaus](osa03-06_toinen_ja_toiseksi_viimeinen/src)

## Risuaitaviiva


[Vastaus](osa03-09_risuaitaviiva/src)

## Risuaitasuorakulmio


[Vastaus](osa03-10_risuaitanelio/src)

## Alleviivaus


[Vastaus](osa03-11_alleviivaus/src)

## Tasaus oikeaan


[Vastaus](osa03-12_tasaus_oikeaan/src)

## Sanalaatikko


[Vastaus](osa03-13_sanalaatikko/src)

## Osajonot 1


[Vastaus](osa03-07_osajonot1/src)

## Osajonot 2


[Vastaus](osa03-08_osajonot2/src)

## Löytyvätkö vokaalit


[Vastaus](osa03-13b_loytyvatko_vokaalit/src)

## Ensimmäisen osajonon haku


[Vastaus](osa03-13c_osajonon_haku/src)

## Kaikkien osajonojen haku


[Vastaus](osa03-14_osajonojen_haku/src)

## Toinen esiintymä


[Vastaus](osa03-15_toinen_esiintyma/src)


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

## 


[Vastaus](osa02-08_ian_tarkistus/src)

## 


[Vastaus](osa02-09_veljenpojat/src)

## 


[Vastaus](osa02-10_arvosana_ja_pisteet/src)

## 


[Vastaus](osa02-11_fizzbuzz/src)

## 


[Vastaus](osa02-12_karkausvuosi/src)

## 


[Vastaus](osa02-13_aakkosjarjestyksessa_keskimmainen/src)

## 


[Vastaus](osa02-14_lahjaverolaskuri/src)

## 


[Vastaus](osa02-15_jatketaanko/src)

## 


[Vastaus](osa02-16_syotteen_rajaus/src)

## 


[Vastaus](osa02-17_lahtolaskenta/src)

## 


[Vastaus](osa02-18_salasana_uudelleen/src)

## 


[Vastaus](osa02-19_pin_ja_yritysten_maara/src)

## 


[Vastaus](osa02-20_seuraava_karkausvuosi/src)

## 


[Vastaus](osa02-21_tarina/src)

## 


[Vastaus](osa02-22_lukujen_kasittelya/src)


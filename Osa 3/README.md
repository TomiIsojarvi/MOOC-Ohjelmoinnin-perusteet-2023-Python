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
Kirjoita ohjelma, joka kysyy käyttäjältä merkkijonon ja määrän ja tulostaa sitten annettua merkkijonoa annetun määrän. Tulostuksen tulee tapahtua yhdelle riville yhteen pötköön.

Esimerkkisuoritus:
```
Anna merkkijono: heippa
Anna määrä: 4
heippaheippaheippaheippa
```

[Vastaus](osa03-05a_monistetut_jonot/src)

## Pidempi jono
Kirjoita ohjelma, joka kysyy käyttäjältä kaksi merkkijonoa ja tulostaa jonoista pidemmän (ts. sen, jossa on enemmän merkkejä). Jos jonot ovat yhtä pitkiä tulostetaan viesti "Jonot ovat yhtä pitkät"

Esimerkkisuorituksia:
```
Anna jono 1: moi
Anna jono 2: heippa
heippa on pidempi
```
```
Anna jono 1: moikkelis koikkelis
Anna jono 2: heipparallaa
moikkelis koikkelis on pidempi
```
```
Anna jono 1: moi
Anna jono 2: hei
Jonot ovat yhtä pitkät
```

[Vastaus](osa03-05b_pidempi_jono/src)

## Lopusta alkuun
Kirjoita ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten merkkijonon merkit allekkain käänteisessä järjestyksessä lopusta alkuun.

Esimerkkisuoritus:
```
Anna merkkijono: heippa
a
p
p
i
e
h
```

[Vastaus](osa03-05c_lopusta_alkuun/src)

## Toinen ja toiseksi viimeinen
Tee ohjelma, joka kysyy käyttäjältä sanan ja kertoo, ovatko sen toinen ja toiseksi viimeinen merkki samoja.
```
Anna sana: python
Toinen ja toiseksi viimeinen kirjain eroavat
```
```
Anna sana: pascal
Toinen ja toiseksi viimeinen kirjain on a
```

[Vastaus](osa03-06_toinen_ja_toiseksi_viimeinen/src)

## Risuaitaviiva
Tee ohjelma, joka piirtää käyttäjän määräämän levyisen risuaitaviivan.
```
Leveys: 3

###
```
```
Leveys: 8

########
```

[Vastaus](osa03-09_risuaitaviiva/src)

## Risuaitasuorakulmio
Laajenna edellistä niin, että käyttäjä syöttää myös piirrettävien rivien määrän
```
Leveys: 10
Korkeus: 3
##########
##########
##########
```

[Vastaus](osa03-10_risuaitanelio/src)

## Alleviivaus
Tee ohjelma, joka pyytää käyttäjältä merkkijonoja ja tulostaa kunkin merkkijonon oheisen esimerkin mukaisesti alleviivattuna. Ohjelman suoritus päättyy, kun käyttäjä syöttää tyhjän merkkijonon, eli merkkijonon jonka pituus on 0.
```
Anna merkkijono: Moi kaikki!

Moi kaikki!
-----------
Anna merkkijono: Tämä on testijono

Tämä on testijono
-----------------
Anna merkkijono: a

a
-
Anna merkkijono:
```

[Vastaus](osa03-11_alleviivaus/src)

## Tasaus oikeaan
Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sen niin, että tulostetuksi tulee tasan 20 merkkiä. Jos merkkijono on lyhyempi, alkuun tulee tarvittava määrä tähtiä *.

Voit olettaa, että syötetyssä merkkijonossa on enintään 20 merkkiä.
```
Sana: python

**************python
```
```
Sana: pitkämerkkijono

*****pitkämerkkijono
```
```
Sana: tosipitkämerkkijono

*tosipitkämerkkijono
```

[Vastaus](osa03-12_tasaus_oikeaan/src)

## Sanalaatikko
Tee ohjelma, joka kysyy käyttäjältä sanaa ja tulostaa sanan tähtiraameihin, joissa sana on keskellä. Raamien leveys on 30 merkkiä, ja voit olettaa, että sana mahtuu raameihin.

Huom! Jos sanan pituus on pariton, voit tulostaa sanan kumpaan tahansa mahdollisista keskikohdista.
```
Sana: koe

******************************
*            koe             *
******************************
```
```
Sana: python

******************************
*           python           *
******************************
```

[Vastaus](osa03-13_sanalaatikko/src)

## Osajonot 1
Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten kaikki sen ensimmäisestä merkistä alkavat osajonot pituusjärjestyksessä.

Esimerkkitulostus:
```
Anna merkkijono: testi
t
te
tes
test
testi
```

[Vastaus](osa03-07_osajonot1/src)

## Osajonot 2
Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten kaikki sen viimeiseen merkkiin päättyvät osajonot pituusjärjestyksessä.

Esimerkkitulostus:
```
Anna merkkijono: testi
i
ti
sti
esti
testi
```

[Vastaus](osa03-08_osajonot2/src)

## Löytyvätkö vokaalit
Tee ohjelma, joka kysyy käyttäjältä merkkijonon ja tulostaa sitten tiedon löytyvätkö vokaalit a, e ja o merkkijonosta.

Voit olettaa, että merkkijono on syötetty kokonaan pienillä kirjaimilla. Katso mallia esimerkkitulostuksesta.

Esimerkkitulostus:
```
Anna merkkijono: heippa sulle
a löytyy
e löytyy
o ei löydy
```
```
Anna merkkijono: moi
a ei löydy
e ei löydy
o löytyy
```

[Vastaus](osa03-13b_loytyvatko_vokaalit/src)

## Ensimmäisen osajonon haku
Tee ohjelma, joka kysyy käyttäjältä merkkijonoa ja yksittäistä merkkiä. Ohjelma tulostaa merkkijonosta löytyvän ensimmäisen kolmen merkin pituisen osajonon, jonka alkukirjain on käyttäjän syöttämä merkki. Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen.
```
Sana: apinatalo
Merkki: a
api
```
```
Sana: banaani
Merkki: n
naa
```
```
Sana: tomaatti
Merkki: x
```
```
Sana: python
Merkki: n
```

[Vastaus](osa03-13c_osajonon_haku/src)

## Kaikkien osajonojen haku
Tee edellisestä ohjelmasta laajennettu versio, joka tulostaa kaikki merkkijonon sisältämät kolmen merkin pituiset osajonot, joiden alkukirjain on käyttäjän syöttämä merkki. Voit olettaa, että merkkijono on vähintään kolmen merkin pituinen.
```
Sana: apinatalo
Merkki: a
api
ata
alo
```
```
Sana: banaani
Merkki: n
naa
```
Vihje seuraava esimerkki saattaa antaa jotain inspiraatiota eräästä tavasta miten tätä tehtävää voi lähestyä
```python
sana = input("Sana: ")
while True:
    if len(sana) == 0:
        break
    print(sana)
    sana = sana[2:]
```
```
Sana: apinatalo
apinatalo
inatalo
atalo
alo
o
```

[Vastaus](osa03-14_osajonojen_haku/src)

## Toinen esiintymä
Tee ohjelma, joka etsii merkkijonosta osajonon toisen esiintymän. Jos toista (tai edes ensimmäistä) esiintymää ei löydy, ohjelma tulostaa tästä tiedon.

Määritellään tässä yhteydessä, että esiintymät eivät voi mennä päällekkäin, merkkijonossa aaaa osajonon aa toinen esiintymä löytyy siis indeksin 2 kohdalta.

Muutama esimerkkisuoritus:
```
Anna merkkijono: abcabc
Anna osajono: ab
Osajonon toinen esiintymä on kohdassa 3.
```
```
Anna merkkijono: saippuakauppias
Anna osajono: a
Osajonon toinen esiintymä on kohdassa 6.
```
```
Anna merkkijono: aybabtu
Anna osajono: ba
Osajono ei esiinny merkkijonossa kahdesti.
```

[Vastaus](osa03-15_toinen_esiintyma/src)

## Kertotaulut
Tee ohjelma, joka kysyy käyttäjältä positiivisen kokonaisluvun. Ohjelma tulostaa esimerkkitulostuksen mukaisesti kertolaskuja lukuun asti:

Esimerkkisuorituksia:
```
Anna luku: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4
```
```
Anna luku: 3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

[Vastaus](osa03-15b_kertotaulut/src)

## Sanojen ensimmäiset kirjaimet
Tee ohjelma, joka kysyy käyttäjältä lauseen. Ohjelma tulostaa jokaisen sanan ensimmäisen kirjaimen ruudulle omille riveilleen.

Esimerkkisuoritus:
```
Anna lause: Vesihiisi sihisi hississä
V
s
h
```

[Vastaus](osa03-16_sanojen_ensimmaiset_kirjaimet/src)

## Kertomat
Tee ohjelma, joka kysyy käyttäjältä kokonaisluvun. Jos käyttäjä syöttää negatiivisen luvun tai nollan, ohjelman suoritus päättyy. Muuten ohjelma tulostaa luvun kertoman.

Kertoma lasketaan kertomalla keskenään luku ja kaikki sitä pienemmät positiiviset kokonaisluvut. Esim. luvun 5 kertoma on 1 * 2 * 3 * 4 * 5 = 120.

Esimerkkisuorituksia:
```
Anna luku: 3
Luvun 3 kertoma on 6
Anna luku: 4
Luvun 4 kertoma on 24
Anna luku: -1
Kiitos ja moi!
```
```
Anna luku: 1
Luvun 1 kertoma on 1
Anna luku: 0
Kiitos ja moi!
```

[Vastaus](osa03-17_kertomat/src)

## Parit ympäri
Tee ohjelma, joka tulostaa luvut 1:stä käyttäjän antamaan lukuun. Luvut on kuitenkin käännetty pareittain ympäri.
```
Anna luku: 5
2
1
4
3
5
```
```
Anna luku: 6
2
1
4
3
6
5
```

[Vastaus](osa03-18_parit_ympari/src)

## Vuorotellen
Tee ohjelma, joka kysyy käyttäjältä luvun ja tulostaa sitten lukuja vuorotellen seuraavien esimerkkien mukaisesti.
```
Anna luku: 5
1
5
2
4
3
```
```
Anna luku: 6
1
6
2
5
3
4
```

[Vastaus](osa03-19_vuorotellen/src)

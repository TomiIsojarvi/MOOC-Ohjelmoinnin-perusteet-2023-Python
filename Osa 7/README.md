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

```

[Vastaus](osa03-26_shakkilauta/src)

## 


[Vastaus](osa03-27_sananelio/src)


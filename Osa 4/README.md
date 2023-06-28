# Osa 4 - Tehtävien vastaukset
## Hello Visual Studio Code
Tee ohjelma, joka kysyy käyttäjältä, mikä editori on käytössä. Ohjelma jatkaa, kunnes vastaus on Visual Studio Code.

Seuraava käyttöesimerkki havainnollistaa ohjelman haluttua tulostusta:
```
Editori: Emacs
ei ole hyvä
Editori: Vim
ei ole hyvä
Editori: Word
surkea
Editori: Atom
ei ole hyvä
Editori: Visual Studio Code
loistava valinta!
```
Jos käyttäjä kirjoittaa Word tai Notepad, ohjelma vastaa surkea. Muissa epäkelvoissa tapauksissa vastaus on ei ole hyvä.

Ohjelman tulee toimia siten, että "oikean vastauksen" kirjoitusasu ei riipu siitä, kirjoitetaanko vastaus isoja vai pieniä kirjaimia käyttämällä:
```
Editori: NOTEPAD
surkea
Editori: viSUal STudiO cODe
loistava valinta!
```

Kirjainten koon voi jättää huomiotta esim. muuttamalla kirjaimet pieniksi merkkijonojen metodilla lower, jota voi käyttää seuraavasti:
```python
mjono = "Visual Studio CODE"
if "visual studio code" == mjono.lower():
    print("merkkijono oli etsitty!")
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!


[Vastaus](osa04-01_hello_visualstudio_code/src)

## Viiva
Tee funktio viiva, joka saa kaksi parametria (leveys, merkkijono). Funktio tulostaa ensimmäisen parametrin määrittämän pituisen viivan käyttäen toisena parametrina olevan merkkijonon ensimmäistä merkkiä. Jos parametrina oleva merkkijono on tyhjä, tulostuu viiva tähtinä.
```

viiva(7, "%")
viiva(10, "LOL")
viiva(3, "")
```
```
%%%%%%%
LLLLLLLLLL
***
```

[Vastaus](osa04-02_viiva/src)

## Risulaatikko
Tee funktio risulaatikko, joka piirtää risuaitamerkkiä käyttäen parametrinsa korkuisen, kymmenen merkkiä leveän risulaatikon.

Funktion tulee kutsua edellisen tehtävän funktiota viiva kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion koodi tämän tehtävän funktion koodin yläpuolelle. Älä muuta funktiota mitenkaan!

Pari käyttöesimerkkiä
```python
risulaatikko(5)
print()
risulaatikko(2)
```
```
##########
##########
##########
##########
##########

##########
##########
```

[Vastaus](osa04-02a_risulaatikko/src)

## Risuneliö
Tee funktio risunelio, joka piirtää risuaitamerkkiä käyttäen parametrinsa kokoisen risuneliön.

Funktion tulee kutsua edellisen tehtävän funktiota viiva kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion koodi tämän tehtävän funktion koodin yläpuolelle. Älä muuta funktiota mitenkaan!

Pari käyttöesimerkkiä
```python
risunelio(5)
print()
risunelio(3)
```
```
#####
#####
#####
#####
#####

###
###
###
```

[Vastaus](osa04-02b_risunelio/src)

## Neliö
Tee funktio nelio, joka saa kaksi parametria. Funktio tulostaa neliön jonka korkeuden ja leveyden kertoo ensimmäinen parametri. Toinen parametri määrittelee mitä merkkiä käyttäen neliö piirretään.

Funktion tulee kutsua edellisen tehtävän funktiota viiva kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion koodi tämän tehtävän funktion koodin yläpuolelle. Älä muuta funktiota mitenkaan!

Pari käyttöesimerkkiä
```python
nelio(5, "*")
print()
nelio(3, "o")
```
```
*****
*****
*****
*****
*****

ooo
ooo
ooo
```

[Vastaus](osa04-02c_nelio/src)

## Kolmio
Tee funktio kolmio, joka piirtää risuaitamerkkiä käyttäen parametrinsa korkuisen ja levyisen, risuaitakolmion.

Funktion tulee kutsua edellisen tehtävän funktiota viiva kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion koodi tämän tehtävän funktion koodin yläpuolelle. Älä muuta funktiota mitenkaan!

Pari käyttöesimerkkiä
```python
kolmio(6)
print()
kolmio(3)
```
```
#
##
###
####
#####
######

#
##
###
```

[Vastaus](osa04-02d_kolmio/src)

## Kuvio
Tee funktio kuvio, joka saa neljä parametria. Funktio tulostaa kuvion, jonka yläosana on kahden ensimmäisen parametrin määrittelemä kolmio ja alaosana ensimmäisen ja kahden jälkimmäisen parametrin määrittelemä suorakulmio.

Funktion tulee kutsua edellisen tehtävän funktiota viiva kaiken tulostuksen tekemiseen! Kopioi edellisen tehtävän funktion koodi tämän tehtävän funktion koodin yläpuolelle.

Pari käyttöesimerkkiä
```python
kuvio(5, "X", 3, "*")
print()
kuvio(2, "o", 4, "+")
print()
kuvio(3, ".", 0, ",")
```
```
X
XX
XXX
XXXX
XXXXX
*****
*****
*****

o
oo
++
++
++
++

.
..
...
```
Vihje

Älä yritä ratkaista tehtävässä "kaikkia asioita" yhtä aikaa. Keskity ensin esim. siihen että saat kuvion yläosan kolmion piirtymään oikein, ja vasta sen jälkeen jatka kuvion täydentämistä alaosan suorakulmiolla.

Tämä on ylipäätänsäkin ohjelmoinnissa erittäin tärkeää: keskity pieniin osiin kerrallaan, varmista että ne toimivat ennen kuin laajennat ratkaisuasi.

[Vastaus](osa04-03_kuvio/src)

## Joulukuusi
Tee funktio joulukuusi, joka saa yhden parametrin. Funktio tulostaa tekstin joulukuusi! ja parametrinsa kokoisen joulukuusen.

Esim. kutsuttaessa joulukuusi(3) tulostuu
```
joulukuusi!
  *
 ***
*****
  *
```
Esim. kutsuttaessa joulukuusi(5) tulostuu
```
joulukuusi!
    *
   ***
  *****
 *******
*********
    *
```
Huomaa, että joulukuusen vasemmalla puolella pitää olla täsmälleen oikea määrä välilyöntejä. Eli vaikka kuusen muoto olisi täysin oikea, mutta sen alin "neulastaso" ei lähde ruudun vasemmasta reunasta, ei vastaus kelpaa testeille.

[Vastaus](osa04-04_joulukuusi/src)

## Luvuista suurin
Tee funktio luvuista_suurin, joka saa parametriksi kolme kokonaislukua. Funktio palauttaa return-lausetta käyttäen luvuista suurimman.

Käyttöesimerkki
```python
print(luvuista_suurin(3, 4, 1)) # 4
print(luvuista_suurin(99, -4, 7)) # 99
print(luvuista_suurin(0, 0, 0)) # 0
```

[Vastaus](osa04-05_luvuista_suurin/src)

## Merkit samat
Tee funktio samat, joka saa parametriksi merkkijonon ja kaksi merkkijonon indeksejä kuvaavaa kokonaislukua. Funktio palauttaa return-lausetta käyttäen tiedon (True tai False) siitä, ovatko merkkijonon parametreina olevien indeksien osoittamissa paikoissa olevat merkit samat. Jos jompikumpi indekseistä ei osu merkkijonon sisälle, palauttaa metodi False.

Muutama esimerkki:
```python
# samat merkit o ja o
print(samat("koodari", 1, 2)) # True

# eri merkit k ja a
print(samat("koodari", 0, 4)) # False

# toinen indeksi ei ole merkkijonon sisällä
print(samat("koodari", 0, 10)) # False
```

[Vastaus](osa04-06_merkit_samat/src)

## Eka, toka ja vika sana
Tee kolme funktiota: eka_sana, toka_sana ja vika_sana. Jokainen funktioista saa parametrikseen lauseen (eli merkkijonon).

Funktiot palauttavat nimensä mukaisesti lauseen ensimmäisen, toisen tai viimeisen sanan.

Voit olettaa jokaisessa tapauksessa, että merkkijono koostuu vähintään kahdesta sanasta, ja että sanojen välillä on aina täsmälleen yksi välilyönti, ja että merkkijonon alussa ja lopussa ei ole välilyöntejä.
```python
lause = "olipa kerran kauan sitten ohjelmoija"

print(eka_sana(lause)) # olipa
print(toka_sana(lause)) # kerran
print(vika_sana(lause)) # ohjelmoija
```
```
olipa
kerran
ohjelmoija
```
```python
lause = "olipa kerran"

print(toka_sana(lause)) # kerran
print(vika_sana(lause)) # kerran
```

[Vastaus](osa04-07_eka_toka_vika_sana/src)

## Alkioiden arvojen muutokset
Tee ohjelma, joka alustaa listan jossa on arvot [1, 2, 3, 4, 5]. Tämän jälkeen ohjelma kysyy käyttäjältä alkion indeksin ja uuden arvon, vaihtaa kyseisen alkion arvon ja tulostaa listan uudelleen. Ohjelman suoritus päättyy, jos käyttäjä antaa alkion indeksiksi -1.

Esimerkkisuoritus:
```
Anna indeksi: 0
Anna arvo: 10
[10, 2, 3, 4, 5]
Anna indeksi: 2
Anna arvo: 250
[10, 2, 250, 4, 5]
Anna indeksi: 4
Anna arvo: -45
[10, 2, 250, 4, -45]
Anna indeksi: -1
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa04-07a_alkioiden_arvojen_muutokset/src)

## Alkioiden lisäys listaan
Tee ohjelma, joka kysyy käyttäjältä ensin lukujen määrän. Sen jälkeen ohjelma pyytää käyttäjää syöttämään annetun määrän lukuja yksitellen ja lisää ne listaan samassa järjestyksessä.

Lopuksi lista tulostetaan.

Esimerkkisuoritus:
```
Kuinka monta lukua: 3
Anna luku 1: 10
Anna luku 2: 250
Anna luku 3: 34
[10, 250, 34]
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa04-07b_alkoiden_lisays_listaan/src)

## Lisäys ja poisto
Tee ohjelma, joka pyytää käyttäjää valitsemaan alkion lisäyksen tai poiston. Sekä lisäys että poisto tehdään listan loppuun. Lisättävän alkion arvo on aina yhtä suurempi kuin listan viimeinen alkio (tai 1, jos listassa ei ole alkioita).

Joka operaation välissä lista tulostetaan. Katso esimerkkiä seuraavasta tulosteesta:
```
Lista on nyt []
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1]
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1, 2]
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1, 2, 3]
(l)isää, (p)oista vai e(x)it: p
Lista on nyt [1, 2]
(l)isää, (p)oista vai e(x)it: l
Lista on nyt [1, 2, 3]
(l)isää, (p)oista vai e(x)it: x
Moi!
```
Voit olettaa, että listalta ei yritetä poistaa alkioita, jos lista on tyhjä.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa04-07c_lisays_ja_poisto/src)

## Sama sana kahdesti
Tee ohjelma, joka kyselee käyttäjältä sanoja. Kun käyttäjä syöttää jonkin sanan kahdesti, ohjelma tulostaa eri sanojen määrän ja lopettaa toimintansa.
```
sana: olipa
sana: kerran
sana: kauan
sana: sitten
sana: kerran
Annoit 4 eri sanaa
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa04-08_sama_sana_kahdesti/src)

## Lista kahdesti
Tee ohjelma, joka kysyy käyttäjältä lukuja ja lisää niitä listaan. Lista tulostetaan jokaisen luvun lisäyksen jälkeen kahdella eri tavalla:

- alkiot lisäysjärjestyksessä ja
- järjestettynä pienimmästä suurimpaan alkioon
Ohjelman suoritus päättyy, kun käyttäjä syöttää luvun 0.

Esimerkkisuoritus:
```
Anna luku: 3
Lista: [3]
Järjestettynä: [3]
Anna luku: 1
Lista: [3, 1]
Järjestettynä: [1, 3]
Anna luku: 9
Lista: [3, 1, 9]
Järjestettynä: [1, 3, 9]
Anna luku: 5
Lista: [3, 1, 9, 5]
Järjestettynä: [1, 3, 5, 9]
Anna luku: 0
Moi!
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa04-08b_lista_kahdesti/src)

## Listan pituus
Tee funktio pituus, joka palauttaa parametrinaan saamansa listan pituuden.
```python
lista = [1, 2, 3, 4, 5]
vastaus = pituus(lista)
print("vastaus", vastaus)

# huomaa, että voit kutsua funktiota myös antamalla listan suoraan funktion parametriksi
vastaus = pituus([1, 1, 1, 1])
print("vastaus", vastaus)
```
```
vastaus 5
vastaus 4
```

[Vastaus](osa04-09_listan_pituus/src)

## Keskiarvo
Tee funktio keskiarvo, joka palauttaa parametrinaan saamansa kokonaislukuja sisältävän listan alkioiden keskiarvon.
```python
lista = [1, 2, 3, 4, 5]
vastaus = keskiarvo(lista)
print("vastaus", vastaus)
```
```
vastaus 3.0
```

[Vastaus](osa04-10_keskiarvo/src)

## Vaihteluväli
Tee funktio vaihteluvali, joka palauttaa parametrinaan saamansa kokonaislukuja sisältävän listan vaihteluvälin (eli suurimman ja pienimmän alkion erotuksen).
```python
lista = [1, 2, 3, 4, 5]
vastaus = vaihteluvali(lista)
print("vastaus", vastaus)
```
```
vastaus 4
```

[Vastaus](osa04-11_vaihteluvali/src)

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


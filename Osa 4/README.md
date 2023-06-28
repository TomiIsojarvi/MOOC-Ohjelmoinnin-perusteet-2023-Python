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


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

## Tulostus tähdillä
Tee ohjelma, joka pyytää käyttäjää syöttämään merkkijonon ja tulostaa sitten merkkijonon kirjaimet yksitellen allekkain.

Jokaisen kirjaimen jälkeen tulostetaan lisäksi tähti (*) omalle rivilleen.

Esimerkiksi:
```
Anna merkkijono: Python
P
*
y
*
t
*
h
*
o
*
n
*
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa04-11a_tulostus_tahdilla/src)

## Negatiivisesta positiiviseen
Tee ohjelma, joka lukee käyttäjältä positiivisen kokonaisluvun N. Ohjelma tulostaa sen jälkeen luvut väliltä -N...N nollaa lukuunottamatta. Jokainen luku tulostetaan omalle rivilleen.

Esimerkiksi
```
Anna luku: 4
-4
-3
-2
-1
1
2
3
4
```
Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon!

[Vastaus](osa04-11b_negatiivisesta_positiiviseen/src)

## Tähdet
Tee funktio lista_tahtina, joka saa parametriksi listan kokonaislukuja. Funktio tulostaa joukon tähtirivejä siten, että listalla olevat luvut kertovat kunkin rivin tähtimäärän.

Esim. kutsuttaessa lista_tahtina([3, 7, 1, 1, 2]) tulostus on:
```
***
*******
*
*
**
```

[Vastaus](osa04-12_tahdet/src)

## Anagrammi
Tee funktio anagrammi joka saa parametriksi kaksi merkkijonoa. Funktio palauttaa True, jos merkkijonot ovat anagrammeja eli ne muodostuvat täsmälleen samoista kirjaimista.

Esimerkiksi funktiota voisi käyttää näin:
```python
print(anagrammi("talo", "tola")) # True
print(anagrammi("talo", "lato")) # True
print(anagrammi("talo", "olat")) # True
print(anagrammi("tammi", "mitta")) # False
print(anagrammi("python", "java")) # False
```
Vihje: funktio sorted toimii myös merkkijonoille.

[Vastaus](osa04-13_anagrammi/src)

## Palindromit
Tee funktio palindromi, joka saa parametriksi merkkijonon ja palauttaa True, jos merkkijono on palindromi (eli samansisältöinen luettuna alusta loppuun tai lopusta alkuun).

Tee myös funktiota hyödyntävä pääohjelma, joka kyselee käyttäjältä sanoja niin kauan, kunnes käyttäjä syöttää palindromin:
```
Anna palindromi: python
ei ollut palindromi
Anna palindromi: java
ei ollut palindromi
Anna palindromi: kauppias
ei ollut palindromi
Anna palindromi: saippuakauppias
saippuakauppias on palindromi!
```
Huomaa, että pääohjelmaa ei tule kirjoittaa if __name__ == "__main__":-lohkon sisälle

[Vastaus](osa04-14_palindromit/src)

## Positiivisten summa
Tee funktio positiivisten_summa, joka saa parametriksi kokonaislukuja sisältävän listan.

Funktio palauttaa listan positiivisten lukujen summan.
```python
lista = [1, -2, 3, -4, 5]
vastaus = positiivisten_summa(lista)
print("vastaus", vastaus)
```
```
vastaus 9
```

[Vastaus](osa04-15_positiivisten_summa/src)

## Parilliset
Tee funktio parilliset, joka saa parametriksi kokonaislukuja sisältävän listan.

Funktio palauttaa uuden listan, jolla on parametrina olevan listan sisältämät parilliset luvut.
```python
lista = [1, 2, 3, 4, 5]
uusi_lista = parilliset(lista)
print("alkuperäinen", lista)
print("uusi", uusi_lista)
```
```
alkuperäinen [1, 2, 3, 4, 5]
uusi [2, 4]
```

[Vastaus](osa04-16_parilliset/src)

## Summalista
Tee funktio summa, joka saa parametriksi kaksi kokonaislukuja sisältävää listaa. Molemmissa listoissa on sama määrä alkioita.

Funktio palauttaa uuden listan, jonka alkiot muodostuvat parametreina olevien listojen alkioiden summista.

Esim:
```python
a = [1, 2, 3]
b = [7, 8, 9]
print(summa(a, b)) # [8, 10, 12]
```

[Vastaus](osa04-17_summalista/src)

## Uniikit
Tee funktio uniikit, joka saa parametriksi kokonaislukuja sisältävän listan.

Funktio palauttaa uuden listan, joka sisältää parametrina annetun listan luvut suuruusjärjestyksessä siten, että jokainen luku on listalla vain kerran.
```python
lista = [3, 2, 2, 1, 3, 3, 1]
print(uniikit(lista)) # [1, 2, 3]
```

[Vastaus](osa04-18_uniikit/src)

## Listan pisimmän pituus
Tee funktio pisimman_pituus, joka saa parametriksi listan merkkijonoja. Funktio palauttaa tiedon mikä on listan pisimmän merkkijonon pituus.
```python
lista = ["eka", "toka", "kolmas", "seitsemäs"]

tulos = pisimman_pituus(lista)
print(tulos)
```
```python
lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

tulos = pisimman_pituus(lista)
print(tulos)
```
```
9
6
```

[Vastaus](osa04-18a_listan_pimman_pituus/src)

## Listan lyhin
Tee funktio lyhin, joka saa parametriksi listan merkkijonoja. Funktio palauttaa listan lyhimmän merkkijonon. Jos samanpituisia on useita (testeissä näin ei ole), voi funktio palauttaa niistä minkä vaan. Funktio voi olettaa että listalla ei ole tyhjiä eli nollan pituisia merkkijonoja.
```python
lista = ["eka", "toka", "kolmas", "seitsemäs"]

tulos = lyhin(lista)
print(tulos)
```
```python
lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]

tulos = lyhin(lista)
print(tulos)
```
```
eka
eero
```

[Vastaus](osa04-18b_listan_lyhin/src)

## Listan pisimmät
Tee funktio pisimmat, joka saa parametriksi listan merkkijonoja. Funktio palauttaa listan, joka sisältää parametrina annetun listan pisimmän merkkijonon. Jos pisimpiä merkkijonoja on useampia, funktio palauttaa ne kaikki listassa.

Merkkijonojen järjestyksen tuloslistassa tulee noudattaa merkkijonojen järjestystä alkuperäisessä listassa.
```python
lista = ["eka", "toka", "kolmas", "seitsemäs"]

tulos = pisimmat(lista)
print(tulos) # ['seitsemäs']
```
```python
lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

tulos = pisimmat(lista)
print(tulos) # ['emilia', 'juhani']
```

[Vastaus](osa04-19_listan_pisimmat/src)

## Lukulistasta merkkijonolistaksi
Kirjoita funktio muotoile, joka saa parametrikseen liukulukuja sisältävän listan. Funktio muodostaa listan perusteella uuden merkkijonoja sisältävän listan, jossa jokainen liukulukulistan alkio esitetään pyöristettynä kahden desimaalin tarkkuuteen. Listan alkioiden järjestyksen tulee säilyä.

Vinkki: Käytä liukulukujen muotoiluun merkkijonoiksi f-merkkijonoa.

Esimerkki funktion käytöstä:
```python
lista = [1.234, 0.3333, 0.11111, 3.446]
lista2 = muotoile(lista)
print(lista2)
```
```
['1.23', '0.33', '0.11', '3.45']
```

[Vastaus](osa04-20_lukulistasta_merkkijonolistaksi/src)

## Kaikki väärinpäin
Kirjoita funktio kaikki_vaarinpain, joka saa parametrikseen listan merkkijonoja. Funktio luo ja palauttaa uuden listan, jossa kaikki alkuperäisellä listalla olevat merkkijonot on käännetty. Myös listan alkioiden järjestys muutetaan käänteiseksi.

Esimerkki funktion käytöstä:
```python
lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
lista2 = kaikki_vaarinpain(lista)
print(lista2)
```
```
['isky äleiv', 'ikkremise', 'ikkiak', 'ioM']
```

[Vastaus](osa04-21_kaikki_vaarinpain/src)

## Eniten kirjaimia
Kirjoita funktio eniten_kirjainta, joka saa parametrikseen merkkijonon. Funktio palauttaa kirjaimen, jota esiintyy eniten merkkijonossa. Jos yhtä yleisiä kirjaimia on monta, funktion tulee palauttaa niistä ensimmäisenä merkkijonossa esiintyvä.

Esimerkki funktion käytöstä:
```python
mjono = "abcbdbe"
print(eniten_kirjainta(mjono))

toinen_jono = "esimerkkimerkkijonokki"
print(eniten_kirjainta(toinen_jono))
```
```
b
k
```

[Vastaus](osa04-22_eniten_kirjaimia/src)

## Vokaalit pois
Kirjoita funktio ilman_vokaaleja, joka saa parametrikseen merkkijonon. Funktio palauttaa uuden merkkijonon, jossa alkuperäisen merkkijonon vokaalit on poistettu.

Voit olettaa, että merkkijono koostuu pelkästään pienistä suomen kielen kirjaimista a...ö.

Esimerkki funktion käytöstä:
```python
mjono = "tämä on esimerkki"
print(ilman_vokaaleja(mjono))
```
```
tm n smrkk
```

[Vastaus](osa04-23_vokaalit_pois/src)

## Poista isot
Pythonin merkkijonometodi isupper() palauttaa arvon True, jos merkkijono koostuu pelkästään isoista kirjaimista.

Esimerkiksi:
```python
print("XYZ".isupper())

onko_iso = "Abc".isupper()
print(onko_iso)
```
```
True
False
```

Kirjoita metodia hyödyntäen funktio poista_isot, joka saa parametrikseen listan merkkijonoja. Funktio palauttaa uuden listan, jolla on sen parametrina olevasta listasta ne merkkijonot, jotka eivät koostu kokonaan isoista kirjaimista.

Esimerkki funktion käytöstä:
```python
lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
karsittu_lista = poista_isot(lista)
print(karsittu_lista)
```
```
['def', 'pieni', 'toinen pieni', 'Osittain Iso']
```

[Vastaus](osa04-24_poista_isot/src)

## Naapureita listassa
Määritellään, että listan alkiot ovat naapureita, jos niiden erotus on 1. Naapureita olisivat siis esim alkiot 1 ja 2 tai alkiot 56 ja 55.

Kirjoita funktio pisin_naapurijono, joka etsii listasta pisimmän peräkkäisiä naapureita sisältävän osalistan ja palauttaa sen pituuden.

Esimerkiksi listassa [1, 2, 5, 4, 3, 4] pisin tällainen osalista olisi [5, 4, 3, 4], ja sen pituus 4.

Esimerkki funktion kutsumisesta:
```pytohn
lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(pisin_naapurijono(lista))
```
```
4
```

[Vastaus](osa04-25_naapureita_listassa/src)

## Arvosanatilasto
Tässä tehtävässä toteutetaan ohjelma kurssin arvosanatilastojen tulostamiseen.

Ohjelmalle syötetään rivejä, jotka sisältävät yhden opiskelijan koepistemäärän sekä tehtyjen harjoitustehtävien määrän. Ohjelma tulostaa niiden perusteella arvosanoihin liittyviä tilastoja.

Koepisteet ovat kokonaislukuja väliltä 0–20. Tehtyjen harjoitustehtävien lukumäärät taas kokonaislukuja väliltä 0–100.

Ohjelma kyselee käyttäjältä rivejä niin kauan, kunnes käyttäjä syöttää tyhjän rivin. Voit olettaa, että kaikki rivit on syötetty "oikein", eli rivillä on joko kaksi kokonaislukua tai rivi on tyhjä.

Koepisteiden ja harjoitustehtävien syöttäminen etenee seuraavasti:

Esimerkkitulostus
```
Koepisteet ja harjoitusten määrä: 15 87
Koepisteet ja harjoitusten määrä: 10 55
Koepisteet ja harjoitusten määrä: 11 40
Koepisteet ja harjoitusten määrä: 4 17
Koepisteet ja harjoitusten määrä:
Tilasto:
```
Kun käyttäjä on syöttänyt tyhjän rivin, tulostaa ohjelma tilastot.

Tilastot muodostuvat seuraavasti:

Tehtyjen harjoitustehtävien lukumäärästä saa harjoituspisteitä siten, että vähintään 10 % tehtävämäärästä tuo yhden harjoituspisteen, 20 % tuo 2 harjoituspistettä, jne., ja 100 % eli 100 harjoitustehtävää tuo 10 harjoituspistettä. Harjoitustehtävistä saatava pistemäärä on kokonaisluku.

Kurssin arvosana määräytyy kokeen pistemäärän ja harjoitustehtävistä saatavien pisteiden summasta seuraavan taulukon mukaan:

| koepisteet+harjoituspisteet |	arvosana        |
|-----------------------------|-----------------|
| 0–14	                      | 0 (eli hylätty) |
| 15–17	                      | 1               |
| 18–20	                      | 2               |
| 21–23	                      | 3               |
| 24–27	                      | 4               |
| 28–30	                      | 5               |

Edelliseen on kuitenkin poikkeus: jos kokeen pistemäärä on alle 10, on arvosana kokonaispistemäärästä riippumatta 0 eli hylätty.

Yllä olevalla esimerkkisyötteellä ohjelma tulostaa seuraavat tilastot:

Esimerkkitulostus
```
Tilasto:
Pisteiden keskiarvo: 14.5
Hyväksymisprosentti: 75.0
Arvosanajakauma:
  5:
  4:
  3: *
  2:
  1: **
  0: *
```
Desimaaliluvut tulostetaan yhden desimaalin tarkkuudella.

Huom: tässä tehtävässä (eikä missään muussakaan tehtävissä missä ei erikseen pyydetä funktioiden toteuttamista) mitään koodia ei tule sijoittaa if __name__ == "__main__"-lohkoon! Eli jos ohjelmasi toiminnallisuus on esim. funktiossa main, tulee sitä kutsuva koodi kirjoittaa normaaliin tapaan, eikä ym. if-lohkoon kuten on tehtävä niissä tehtävissä, joissa edellytetään funktioiden toteuttamista.

Vihje:

Ohjelman syöte koostuu riveistä joilla on peräkkäin kaksi numeroa:
```
Koepisteet ja harjoitusten määrä: 15 87
```

Syöterivi pitää pilkkoa ensin kahtia ja muuttaa palaset kokonaisluvuksi int-funktiolla. Rivin pilkkominen onnistuu samalla tavalla kun tehtävässä Eka, toka ja vika sana. Siihen on olemassa myös hieman helpompi keino, merkkijonojen metodi split. Googlaa jos haluat, käytä esim. hakusanoja python string split.

[Vastaus](osa04-26_arvosanatilasto/src)


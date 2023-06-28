# Osa 1 - Tehtävien vastaukset
## Hymiö
Kirjoita ohjelma, joka tulostaa ruudulle hymiön: :-)
## Korjaa ohjelma: seitsemän veljestä
Ohjelman tarkoitus on tulostaa seitsemän veljestä aakkosjärjestyksessä. Ohjelmassa on kuitenkin yksi tai useampi virhe, jonka takia se ei toimi oikein. Korjaa ohjelma niin, että veljekset tulostuvat oikeassa järjestyksessä.
## Ukko Nooa
Kirjoita ohjelma, joka tulostaa ruudulle seuraavat rivit (tarkalleen annetussa muodossa välimerkkeineen):
```
Ukko Nooa, Ukko Nooa oli kunnon mies.
Kun hän meni saunaan, laittoi laukun naulaan.
Ukko Nooa, Ukko Nooa oli kunnon mies.
```
## Minuutit vuodessa
Tee ohjelma, joka tulostaa minuuttien määrän vuodessa. Käytä edellisen esimerkin tapaan Pythonia tekemään laskutoimitus!
## Ohjelma tulostaa koodia
Pythonissa voidaan käyttää kaksinkertaisten lainausmerkkien " lisäksi myös yksinkertaista lainausmerkkiä '.

Tämä on kätevää, kun haluat tulostaa lainausmerkkejä:
```
print('"Heti takaisin!", poliisi huusi.')
```
```
"Heti takaisin!", poliisi huusi.
```
Tee ohjelma, jonka tulostus on seuraava:
```
print("Moi kaikki!")
```
## Nimi kahdesti
Kirjoita ohjelma, joka kysyy käyttäjän nimeä ja tämän jälkeen tulostaa nimen kahteen kertaan peräkkäisille riveille.

Ohjelman tulee toimia seuraavasti:
```
Anna nimesi: Pekka
Pekka
Pekka
```
## Nimet huutomerkillä
Kirjoita ohjelma, joka kysyy käyttäjän nimeä ja tämän jälkeen tulostaa nimen kaksi kertaa samalle riville siten, että rivin alussa lopussa sekä nimien välissä on huutomerkki.

Ohjelman tulee toimia seuraavasti:
```
Anna nimesi: Pekka
!Pekka!Pekka!
```
## Nimi ja osoite
Kirjoita ohjelma, joka kysyy käyttäjän nimeä ja osoitetta. Ohjelma tulostaa syötetyt tiedot.

Ohjelman tulee toimia seuraavasti:
```
Etunimi: Sanna
Sukunimi: Seppänen
Katuosoite: Mannerheimintie 10
Postinumero ja kaupunki: 00100 Helsinki
Sanna Seppänen
Mannerheimintie 10
00100 Helsinki
```
## Korjaa ohjelma: Lausahdukset
Tehtäväpohjassa on annettu ohjelma, jonka pitäisi kysyä käyttäjältä kolme lausahdusta ja tulostaa ne esimerkin mukaisesti:
```
Anna 1. osa: entten
Anna 2. osa: tentten
Anna 3. osa: teelikamentten
entten-tentten-teelikamentten!
```
Ohjelmassa on kuitenkin virhe tai virheitä, joiden takia se ei toimi oikein. Korjaa ohjelma.
## Tarina
Tee ohjelma, joka tulostaa oheisen tarinan, johon on upotettu käyttäjän antama nimi ja vuosi.
```
Anna nimi: Maija
Anna vuosi: 1572

Maija on urhea ritari, syntynyt vuonna 1572. Eräänä aamuna Maija heräsi kovaan meluun: lohikäärme lähestyi kylää. Vain Maija voisi pelastaa kylän asukkaat.
```
Tarinan tulee muuttua sen mukaan, mitkä tiedot käyttäjä antaa.
## Välilyönnillä vai ilman
Saat seuraavan koodinpätkän työnhakijoille suunnatun sovelluksen parissa työskentelevältä tuttavaltasi:
```
nimi = "Teppo Testaaja"
ika = 20
taito1 = "python"
taso1 = "aloittelija"
taito2 = "java"
taso2 = "veteraani"
taito3 = "ohjelmointi"
taso3 = "puoliammattilainen"
ala = 2000
yla = 3000

print("nimeni on ", nimi, " , olen ", ika, "-vuotias")
print("taitoihini kuuluvat")
print("- ", taito1, " (", taso1, ")")
print("- ", taito2, " (", taso2, ")")
print("- ", taito3, " (", taso3, " )")
print("haen työtä, josta maksetaan palkkaa", ala, "-", yla, "euroa kuussa")
```
Koodin pitäisi tuottaa täsmälleen seuraavanlainen tulostus:
```
nimeni on Teppo Testaaja, olen 20-vuotias

taitoihini kuuluvat
 - python (aloittelija)
 - java (veteraani)
 - ohjelmointi (puoliammattilainen)

haen työtä, josta maksetaan palkkaa 2000-3000 euroa kuussa
```
Koodi toimii melkein oikein, mutta ei kuitenkaan ihan. Tässä tehtävässä on todella tarkat testit, jotka vaativat, että tulostus on välilyönnilleen oikein.

Korjaa siis koodi siten, että tulostus näyttää oikealta. Huomaa, että erityisesti print-komennon muoto, jossa tulostettavat osat eritellään pilkulla, voi tuottaa yllätyksiä, sillä se lisää osien väliin välilyönnin.

Helpoiten saat muutettua koodin toimivaksi käyttämällä tulostukseen f-merkkijonoja.

Vihje: saat tulostettua tyhjän rivin komennolla print tai lisäämällä tulostettavaan merkkijonoon merkinnän \n.

Muista olla tarkkana tulostusten muodon suhteen jatkossakin kurssin tehtävissä. Osassa tehtävissä testit vaativat täsmälleen esimerkkitulostusten mukaisen muotoilun.
## Laskutoimitukset
Ohjelman tehtäväpohjassa on määritelty kaksi kokonaislukumuuttujaa x ja y:
```
x = 27
y = 15
```
Täydennä ohjelma siten, että sen tulostus on seuraava:
```
27 + 15 = 42
27 - 15 = 12
27 * 15 = 405
27 / 15 = 1.8
```
Ohjelman tulee toimia siinäkin tapauksessa, että muuttujien arvoa vaihdetaan. Eli jos ensimmäiset rivit muuttuvat muotoon
```
x = 4
y = 9
```
niin tulostus on seuraava:
```
4 + 9 = 13
4 - 9 = -5
4 * 9 = 36
4 / 9 = 0.4444444444444444
```
## Korjaa ohjelma: Tulostukset samalle riville
Jos print-komennolle annetaan lisäparametri end = "", komento ei tulosta rivinvaihtoa merkkijonon jälkeen.

Esimerkiksi:
```
print("Moi ", end="")
print("kaikki!")
```
```
Moi kaikki!
```
Korjaa ohjelma niin, että koko lasku tuloksineen tulostetaan yhdelle riville muuttamatta kuitenkaan print-komentojen määrää:
```
print(5)
print(" + ")
print(8)
print(" - ")
print(4)
print(" = ")
print(5 + 8 - 4)
```
## Luku kertaa viisi
Tee ohjelma, joka kysyy käyttäjältä lukua. Ohjelma tulostaa luvun kerrottuna viidellä.

Ohjelman tulee toimia seuraavasti:
```
Anna luku: 3
Kun kerrotaan 3 luvulla 5, saadaan 15
```
## Nimi ja ikä
Tee ohjelma, joka kysyy käyttäjältä tämän nimen ja syntymävuoden. Ohjelma tulostaa sitten viestin seuraavan esimerkin mukaisesti:
```
Anna nimi: Keijo Keksitty
Anna syntymävuosi: 1990
Moi Keijo Keksitty, olet 30 vuotta vanha vuoden 2020 lopussa
```
## Vuorokaudet sekunteina
Tee ohjelma, joka kysyy käyttäjältä vuorokausien lukumäärän. Tämän jälkeen ohjelma tulostaa sekuntien määrän annetuissa vuorokausissa.

Ohjelman tulee toimia seuraavasti:
```
Kuinka monen vuorokauden sekunnit tulostetaan? 1
86400
```
Toinen esimerkki:
```
Kuinka monen vuorokauden sekunnit tulostetaan? 7
604800
```
## Korjaa ohjelma: Lukujen tulo
Oheinen ohjelma kysyy käyttäjältä kolme lukua ja tulostaa näiden tulon (eli luvut kerrottuna toisillaan). Ohjelmassa on kuitenkin virhe tai virheitä, joiden takia se ei toimi. Korjaa ohjelma sellaiseksi, että se toimii oikein.

Ohjelman siis pitäisi toimia esimerkiksi näin:
```
Anna luku 1: 2
Anna luku 2: 3
Anna luku 3: 5
Tulo on 30
```
## Lukujen summa ja tulo
Tee ohjelma joka kysyy käyttäjältä kaksi lukua. Ohjelma tulostaa lukujen summan ja tulon.

Ohjelman tulee toimia seuraavasti:
```
Luku 1: 3
Luku 2: 7
Lukujen summa 10
Lukujen tulo 21
```
## Lukujen summa ja keskiarvo
Tee ohjelma, joka lukee käyttäjältä neljä lukua ja tulostaa niiden summan ja keskiarvon

Ohjelman tulee toimia seuraavasti:
```
Luku 1: 2
Luku 2: 1
Luku 3: 6
Luku 4: 7
Lukujen summa on 16 ja keskiarvo 4.0
```
## Ruokailukustannukset
Tee ohjelma, joka arvioi käyttäjän keskimääräisiä ruokailukustannuksia.

Ohjelma kysyy, kuinka monta kertaa viikossa käyttäjä käy Unicafessa ja Unicafe-lounaan hinnan sekä viikon muiden ruokaostosten hinnan.

Näiden tietojen perusteella ohjelma laskee käyttäjän keskimääräiset ruokamenot sekä viikossa että yhtenä päivänä.

Ohjelman tulee toimia seuraavasti:
```
Montako kertaa viikossa syöt Unicafessa? 4
Unicafe-lounaan hinta? 2.5
Paljonko käytät viikossa ruokaostoksiin? 28.5

Kustannukset keskimäärin:
Päivässä 5.5 euroa
Viikossa 38.5 euroa
```
## Opiskelijat ryhmiin
Tee ohjelma, joka kysyy kurssin opiskelijoiden määrän ja ryhmän koon ja ilmoittaa, montako ryhmää opiskelijoista muodostuu. Jos jako ei mene tasan, yhdessä ryhmässä voi olla vähemmän opiskelijoita, mutta kaikissa muissa on oltava haluttu määrä.
```
Montako opiskelijaa? 8
Mikä on ryhmän koko? 4
Ryhmien määrä: 2
```
```
Montako opiskelijaa? 11
Mikä on ryhmän koko? 3
Ryhmien määrä: 4
```
Vihje: tehtävän tekeminen onnistuu kokonaislukujakolaskuoperaattorilla //

Vihje2: jos et keksi miten tehtävä ratkeaa, älä huolestu suotta vaan tutustu seuraavassa luvussa esiteltävään ehtorakenteeseen. Ehtorakenteen avulla tehtävä on huomattavasti helpompi ratkaista.
## Orwell
Tee ohjelma, joka kysyy käyttäjältä kokonaisluvun ja tulostaa merkkijonon "Orwell" jos luku on täsmälleen 1984. Muussa tapauksessa ohjelma ei tulosta mitään.
```
Anna luku: 2020
```
```
Anna luku: 1984
Orwell
```
## Itseisarvo
Kirjoita ohjelma, joka lukee käyttäjältä kokonaisluvun. Mikäli luku on pienempi kuin 0, ohjelma tulostaa luvun kerrottuna luvulla -1. Muulloin ohjelma tulostaa käyttäjän syöttämän luvun. Alla on muutamia esimerkkejä ohjelman odotetusta toiminnasta.
```
Anna luku: -7
Luvun itseisarvo on 7
```
```
Anna luku: 1
Luvun itseisarvo on 1
```
```
Anna luku: -99
Luvun itseisarvo on 99
```
## Keittoa vai ei
Kirjoita ohjelma, joka kysyy ensin käyttäjän nimen. Jos nimi on mikä tahansa muu kuin "Jerry", ohjelma kysyy keittoannosten lukumäärän ja kertoo sitten kokonaishinnan. Yksi annos maksaa 5,90.

Kaksi esimerkkisuoritusta:
```
Mikä on nimesi: Kramer
Kuinka monta annosta keittoa: 2
Kokonaishinta on 11.8
Seuraava!
```
```
Mikä on nimesi: Jerry
Seuraava!
```
## Luvun suuruusluokka
Tee ohjelma, joka lukee käyttäjältä kokonaisluvun ja kertoo sitten sen suuruusluokan oheisten esimerkkisuoritusten mukaisesti:
```
Anna luku: 950
Luku on pienempi kuin 1000
Kiitos!
```
```
Anna luku: 59
Luku on pienempi kuin 1000
Luku on pienempi kuin 100
Kiitos!
```
```
Anna luku: 2
Luku on pienempi kuin 1000
Luku on pienempi kuin 100
Luku on pienempi kuin 10
Kiitos!
```
```
Anna luku: 1123
Kiitos!
```
## Laskin
Tee ohjelma, joka kysyy käyttäjältä ensin kaksi lukua ja sen jälkeen komennon. Jos komento on joko summa, tulo tai erotus, ohjelma laskee syötteille kyseisen operaation tuloksen. Muussa tapauksessa ohjelma ei tulosta mitään.

Esimerkkitulostuksia:
```
Luku 1: 10
Luku 2: 17
Komento: summa

10 + 17 = 27
```
```
Luku 1: 4
Luku 2: 6
Komento: tulo

4 * 6 = 24
```
```
Luku 1: 4
Luku 2: 6
Komento: erotus

4 - 6 = -2
```
## Lämpötilat
Tee ohjelma, joka kysyy käyttäjältä lämpötilan fahrenheit-asteina, ja tulostaa sitten lämpötilan celsius-asteina. Jos lämpötila celsius-asteina on pienempi kuin 0, ohjelma tulostaa lisäksi viestin "Paleltaa!".

Kaavan fahrenheit-asteiden muuntamiseksi celsius-asteiksi voit etsiä esimerkiksi googlaamalla.

Kaksi esimerkkisuoritusta:
```
Anna lämpötila (F): 101
101 fahrenheit-astetta on 38.333333333333336 celsius-astetta

Anna lämpötila (F): 21
21 fahrenheit-astetta on -6.111111111111111 celsius-astetta
Paleltaa!
```
## Palkka
Tee ohjelma, joka kysyy tuntipalkkaa, työskenneltyjen tuntien määrää ja viikonpäivää. Ohjelma tulostaa palkan, joka on tuntipalkka kertaa tuntien määrä muina päivinä paitsi sunnuntaisin, jolloin tuntipalkka on kaksinkertainen.
```
Tuntipalkka: 8.5
Työtunnit: 3
Viikonpäivä: maanantai
Palkka 25.5 euroa
```
```
Tuntipalkka: 12.5
Työtunnit: 10
Viikonpäivä: sunnuntai
Palkka 250.0 euroa
```
## Korjaa ohjelma: Korkoa kortille
Ohjelmassa lasketaan bonuskortin saldoon vuoden lopussa lisättävä bonuspistemäärä seuraavan kaavan mukaisesti:

- Jos bonuspisteitä on alle sata, korkona saa 10 % lisää pisteitä
- Muussa tapauksessa korkona saa 15 % lisää pisteitä
Ohjelma siis toimii esim. näin:
```
Kuinka paljon pisteitä? 55
Sait 10 % bonusta
Pisteitä on nyt 60.5
```
Ohjelma toimii kuitenkin jollain syötteillä oudosti:
```
Kuinka paljon pisteitä? 95
Sait 10 % bonusta
Sait 15 % bonusta
Pisteitä on nyt 120.175
```
Korjaa ohjelma niin, että bonusta tulee joko 10 % tai 15 %, ei koskaan molempia.
## Huomiset vaatteet
Tee ohjelma, joka kysyy huomisen sääennusteen ja suosittelee sen mukaista pukeutumista.

Suositus vaihtelee sen mukaan, onko lämpötila yli 20 astetta, yli 10 astetta vai yli 5 astetta. Myös sade vaikuttaa suositukseen.

Ohjelma toimii seuraavasti:
```
Kerro huominen sääennuste:
Lämpötila: 21
Sataako (kyllä/ei): ei
Pue housut ja t-paita
```
```
Kerro huominen sääennuste:
Lämpötila: 11
Sataako (kyllä/ei): ei
Pue housut ja t-paita
Ota myös pitkähihainen paita
```
```
Kerro huominen sääennuste:
Lämpötila: 7
Sataako (kyllä/ei): ei
Pue housut ja t-paita
Ota myös pitkähihainen paita
Pue päälle takki
```
```
Kerro huominen sääennuste:
Lämpötila: 3
Sataako (kyllä/ei): kyllä
Pue housut ja t-paita
Ota myös pitkähihainen paita
Pue päälle takki
Suosittelen lämmintä takkia
Kannattaa ottaa myös hanskat
Muista sateenvarjo!
```
## Toisen asteen yhtälön ratkaiseminen
Pythonin math-moduulissa on funktio sqrt, jolla voi laskea luvun neliöjuuren. Voit käyttää sitä ohjelmassa seuraavasti:
```
from math import sqrt

print(sqrt(9))
```
Ohjelma tulostaa:
```
3.0
```
Kirjoita ohjelma, joka ratkaisee toisen asteen yhtälön ax²+bx+c. Ohjelmalle annetaan arvot a, b ja c, ja sen tulee laskea juuret (eli ratkaisut) kaavalla

x = (-b ± sqrt(b²-4ac))/(2a).

Voit olettaa, että yhtälöllä on kaksi juurta, jolloin yllä oleva kaava toimii.

Esimerkkituloste:
```
Anna a: 1
Anna b: 2
Anna c: -8

Juuret ovat 2.0 ja -4.0
```

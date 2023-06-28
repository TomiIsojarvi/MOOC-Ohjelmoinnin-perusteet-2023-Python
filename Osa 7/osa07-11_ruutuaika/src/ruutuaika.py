# tee ratkaisu tänne,
from datetime import datetime, timedelta

if True:
	# Release
	tiedosto_nimi = input("Tiedosto: ")
	aloitus_paiva = input("Aloituspäivä: ")
	paivat = int(input("Montako päivää: "))
else:
	# Debug
	tiedosto_nimi = "kesakuun_loppu.txt"
	aloitus_paiva = "24.6.2020"
	paivat = 5

ruutuajat = []

aloitus_paiva = datetime.strptime(aloitus_paiva, "%d.%m.%Y")

print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")

for i in range(0, paivat):
	paiva = aloitus_paiva + timedelta(days = i)
	ruutuaika = input("Ruutuaika " + paiva.strftime("%d.%m.%Y") + ": ")
	ruutuaika = ruutuaika.split()

	if len(ruutuaika) != 3:
		raise ValueError("Ruutuajat väärin.")

	ruutuajat.append(ruutuaika)

# Luodaan tiedosto ja kirjoitetaan tiedot.
with open(tiedosto_nimi, "w") as tiedosto:
	# Kirjoitetaan ajanjakso
	loppupaiva = aloitus_paiva + timedelta(days = paivat - 1)
	tiedosto.write("Ajanjakso: " + aloitus_paiva.strftime("%d.%m.%Y") + "-" + loppupaiva.strftime("%d.%m.%Y") + "\n")

	# Kirjoitetaan minuutit yhteensä.
	minuutit = 0
	for ruutuaika in ruutuajat:
		for ajat in ruutuaika:
			minuutit += int(ajat)

	tiedosto.write("Yht. minuutteja: " + str(minuutit) + "\n")

	# Kirjoitetaan keskimääräiset minuutit.
	keskimaaraiset = minuutit / paivat
	tiedosto.write("Keskim. minuutteja: " + str(keskimaaraiset) + "\n")

	# kirjoitetaan kaikki ruutuajat.
	for paiva in range(paivat):
		paivamaara = aloitus_paiva + timedelta(days = paiva)
		minuutit = ruutuajat[paiva]

		tiedosto.write(paivamaara.strftime("%d.%m.%Y") + ": " + minuutit[0] + "/" + minuutit[1] + "/" + minuutit[2] + "\n")


	print("Tiedot tallennettu tiedostoon " + tiedosto_nimi)
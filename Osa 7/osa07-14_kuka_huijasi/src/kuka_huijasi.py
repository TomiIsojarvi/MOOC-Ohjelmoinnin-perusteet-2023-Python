# tee ratkaisu tänne
import csv
from datetime import datetime, timedelta

def huijarit():
	aloitusajat = []
	palautukset = []
	huijarit = []

	# Luetaan aloitusajat omaan listaan.
	with open("tentin_aloitus.csv") as tiedosto:
		for rivi in csv.reader(tiedosto, delimiter=";"):
			tunnus = rivi[0]
			aloitusaika = datetime.strptime(rivi[1], "%H:%M")
			aloitusajat.append({"tunnus": tunnus, "aloitusaika": aloitusaika})

	# Luetaan palautukset omaan listaan.
	with open("palautus.csv") as tiedosto:
		for rivi in csv.reader(tiedosto, delimiter=";"):
			tunnus = rivi[0]
			tehtava = rivi[1]
			pisteet = rivi[2]
			palautusaika = datetime.strptime(rivi[3], "%H:%M")
			palautukset.append({"tunnus": rivi[0], "tehtava": tehtava, "pisteet": pisteet, "palautusaika": palautusaika})

	# Etsitään huijarit.
	for palautus in palautukset:
		tunnus = palautus["tunnus"]
		palautusaika = palautus["palautusaika"]

		for aloitus in aloitusajat:
			if aloitus["tunnus"] == tunnus:
				aloitusaika = aloitus["aloitusaika"]
				erotus = palautusaika - aloitusaika

				if erotus > timedelta(hours=3):
					if tunnus not in huijarit:
						huijarit.append(tunnus)

	return huijarit

if __name__ == '__main__':
	print(huijarit())
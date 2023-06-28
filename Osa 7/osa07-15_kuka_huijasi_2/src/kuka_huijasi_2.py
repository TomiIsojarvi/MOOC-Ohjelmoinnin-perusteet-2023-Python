# tee ratkaisu tänne
import csv
from datetime import datetime, timedelta

def viralliset_pisteet():
	viralliset = {}
	lopulliset_pisteet = {}

	# Avataan tentin_aloitus.csv ja tallennetaan aloitusaika sanakirjaan.
	with open("tentin_aloitus.csv") as tiedosto:
		# Jokaiselta riviltä...
		for rivi in csv.reader(tiedosto, delimiter=";"):
			tunnus = rivi[0]

			if tunnus not in viralliset:
				viralliset[tunnus] = {}

			viralliset[tunnus]["aloitusaika"] = datetime.strptime(rivi[1], "%H:%M")

	# Avataan palautus.csv ja tallennetaan tehtävien pisteet sanakirjaan.
	with open("palautus.csv") as tiedosto:
		# Jokaiselta riviltä...
		for rivi in csv.reader(tiedosto, delimiter=";"):
			tunnus = rivi[0]
			tehtava = rivi[1]
			pisteet = int(rivi[2])
			palautusaika = datetime.strptime(rivi[3], "%H:%M")

			# Jos kulunut yli 3 tuntia tehtävässä, jatketaan eteenpäin.
			erotusaika = palautusaika - viralliset[tunnus]["aloitusaika"]
			if erotusaika > timedelta(hours=3):
				continue

			# Onko tehtävä jo sanakirjassa? Jos ei, niin lisätään se.
			if tehtava not in viralliset[tunnus]:
				viralliset[tunnus][tehtava] = pisteet

			# Onko suurempi arvosana?
			if pisteet > viralliset[tunnus][tehtava]:
				viralliset[tunnus][tehtava] = pisteet

	# Luodaan sanakirja lopullisille pisteille.
	for opiskelija in viralliset:
		if opiskelija not in lopulliset_pisteet:
			lopulliset_pisteet[opiskelija] = 0

		for tehtava in viralliset[opiskelija]:
			if tehtava == "aloitusaika":
				continue

			lopulliset_pisteet[opiskelija] += viralliset[opiskelija][tehtava]

	return lopulliset_pisteet

if __name__ == '__main__':
	print(viralliset_pisteet())
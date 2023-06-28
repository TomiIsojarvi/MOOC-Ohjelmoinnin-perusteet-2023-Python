# tee ratkaisu tänne
def main():
	if True:
		# Release
		opiskelijatiedot = input("Opiskelijatiedot: ")
		tehtavatiedot = input("Tehtävätiedot: ")
	else:
		# Debug
		opiskelijatiedot = "opiskelijat1.csv"
		tehtavatiedot = "tehtavat1.csv"

	nimet = {}

	# Avataan opiskelijatiedot
	with open(opiskelijatiedot) as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')
			if osat[0] == "opnro":
				continue

			nimet[osat[0]] = osat[1] + " " + osat[2]

	tehtavat = {}

	# Avataan tehtävätiedot
	with open(tehtavatiedot) as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')

			if osat[0] == "opnro":
				continue

			summa = 0

			for osa in osat[1:]:
				summa += int(osa)

			tehtavat[osat[0]] = summa

	# Tulostetaan
	for opnro, nimi in nimet.items():
		print(f"{nimi} {tehtavat[opnro]}")

main()
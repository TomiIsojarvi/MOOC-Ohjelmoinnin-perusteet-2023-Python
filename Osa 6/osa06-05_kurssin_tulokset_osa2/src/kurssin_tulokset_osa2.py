# tee ratkaisu tänne
def main():
	if False:
		# Release
		opiskelijatiedot = input("Opiskelijatiedot: ")
		tehtavatiedot = input("Tehtävätiedot: ")
		tehtavatiedot = input("Koepisteet: ")
	else:
		# Debug
		opiskelijatiedot = "opiskelijat1.csv"
		tehtavatiedot = "tehtavat1.csv"
		koepistetiedot = "koepisteet1.csv"

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

	koepisteet = {}

	# Avataan koepistetiedot
	with open(koepistetiedot) as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')

			if osat[0] == "opnro":
				continue

			summa = 0

			for osa in osat[1:]:
				summa += int(osa)

			koepisteet[osat[0]] = summa

	# Tulostetaan
	for opnro, nimi in nimet.items():
		# Lasketaan tehtävien pisteet.
		tehtavapisteet = int(tehtavat[opnro] / 40 * 10)

		yhteensa = tehtavapisteet + koepisteet[opnro]
		arvosana = 0

		# Lasketaan karvosana.
		if yhteensa >= 0 and yhteensa < 15:
			arvosana = 0
		elif yhteensa >= 15 and yhteensa < 18:
			arvosana = 1
		elif yhteensa >= 18 and yhteensa < 21:
			arvosana = 2
		elif yhteensa >= 21 and yhteensa < 24:
			arvosana = 3
		elif yhteensa >= 24 and yhteensa < 28:
			arvosana = 4
		else:
			arvosana = 5

		print(f"{nimi} {arvosana}")

main()
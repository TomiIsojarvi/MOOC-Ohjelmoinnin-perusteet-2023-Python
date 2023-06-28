# tee ratkaisu tänne

#------------------------------------------------------------------------------
# lue_opiskelijatiedot - Lukee opiskelijatiedot tiedostosta
#------------------------------------------------------------------------------
def lue_opiskelijatiedot(tiedostonimi: str):
	nimet = {}

	with open(tiedostonimi) as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')
			if osat[0] == "opnro":
				continue

			nimet[osat[0]] = osat[1] + " " + osat[2]

	return nimet

#------------------------------------------------------------------------------
# lue_tehtavatiedot - Lukee tehtävätiedot tiedostosta ja summaa pisteet yhteen
#------------------------------------------------------------------------------
def lue_tehtavatiedot(tiedostonimi: str):
	tehtavat = {}

	with open(tiedostonimi) as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')

			if osat[0] == "opnro":
				continue

			summa = 0

			for osa in osat[1:]:
				summa += int(osa)

			tehtavat[osat[0]] = summa

	return tehtavat

#------------------------------------------------------------------------------
# lue_koepistetiedot - Lukee koepistetiedot tiedostosta ja summaa koepisteet
#------------------------------------------------------------------------------
def lue_koepistetiedot(tiedostonimi: str):
	koepisteet = {}

	# Avataan koepistetiedot
	with open(tiedostonimi) as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')

			if osat[0] == "opnro":
				continue

			summa = 0

			for osa in osat[1:]:
				summa += int(osa)

			koepisteet[osat[0]] = summa

	return koepisteet

#------------------------------------------------------------------------------
# lue_kurssitiedot - Lukee kurssitiedot tiedostosta
#------------------------------------------------------------------------------
def lue_kurssitiedot(tiedostonimi: str):
	with open(tiedostonimi) as tiedosto:
		nimi = ""
		laajuus = 0
		rivit = []

		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(': ')
			rivit.append(osat[1])

		nimi = rivit[0]
		laajuus = rivit[1]
		
	return {"nimi": nimi, "laajuus": laajuus}

#------------------------------------------------------------------------------
# laske_pisteet - Laskee kokonaispisteet
#------------------------------------------------------------------------------
def laske_pisteet(opiskelija_nro: int, tehtavat: dict, koepisteet: dict):
	teht_pist = int(tehtavat[opiskelija_nro] / 40 * 10)
	koe_pist = koepisteet[opiskelija_nro]
	kok_pist = teht_pist + koe_pist

	return kok_pist

#------------------------------------------------------------------------------
# laske_arvosana - Laskee arvosanan pisteiden perusteella
#------------------------------------------------------------------------------
def laske_arvosana(pisteet):
	if pisteet >= 0 and pisteet < 15:
		return 0
	elif pisteet >= 15 and pisteet < 18:
		return 1
	elif pisteet >= 18 and pisteet < 21:
		return 2
	elif pisteet >= 21 and pisteet < 24:
		return 3
	elif pisteet >= 24 and pisteet < 28:
		return 4
	else:
		return 5

#------------------------------------------------------------------------------
# tulosta_tiedot - Tulostaa opiskelijoiden tiedot
#------------------------------------------------------------------------------
def tulosta_tiedot(kurssi: dict, nimet: dict, tehtavat: dict, koepisteet: dict):

	# Tulostetaan otsikot ---------------

	kurssi_merkkijono = f"{kurssi['nimi']}, {kurssi['laajuus']} opintopistettä"
	print(kurssi_merkkijono)

	for i in range(0, len(kurssi_merkkijono)):
		print("=", end="")

	print()
	print("nimi" + 26 * " " + "teht_lkm  teht_pist koe_pist  yht_pist  arvosana")

	#------------------------------------

	for opiskelija_nro, nimi in nimet.items():
		# Lasketaan opiskelijan pisteet
		tehtava_lkm = tehtavat[opiskelija_nro] 
		tehtava_pist = int(tehtavat[opiskelija_nro] / 40 * 10)
		koe_pist = koepisteet[opiskelija_nro]
		yht_pist = tehtava_pist + koe_pist

		# Arvosana
		arvosana = laske_arvosana(yht_pist)

		# Tulostetaan opiskelijan tiedot
		print(f"{nimi:30}{tehtava_lkm:<10}{tehtava_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana:<10}")

#------------------------------------------------------------------------------
# tulosta_tiedostoon - Tulostaa opiskelijoiden tiedot tiedostoon
#------------------------------------------------------------------------------
def tulosta_tiedostoon(tiedostonimi: str, kurssi: dict, nimet: dict, tehtavat: dict, koepisteet: dict):

	with open(tiedostonimi, "w") as tiedosto:

		# Kirjoitetaan otsikot ------------

		kurssi_merkkijono = f"{kurssi['nimi']}, {kurssi['laajuus']} opintopistettä\n"
		tiedosto.write(kurssi_merkkijono)
		
		strjono = ""
		for i in range(0, len(kurssi_merkkijono) - 1):
			strjono += "="

		tiedosto.write(strjono + "\n")
		tiedosto.write("nimi" + 26 * " " + "teht_lkm  teht_pist koe_pist  yht_pist  arvosana\n")

		#----------------------------------

		for opiskelija_nro, nimi in nimet.items():
			# Lasketaan pisteet
			tehtava_lkm = tehtavat[opiskelija_nro] 
			tehtava_pist = int(tehtavat[opiskelija_nro] / 40 * 10)
			koe_pist = koepisteet[opiskelija_nro]
			yht_pist = tehtava_pist + koe_pist

			# Arvosana
			arvosana = laske_arvosana(yht_pist)

			tiedosto.write(f"{nimi:30}{tehtava_lkm:<10}{tehtava_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana:<10}\n")

#------------------------------------------------------------------------------
# tallenna_tiedot - Tallenaa tiedot .csv-tiedostoon
#------------------------------------------------------------------------------
def tallenna_tiedot(tiedostonimi: str, kurssi: dict, nimet: dict, tehtavat: dict, koepisteet: dict):
	with open(tiedostonimi, "w") as tiedosto:

		for opiskelija_nro, nimi in nimet.items():
			# Lasketaan pisteet
			tehtava_lkm = tehtavat[opiskelija_nro] 
			tehtava_pist = int(tehtavat[opiskelija_nro] / 40 * 10)
			koe_pist = koepisteet[opiskelija_nro]
			yht_pist = tehtava_pist + koe_pist

			# Arvosana
			arvosana = laske_arvosana(yht_pist)

			tiedosto.write(f"{opiskelija_nro};{nimi};{arvosana}\n")

#------------------------------------------------------------------------------
# main - Pääfunktio
#------------------------------------------------------------------------------
def main():
	if True:
		# Release
		opiskelijatiedot = input("Opiskelijatiedot: ")
		tehtavatiedot = input("Tehtävätiedot: ")
		koepistetiedot = input("Koepisteet: ")
		kurssitiedot = input("Kurssin tiedot: ")
	else:
		# Debug
		opiskelijatiedot = "opiskelijat2.csv"
		tehtavatiedot = "tehtavat2.csv"
		koepistetiedot = "koepisteet2.csv"
		kurssitiedot = "kurssi2.txt"

	nimet = lue_opiskelijatiedot(opiskelijatiedot)
	tehtavat = lue_tehtavatiedot(tehtavatiedot)
	koepisteet = lue_koepistetiedot(koepistetiedot)
	kurssi = lue_kurssitiedot(kurssitiedot)
	
	#tulosta_tiedot(kurssi, nimet, tehtavat, koepisteet)
	tulosta_tiedostoon("tulos.txt", kurssi, nimet, tehtavat, koepisteet)
	tallenna_tiedot("tulos.csv", kurssi, nimet, tehtavat, koepisteet)

	print("Tulokset talletettu tiedostoihin tulos.txt ja tulos.csv")

main()
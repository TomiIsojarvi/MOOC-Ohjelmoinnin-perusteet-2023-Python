# tee ratkaisu tänne

#------------------------------------------------------------------------------
# lue_opiskelijatiedot - Lukee opiskelijatiedot tiedostosta
#------------------------------------------------------------------------------
def lue_opiskelijatiedot(tiedostonimi):
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
# lue_tehtavatiedot - Lukee tehtävätiedot tiedostosta
#------------------------------------------------------------------------------
def lue_tehtavatiedot(tiedostonimi):
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
# lue_koepistetiedot - Lukee koepistetiedot tiedostosta
#------------------------------------------------------------------------------
def lue_koepistetiedot(tiedostonimi):
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
def tulosta_tiedot(nimet: dict, tehtavat: dict, koepisteet: dict):
	print("nimi" + 26 * " " + "teht_lkm  teht_pist koe_pist  yht_pist  arvosana")

	for opnro, nimi in nimet.items():

		# Lasketaan pisteet
		teht_lkm = tehtavat[opnro] 
		teht_pist = int(tehtavat[opnro] / 40 * 10)
		koe_pist = koepisteet[opnro]
		yht_pist = teht_pist + koe_pist

		# Arvosana
		arvosana = laske_arvosana(yht_pist)

		print(f"{nimi:30}{teht_lkm:<10}{teht_pist:<10}{koe_pist:<10}{yht_pist:<10}{arvosana:<10}")

#------------------------------------------------------------------------------
# main - Pääfunktio
#------------------------------------------------------------------------------
def main():
	if True:
		# Release
		opiskelijatiedot = input("Opiskelijatiedot: ")
		tehtavatiedot = input("Tehtävätiedot: ")
		koepistetiedot = input("Koepisteet: ")
	else:
		# Debug
		opiskelijatiedot = "opiskelijat1.csv"
		tehtavatiedot = "tehtavat1.csv"
		koepistetiedot = "koepisteet1.csv"

	nimet = lue_opiskelijatiedot(opiskelijatiedot)
	tehtavat = lue_tehtavatiedot(tehtavatiedot)
	koepisteet = lue_koepistetiedot(koepistetiedot)
	
	tulosta_tiedot(nimet, tehtavat, koepisteet)

main()
# tee ratkaisu tänne
def lue_hedelmat():
	hedelmat = {}

	with open("hedelmat.csv") as tiedosto:
		for rivi in tiedosto:
			#rivi = rivi.replace("\n", "")
			osat = rivi.split(";")
			hedelmat[osat[0]] = float(osat[1])

	return hedelmat
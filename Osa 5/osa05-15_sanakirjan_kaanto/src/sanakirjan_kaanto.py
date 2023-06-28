# tee ratkaisu tänne
def kaanna(sanakirja: dict):
	uusi_sanakirja = {}

	for elem in sanakirja:
		uusi_sanakirja[sanakirja[elem]] = elem

	for avain, arvo in uusi_sanakirja.items():
		sanakirja[avain] = arvo
		del sanakirja[arvo]

#if __name__ == "__main__":
#	s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
#	kaanna(s)
#	print(s)
# tee ratkaisu tänne
def suurin():
	with open("luvut.txt") as tiedosto:
		suurin = 0

		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			luku = int(rivi)
			if luku > suurin:
				suurin = luku

	return suurin
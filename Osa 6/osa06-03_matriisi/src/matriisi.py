# tee ratkaisu tänne
def maksimi():
	with open("matriisi.txt") as tiedosto:
		suurin = 0
		luvut = []

		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			luvut = rivi.split(",")

			for luku in luvut:
				if int(luku) > suurin:
					suurin = int(luku)

	return suurin

def summa():
	summa = 0
	luvut = []

	with open("matriisi.txt") as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			luvut = rivi.split(",")
			
			for luku in luvut:
				summa += int(luku)

	return summa

def rivisummat():
	summat = []

	with open("matriisi.txt") as tiedosto:
		for rivi in tiedosto:
			summa = 0
			rivi = rivi.replace("\n", "")
			luvut = rivi.split(",")

			for luku in luvut:
				summa += int(luku)

			summat.append(summa)
	
	return summat
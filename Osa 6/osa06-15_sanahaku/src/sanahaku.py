# tee ratkaisu tänne
import re

def hae_sanat(hakusana: str):
	sanat = []
	loydetyt = []

	with open("sanat.txt") as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			sanat.append(rivi)

	if "." in hakusana:
		pituus = str(len(hakusana))

		# Haetaan ensin hakusanan pituiset osumat
		regex = re.compile("^[a-zA-Z]{" + pituus + "}$")
		loydetyt = list(filter(regex.match, sanat))

		# ...ja tämän jälkeen itse osumat.
		regex = re.compile(hakusana)
		loydetyt = list(filter(regex.match, loydetyt))
		
		return loydetyt
	
	elif hakusana.startswith("*") or hakusana.endswith("*"):
		if hakusana.startswith("*"):
			regex = re.compile("." + hakusana + "$")
		else:
			hakusana = hakusana[:-1]
			regex = re.compile(hakusana)
		loydetyt = list(filter(regex.match, sanat))

		return loydetyt
	
	else:
		pituus = str(len(hakusana))
		regex = re.compile("^" + hakusana + "$")
		loydetyt = list(filter(regex.match, sanat))
		return loydetyt

	
if __name__ == '__main__':
	print(hae_sanat("cat"))
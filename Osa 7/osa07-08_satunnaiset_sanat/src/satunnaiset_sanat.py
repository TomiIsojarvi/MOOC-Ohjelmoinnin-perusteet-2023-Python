# tee ratkaisu tänne
import re
from random import sample

def sanat(n: int, alku: str):
	sanat = []
	loydetyt = []

	with open("sanat.txt") as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			sanat.append(rivi)
	
	regex = re.compile("^" + alku)
	loydetyt = list(filter(regex.match, sanat))

	if len(loydetyt) < n:
		raise ValueError("Ei tarpeeksi tuloksia")
	
	arvotut_sanat = rivi = sample(loydetyt, n)

	return arvotut_sanat

if __name__ == '__main__':
	lista = sanat(3, "ca")
	for sana in lista:
			print(sana)
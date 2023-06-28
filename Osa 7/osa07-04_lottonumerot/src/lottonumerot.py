# tee ratkaisu tänne
from random import shuffle

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
	kaikki = list(range(alaraja, ylaraja + 1))
	shuffle(kaikki)
	rivi = kaikki[0:maara]
	rivi.sort()
	return rivi

if __name__ == '__main__':
	for numero in lottonumerot(7, 1, 40):
		print(numero)
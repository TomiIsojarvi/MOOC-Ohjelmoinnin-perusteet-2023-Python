# tee ratkaisu tänne
from random import choice

def heita(noppa: str):
	tulos = 0

	noppaA = [3, 3, 3, 3, 3, 6]
	noppaB = [2, 2, 2, 5, 5, 5]
	noppaC = [1, 4, 4, 4, 4, 4]

	if noppa == "A":
		tulos = choice(noppaA)
	elif noppa == "B":
		tulos = choice(noppaB)
	else:
		tulos = choice(noppaC)

	return tulos

def pelaa(noppa1: str, noppa2: str, kertaa: int):
	noppa1_voitot = 0
	noppa2_voitot = 0
	tasapelit = 0

	for i in range(0, kertaa):
		luku1 = heita(noppa1)
		luku2 = heita(noppa2)

		if luku1 > luku2:
			noppa1_voitot += 1
		elif luku1 < luku2:
			noppa2_voitot += 1
		else:
			tasapelit += 1

	return (noppa1_voitot, noppa2_voitot, tasapelit)

if __name__ == '__main__':
	tulos = pelaa("A", "C", 1000)
	print(tulos)
	tulos = pelaa("B", "B", 1000)
	print(tulos)
# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkio: int):
	samat = 0

	for rivi in matriisi:
		for sarake in rivi:
			if sarake == alkio:
				samat += 1

	return samat

if __name__ == '__main__':
	m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
	print(laske_alkiot(m, 1))

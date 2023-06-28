# tee ratkaisu tänne
def transponoi(matriisi: list):
	koko = len(matriisi)
	uusi_matriisi = []

	# Tehdään samankokoinen nollilla täytetty matriisi
	for rivi in range(koko):
		temp_rivi = []
		for sarake in range(koko):
			temp_rivi.append(0)
		uusi_matriisi.append(temp_rivi)

	# Transponoidaan
	for i in range(koko):
	 for j in range(koko):
			uusi_matriisi[j][i] = matriisi[i][j]

	# Kopioidaan
	matriisi[:] = uusi_matriisi

#if __name__ == '__main__':
#		matriisi = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#		transponoi(matriisi)
#
#		print(matriisi)
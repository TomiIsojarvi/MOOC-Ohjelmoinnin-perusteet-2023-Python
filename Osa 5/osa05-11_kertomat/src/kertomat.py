# tee ratkaisu tänne
def kertomat(n: int):
	luvut = {}
	luvut[1] = 1

	for luku in range(2, n + 1):
		kertoma = 1
		for i in range(2, luku + 1):
			kertoma *= i
		luvut[luku] = kertoma

	return luvut

#if __name__ == '__main__':
	#k = kertomat(5)
	#print(k[1])
	#print(k[3])
	#print(k[5])
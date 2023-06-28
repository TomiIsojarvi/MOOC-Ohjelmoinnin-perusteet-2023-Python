# tee ratkaisu tänne
def pisimmat(lista):
	suurin_pituus = 0
	suurimmat = []
	
	for i in lista:
		pituus = len(i)
		if pituus >= suurin_pituus:
			suurin_pituus = pituus
	
	for j in lista:
		pituus = len(j)
		if pituus == suurin_pituus:
			suurimmat.append(j)

	return suurimmat

if __name__ == '__main__':
	lista = ["eka", "toka", "kolmas", "seitsemäs"]

	tulos = pisimmat(lista)
	print(tulos)
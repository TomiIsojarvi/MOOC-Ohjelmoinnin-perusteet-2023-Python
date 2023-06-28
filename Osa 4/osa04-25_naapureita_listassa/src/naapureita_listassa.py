# tee ratkaisu tänne
def pisin_naapurijono(lista):
	temp = []
	#temp.append(lista[0])

	pituus = 0
	naapurit = []

	for x in range(1, len(lista)):
		if len(temp) == 0:
				temp.append(lista[x-1])

		if lista[x] == lista[x - 1] + 1 or lista[x] == lista[x - 1] - 1:
			temp.append(lista[x])
			if len(temp) > pituus:
				naapurit = temp.copy()
				pituus = len(naapurit)
		else:
			temp = []

	return pituus

if __name__ == '__main__':
	lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
	print(pisin_naapurijono(lista))
# tee ratkaisu tänne
def lyhin(lista):
	pienin_pituus = len(lista[0])
	sana = ""
	
	for i in lista:
		pituus = len(i)
		if pituus <= pienin_pituus:
			pienin_pituus = pituus
			sana = i

	return sana

if __name__ == '__main__':
	lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]

	tulos = lyhin(lista)
	print(tulos)
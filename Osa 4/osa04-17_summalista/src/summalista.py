# tee ratkaisu tänne

def summa(a: list, b: list):
	uusi_lista = []
	
	for i in range(len(a)):
		uusi_lista.append(a[i] + b[i])

	return uusi_lista

if __name__ =='__main__':
	a = [1, 2, 3]
	b = [7, 8, 9]
	print(summa(a, b)) # [8, 10, 12]
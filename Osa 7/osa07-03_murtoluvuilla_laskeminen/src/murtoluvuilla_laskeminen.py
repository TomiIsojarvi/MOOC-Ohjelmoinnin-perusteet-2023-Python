# tee ratkaisu tänne
from fractions import Fraction

def jaa_palasiksi(maara: int):
	lista = []
	
	for i in range(0, maara):
		lista.append(Fraction(1, maara))
		 
	return lista

if __name__ == '__main__':
	for p in jaa_palasiksi(3):
		print(p)
	print()
	print(jaa_palasiksi(5))


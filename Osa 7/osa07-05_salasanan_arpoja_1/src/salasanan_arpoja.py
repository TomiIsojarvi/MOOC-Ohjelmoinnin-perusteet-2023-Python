# tee ratkaisu tänne
from random import choice
from string import ascii_lowercase

def luo_salasana(maara: int):
	salasana = ""

	for i in range(maara):
		salasana += choice(ascii_lowercase)

	return salasana

if __name__ == '__main__':
	for i in range(10):
		print(luo_salasana(8))
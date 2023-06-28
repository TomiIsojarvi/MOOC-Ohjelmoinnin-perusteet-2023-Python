# tee ratkaisu tänne

# rivi_oikein-funktio: Tarkistaa rivit
def rivi_oikein(sudoku: list, rivi_nro: int):
	rivi = sudoku[rivi_nro]

	for i in range(1, 10):
		maara = 0
		for ruutu in rivi:
			if ruutu == i:
				maara += 1

			if maara > 1:
				return False

	return True

# sarake_oikein-funktio: Tarkistaa sarakkeet
def sarake_oikein(sudoku: list, sarake_nro: int):
	sarake = []
	for rivi in sudoku:
		sarake.append(rivi[sarake_nro])

	for i in range(1, 10):
		maara = 0
		for ruutu in sarake:
			if ruutu == i:
				maara += 1

			if maara > 1:
				return False

	return True

# nelio_oikein-funktio: Tarkistaa 3x3 -neliöt
def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
	rivit = sudoku[rivi_nro : rivi_nro + 3]
	nelio = []

	for rivi in rivit:
		for sarake in range(sarake_nro, sarake_nro + 3):
			nelio.append(rivi[sarake])

	for i in range(1, 10):
		maara = 0

		for ruutu in nelio:
			if ruutu == i:
				maara += 1

			if maara > 1:
				return False

	return True

# sudoku_oikein-funktio: Tarkistaa sudokun
def sudoku_oikein(sudoku: list):

	for i in range(0, 9):

		if rivi_oikein(sudoku, i) == False:
			return False

		if sarake_oikein(sudoku, i) == False:
			return False

	for i in range(0, 9, 3):
		for j in range(0,9, 3):
			if nelio_oikein(sudoku, i, j) == False:
				return False

	return True
	
# Testaus
if __name__ == '__main__':
	sudoku1 = [
		[9, 0, 0, 0, 8, 0, 3, 0, 0],
		[2, 0, 0, 2, 5, 0, 7, 0, 0],
		[0, 2, 0, 3, 0, 0, 0, 0, 4],
		[2, 9, 4, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 7, 3, 0, 5, 6, 0],
		[7, 0, 5, 0, 6, 0, 4, 0, 0],
		[0, 0, 7, 8, 0, 3, 9, 0, 0],
		[0, 0, 1, 0, 0, 0, 0, 0, 3],
		[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(sudoku_oikein(sudoku1))

	sudoku2 = [
		[2, 6, 7, 8, 3, 9, 5, 0, 4],
		[9, 0, 3, 5, 1, 0, 6, 0, 0],
		[0, 5, 1, 6, 0, 0, 8, 3, 9],
		[5, 1, 9, 0, 4, 6, 3, 2, 8],
		[8, 0, 2, 1, 0, 5, 7, 0, 6],
		[6, 7, 4, 3, 2, 0, 0, 0, 5],
		[0, 0, 0, 4, 5, 7, 2, 6, 3],
		[3, 2, 0, 0, 8, 0, 0, 5, 7],
		[7, 4, 5, 0, 0, 3, 9, 0, 1]
	]

	print(sudoku_oikein(sudoku2))
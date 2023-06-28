# tee ratkaisu tänne
def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
	sudoku[rivi_nro][sarake_nro] = luku

def tulosta(sudoku: list):
	rivi_nro = 0
	
	for rivi in sudoku:
		sarake_nro = 0

		if rivi_nro % 3 == 0 and rivi_nro != 0:
			print()
			rivi_nro = 0
		
		for sarake in rivi:
			if sarake_nro % 3 == 0 and sarake_nro != 0:
				print(" ", end="")
				sarake_nro = 0

			if sarake == 0:
				print("_ ", end="")
			else:
				print(f"{sarake} ", end="")

			sarake_nro += 1
		
		rivi_nro += 1

		print()

if __name__ == "__main__":
	sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
	]

	tulosta(sudoku)
	lisays(sudoku, 0, 0, 2)
	lisays(sudoku, 1, 2, 7)
	lisays(sudoku, 5, 7, 3)
	print()
	print("Kolme numeroa lisätty:")
	print()
	tulosta(sudoku)
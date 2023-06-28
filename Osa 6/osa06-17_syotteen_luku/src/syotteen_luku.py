# tee ratkaisu tänne
def lue(teksti: str, pienin: int, suurin: int):
	while True:
		try:
			syote = int(input(teksti))

			if syote > pienin and syote < suurin:
				return syote
		except ValueError:
			pass

		print(f"Syötteen on oltava kokonaisluku väliltä {pienin}...{suurin}")

if __name__ == '__main__':
	luku = lue("syötä luku: ", 5, 10)
	print("syötit luvun:", luku)
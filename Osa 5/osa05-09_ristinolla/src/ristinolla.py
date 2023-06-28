# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
	
	if x > 2 or x < 0 or y > 2 or y < 0:
		return False

	if lauta[y][x] == "":
		lauta[y][x] = nappula
		return True
	else:
		return False
	

if __name__ == "__main__":
	lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
	print(pelaa_siirto(lauta, 2, 0, "X"))
	print(lauta)
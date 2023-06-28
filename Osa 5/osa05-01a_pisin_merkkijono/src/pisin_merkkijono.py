# tee ratkaisu tänne
def pisin(merkkijonot: list):
	pisin_sana = ""

	for sana in merkkijonot:
		if len(sana) > len(pisin_sana):
			pisin_sana = sana
	
	return pisin_sana

if __name__ == "__main__":
	jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
	print(pisin(jonot))
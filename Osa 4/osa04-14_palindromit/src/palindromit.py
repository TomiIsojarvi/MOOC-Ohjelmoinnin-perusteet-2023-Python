# tee ratkaisu tänne
def palindromi(merkkijono: str) -> bool:
	pituus = len(merkkijono)
	samat = False

	for i in range(0, pituus):
		if merkkijono[i] == merkkijono[-i - 1]:
			samat = True
		else:
			samat = False
			break

	return samat

#------------------------------------------------------------------------------

while True:
	sana = input("anna palindromi: ")
	if palindromi(sana) == True:
		print(sana, "on palindromi!")
		break
	else:
		print("ei ollut palindromi")

# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!

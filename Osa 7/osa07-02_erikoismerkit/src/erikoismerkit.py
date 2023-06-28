# tee ratkaisu tänne
import string

def jaa_merkkeihin(merkkijono: str):
	ascii = ""
	valimerkit = ""
	muut = ""
	
	for merkki in merkkijono:
		if merkki in string.ascii_letters:
			ascii += merkki
		elif merkki in string.punctuation:
			valimerkit += merkki
		else:
			muut += merkki

	return (ascii, valimerkit, muut)

if __name__ == '__main__':
	osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
	print(osat[0])
	print(osat[1])
	print(osat[2])
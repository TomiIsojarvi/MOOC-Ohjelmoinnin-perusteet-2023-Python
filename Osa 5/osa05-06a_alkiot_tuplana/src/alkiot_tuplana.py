# tee ratkaisu tänne

def tuplaa_alkiot(luvut: list):
	uudet_luvut = []

	for luku in luvut:
		uudet_luvut.append(luku * 2)

	return uudet_luvut

if __name__ == "__main__":
	luvut = [2, 4, 5, 3, 11, -4]
	tuplaluvut = tuplaa_alkiot(luvut)
	print("alkuperäinen:", luvut)
	print("tuplattu:", tuplaluvut)
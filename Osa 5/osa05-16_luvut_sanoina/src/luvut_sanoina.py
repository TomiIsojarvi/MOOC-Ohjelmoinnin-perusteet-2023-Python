# tee ratkaisu tänne

def lukukirja():
	luvut = {0:"nolla", 1:"yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", \
		6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän",10:"kymmenen"}

	for luku in range(11, 20):
		luvut[luku] = luvut[luku - 10] + "toista"

	for i in range(2, 10):
		for j in range(0, 10):
			if j == 0:
				luvut[i * 10] = luvut[i] + "kymmentä"
			else:
				luvut[i * 10 + j] = luvut[i] + "kymmentä" + luvut[j]

	return luvut
	

#if __name__ == "__main__":
#	luvut = lukukirja()
#	print(luvut[2])
#	print(luvut[11])
#	print(luvut[45])
#	print(luvut[99])
#	print(luvut[0])
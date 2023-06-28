# tee ratkaisu tänne
def histogrammi(merkkijono):
	ryhmat = {}

	for kirjain in merkkijono:
		if kirjain not in ryhmat:
			ryhmat[kirjain] = 0
		ryhmat[kirjain] += 1

	for kirjain in ryhmat:
		print(kirjain, end=" ")

		for i in range(0, ryhmat[kirjain]):
			print("*", end="")

		print()

#histogrammi("saippuakauppias")
# tee ratkaisu tänne
def kumpi_voitti(pelilauta: list):
	pelaaja1 = 0
	pelaaja2 = 0

	for rivi in pelilauta:
		for sarake in rivi:
			if sarake == 1:
				pelaaja1 += 1
			elif sarake == 2:
				pelaaja2 += 1
			else:
				continue

	if pelaaja1 > pelaaja2:
		return 1
	elif pelaaja1 < pelaaja2:
		return 2
	else:
		return 0
# Tee ratkaisu tänne
def anagrammi(sana1, sana2):
	sana1 = sorted(sana1)
	sana2 = sorted(sana2)
	if (sana1 == sana2):
		return True
	else:
		return False

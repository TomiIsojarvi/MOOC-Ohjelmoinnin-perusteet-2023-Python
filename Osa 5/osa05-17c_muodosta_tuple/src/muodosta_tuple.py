# tee ratkaisu tänne
def tee_tuple(x: int, y: int, z: int):
	minimi = min(x, y, z)
	maksimi = max(x, y, z)
	summa = x + y + z

	return (minimi, maksimi, summa)

if __name__ == "__main__":
	print(tee_tuple(5, 3, -1))
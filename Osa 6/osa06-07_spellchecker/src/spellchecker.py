# tee ratkaisu tänne

def main():
	words = []
	text_words = []
	typo = False

	text = input("Write text: ")
	text_words = text.split()

	with open("wordlist.txt") as file:
		for row in file:
			row = row.strip()
			words.append(row)

	for word in text_words:
		lower = word.lower()

		if lower in words:
			print(f"{word} ", end="")
		else:
			print(f"*{word}* ", end="")

main()
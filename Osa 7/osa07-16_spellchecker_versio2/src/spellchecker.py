# tee ratkaisu tänne
from difflib import get_close_matches

def main():
	words = []
	text_words = []
	typos = []
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
			typos.append(word)
			
	print("\nkorjausehdotukset:")
	
	for typo_word in typos:
		recommended = []
		recommended = get_close_matches(typo_word, words)
		print(f"{typo_word}: ", end="")
		print(', '.join([item for item in recommended]) + '')

main()
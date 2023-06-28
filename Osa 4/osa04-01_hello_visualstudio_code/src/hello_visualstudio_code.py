# Kirjoita ratkaisu tähän

while True:
  editori = input("Editori: ")
  if editori.lower() == "visual studio code":
    print("loistava valinta!")
    break
  elif editori.lower() == "word" or editori.lower() == "notepad":
    print("surkea")
  else:
    print("ei ole hyvä")
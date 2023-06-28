# tee ratkaisu tänne

def lisaa_merkinta():
  with open("paivakirja.txt", "a") as tiedosto:
    merkinta = input("Anna merkintä: ")
    merkinta += '\n'

    tiedosto.write(merkinta)
    print("Päiväkirja tallennettu")

def lue_merkinnat():
  with open("paivakirja.txt", "r") as tiedosto:
    print("Merkinnät:")

    for rivi in tiedosto:
      print(rivi, end="")

def main():
  while True:
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    valinta = int(input("Valinta: "))

    if valinta == 0:
      print("Heippa!")
      break
    elif valinta == 1:
      lisaa_merkinta()
    else:
      lue_merkinnat()

main()

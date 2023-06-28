# Kirjoita ratkaisu tähän
lista = []

while True:
  luku = int(input("Anna luku: "))

  if luku == 0:
    print("Moi!")
    break

  lista.append(luku)
  jarjestetty = sorted(lista)

  print("Lista:", lista)
  print("Järjestettynä:", jarjestetty)

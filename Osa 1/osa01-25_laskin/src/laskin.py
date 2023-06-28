luku1 = int(input("Luku 1: "))
luku2 = int(input("luku 2: "))
komento = input("Komento: ")

# En rupea tässä säilyttämään boolean arvoja erillisiin muuttujiin, vaan mennään tällä:
if komento == "summa":
    print(f"{luku1} + {luku2} = {luku1 + luku2}")

if komento == "erotus":
    print(f"{luku1} - {luku2} = {luku1 - luku2}")

if komento == "tulo":
    print(f"{luku1} * {luku2} = {luku1 * luku2}")
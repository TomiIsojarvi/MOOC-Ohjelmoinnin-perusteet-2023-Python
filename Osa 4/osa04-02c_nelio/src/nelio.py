# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):
    merkki = "*"

    if len(merkkijono) != 0:
        merkki = merkkijono[0]
    
    print(merkki * leveys)


def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 0

    while i < koko:
        viiva(koko, merkki)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")

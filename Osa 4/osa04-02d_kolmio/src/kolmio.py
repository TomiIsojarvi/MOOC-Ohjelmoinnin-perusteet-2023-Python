# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(leveys, merkkijono):
    merkki = "*"

    if len(merkkijono) != 0:
        merkki = merkkijono[0]
    
    print(merkki * leveys)

def kolmio(koko):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 1
    while i <= koko:
        viiva(i, "#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kolmio(5)

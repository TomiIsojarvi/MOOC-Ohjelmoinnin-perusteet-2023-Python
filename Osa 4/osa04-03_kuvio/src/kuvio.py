# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
def viiva(leveys, merkkijono):
    merkki = "*"

    if len(merkkijono) != 0:
        merkki = merkkijono[0]
    
    print(merkki * leveys)

def kolmio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 1
    while i <= koko:
        viiva(i, merkki)
        i += 1

def suorakulmio(koko1, koko2, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    i = 0

    while i < koko2:
        viiva(koko1, merkki)
        i += 1

def kuvio(koko1, merkki1, koko2, merkki2):
    kolmio(koko1, merkki1)
    suorakulmio(koko1, koko2, merkki2)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")

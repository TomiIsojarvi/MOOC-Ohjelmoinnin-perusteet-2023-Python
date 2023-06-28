# tee ratkaisu tänne
def viiva(leveys, merkkijono):
    merkki = "*"

    if len(merkkijono) != 0:
        merkki = merkkijono[0]
    
    print(merkki * leveys)


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "x")

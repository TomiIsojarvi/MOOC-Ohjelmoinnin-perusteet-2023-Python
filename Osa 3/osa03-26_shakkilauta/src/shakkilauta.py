def shakkilauta(koko):
    i = 1
    j = 1
    merkki = "1"
    merkkijono = ""

    while i <= koko:
        merkkijono = ""
        while j <= koko:
            if i % 2 == 0:
                if j % 2 == 0:
                    merkki = "1"
                else:
                    merkki = "0"
            else:
                if j % 2 == 0:
                    merkki = "0"
                else:
                    merkki = "1"

            merkkijono += merkki
            j += 1

        print(merkkijono)
        i += 1
        j = 1

    

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)
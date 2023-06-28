# tee ratkaisu tänne
def joulukuusi(koko):
    print("joulukuusi!")
    leveys = koko * 2 - 1
    merkkijono = ""
    i = 1
    j = 1
    tyhjat = 0

    while i <= koko:
        # Kuinka paljon tyhjää molemmilla puolilla
        tyhjat = (leveys - j) // 2
        merkkijono += " " * tyhjat
        merkkijono += "*" * j
        merkkijono += " " * tyhjat
        print(merkkijono)
        merkkijono = ""
        i += 1
        j += 2

    tyhjat = (leveys - 1) // 2
    merkkijono = " " * tyhjat
    merkkijono += "*"
    print(merkkijono)


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)
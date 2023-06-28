def nelio(sana, koko):
    i = 0
    j = 0
    merkki = sana[0]
    merkkijono = ""
    paikka = 0

    while i < koko:
        merkkijono = ""
        while j < koko:
            if paikka >= len(sana):
                paikka = 0

            merkkijono += sana[paikka]
            j += 1
            paikka += 1

        print(merkkijono)
        i += 1
        j = 0

if __name__ == "__main__":
    nelio("ab", 3)
    print()
    nelio("aybabtu", 5)
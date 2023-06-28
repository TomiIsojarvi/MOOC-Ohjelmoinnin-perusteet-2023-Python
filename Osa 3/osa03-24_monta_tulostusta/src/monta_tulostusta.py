def tulosta_monesti(merkkijono, kertaa):
    i = 0

    while i < kertaa:
        print(merkkijono)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)
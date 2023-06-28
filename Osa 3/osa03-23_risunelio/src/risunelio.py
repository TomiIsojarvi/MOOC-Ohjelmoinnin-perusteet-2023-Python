def risunelio(koko):
    i = 0

    while i < koko:
        print("#" * koko)
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
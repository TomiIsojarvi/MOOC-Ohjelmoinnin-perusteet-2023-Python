# tee ratkaisu tänne
def samat(sana, index1, index2):
    if index1 >= len(sana) or index2 >= len(sana):
        return False

    if sana[index1] == sana[index2]:
        return True
    else:
        return False

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 2)) 
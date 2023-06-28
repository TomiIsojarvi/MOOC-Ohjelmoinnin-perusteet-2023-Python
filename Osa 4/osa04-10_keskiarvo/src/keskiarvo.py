# tee ratkaisu tänne
def keskiarvo(lista: list):
    pituus = len(lista)
    summa = sum(lista)
    return summa / pituus

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = keskiarvo(lista) 
    print(tulos)

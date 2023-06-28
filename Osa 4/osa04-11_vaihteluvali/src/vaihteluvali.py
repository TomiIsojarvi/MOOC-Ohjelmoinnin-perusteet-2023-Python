# tee ratkaisu tänne
def vaihteluvali(lista: list):
    maksimi = max(lista)
    minimi = min(lista)
    return maksimi - minimi

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)
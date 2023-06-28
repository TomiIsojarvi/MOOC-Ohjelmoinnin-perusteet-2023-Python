# tee ratkaisu tänne
def eka_sana(lause):
    alku = 0
    loppu = lause.find(" ")
    return lause[alku:loppu]

def toka_sana(lause):
    alku = lause.find(" ")
    osalause = lause[alku + 1:]
    alku = 0
    loppu = osalause.find(" ")
    if loppu == -1:
        return osalause[alku:]
    else:
        return osalause[alku:loppu]

def vika_sana(lause):
    alku = lause.rfind(" ")
    return lause[alku + 1:]

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause)) 
    print(vika_sana(lause))
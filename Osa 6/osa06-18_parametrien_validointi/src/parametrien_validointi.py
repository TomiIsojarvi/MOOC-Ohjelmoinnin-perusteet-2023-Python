# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):
  if nimi == "":
    raise ValueError("Nimi on tyhjä merkkijono")
  if len(nimi.split()) < 2:
    raise ValueError("Nimen tulee koostua yli kahdesta sanasta")
  if len(nimi) > 40:
    raise ValueError("Nimi liian pitkä (yli 40 merkkiä)")
  if ika < 0:
    raise ValueError("Ikä negatiivinen")
  if ika > 150:
    raise ValueError("Ikä suurempi kuin 150")

  return (nimi, ika)

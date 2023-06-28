kustannukset = 0

unicafe_kerrat = int(input("Montako kertaa viikossa syöt Unicafessa? "))
unicafe_hinta = float(input("Unicafe-lounaan hinta? "))
unicafe = unicafe_hinta * unicafe_kerrat
kustannukset += unicafe

ruokaostokset = float(input("Paljonko käytät viikossa ruokaostoksiin? "))
kustannukset += ruokaostokset

print("Kustannukset keskimäärin:")
print(f"Päivässä {kustannukset / 7} euroa")
print(f"Viikossa {kustannukset} euroa")
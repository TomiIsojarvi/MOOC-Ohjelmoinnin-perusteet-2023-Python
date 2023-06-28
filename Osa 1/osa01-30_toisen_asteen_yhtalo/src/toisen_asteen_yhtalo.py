# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

a = float(input("Anna a: "))
b = float(input("Anna b: "))
c = float(input("Anna c: "))

x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print("Juuret ovat", x1, "ja", x2)
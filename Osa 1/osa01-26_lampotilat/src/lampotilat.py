fahrenheit = float(input("Anna lämpötila (F): "))

celsius = (fahrenheit - 32) / 1.8

print(fahrenheit, "fahrenheit-astetta on", celsius, "celsius-astetta")

if celsius < 0:
    print("Paleltaa!")
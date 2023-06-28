luku = int(input("Luku: "))

if luku % 3 == 0 and luku % 5 != 0:
    print("Fizz")
elif luku % 3 != 0 and luku % 5 == 0:
    print("Buzz")
elif luku % 3 == 0 and luku % 5 == 0:
    print("FizzBuzz")
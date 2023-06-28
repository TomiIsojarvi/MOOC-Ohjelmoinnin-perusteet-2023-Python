salasana = input("Salasana: ")

while True:
    ss = input("Toista salasana: ")

    if ss == salasana:
        print("Käyttäjätunnus luotu!")
        break
    
    print("Ei ollut sama!")
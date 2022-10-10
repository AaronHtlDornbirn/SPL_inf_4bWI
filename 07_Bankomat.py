endless = True
Konto = 0

print("Was wollen Sie machen?")

print("1. Einzahlen")
print("2. Abheben")
print("3. Kontostand")
print("4. Beenden")

while endless:
    selection = int(input())
    if selection == 1:
        print("Wie viel möchten Sie einzahlen?")
        einzahlen = int(input())
        Konto += einzahlen
        print("Sie haben "+ str(einzahlen) +" Euro eingezahlt.")
    elif selection == 2:
        print("Wie viel möchten Sie abheben?")
        abheben = int(input())
        Konto -= abheben
        print("Sie haben "+ str(abheben) +" Euro abgehoben.")
        if Konto < 0:
            print("Sie befinden sich im Minus mit: "+ str(Konto) +" Euro.")
    elif selection == 3:
        print("Ihr Kontostand beträgt "+ str(Konto) +" Euro.")  
    elif selection == 4:
        break   
    else:
        print("Die von Ihnen eingegebene Zahl existiert nicht!")

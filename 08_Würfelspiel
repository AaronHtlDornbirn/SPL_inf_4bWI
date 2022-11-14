import random
random = random.Random()

endless = True
mypoints = 0
compoints = 0

print("Was wollen Sie machen?")

print("1. Würfeln")
print("2. Gegner Würfeln lassen")
print("3. Auflösen")
print("4. Punkte zurücksetzen")
print("5. Beenden")


while endless:
    selection = int(input())
    if selection == 1:
        print("Sie Würfeln!")
        mynum = random.randint(6,36)
        mypoints += mynum       
        print("Sie haben "+ str(mypoints) +" Punkte gewürfelt.")
    elif selection == 2:
        print("Computer Würfelt!")
        comnum = random.randint(6,36)
        compoints += comnum       
        #print("Computer hat "+ str(compoints) +" Punkte gewürfelt.")
    elif selection == 3:
        print("Auflösung:")
        if mypoints > compoints:
            print("Du hast gewonnen mit "+ str(mypoints) +" Punkten.")
        elif mypoints == compoints:
            print("Unentschieden, ihr habt beide: "+ str(mypoints) +" Punkte.")
        else:
            print("Du hast verloren mit "+ str(mypoints) +" Punkten.")        
        print("Meine Punkte: "+ str(mypoints))
        print("Computer Punkte: "+ str(compoints))
    elif selection == 4:
        print("Die Punkte wurden zurückgesetzt.")
        mypoints = 0
        compoints = 0
        print("Meine Punkte: "+ str(mypoints))
        print("Computer Punkte: "+ str(compoints))
    elif selection == 5:
        break    
    else:
        print("Die von Ihnen eingegebene Zahl existiert nicht!")

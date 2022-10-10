from ast import If
import random

random = random.Random()
randnr1 = random.randint(1,100)
randnr2 = random.randint(1,100)

print(randnr1)
print(randnr2)

if(randnr1 < randnr2 & randnr1 < 50):
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
elif(randnr1 < 30 | randnr2 < 30):
    print("Eine der beiden ist kleiner als 30")
elif(randnr1 < 50 & randnr2 != 50):
    print("Erste Zahl klein, zweite kein 50iger")
else:
    print("keine Besonderheiten")
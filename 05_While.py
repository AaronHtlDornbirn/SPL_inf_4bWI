import random

random = random.Random()
randomnumber = 0
summe = 0

while(randomnumber != 15 | randomnumber != 25):
    randomnumber = random.randint(10,30)
    summe += randomnumber

print(summe)
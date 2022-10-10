import random

random = random.Random()
randnr1 = random.randint(1,100)

print(randnr1)

if(randnr1 < 20):
    print("mini")
elif(randnr1 <= 50):
    print("medium")
else:
    print("large")
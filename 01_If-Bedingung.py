import random

random = random.Random()
randomnumber01 = random.randint(1,100)

print(randomnumber01)

if(randomnumber01 < 20):
    print("mini")
if(randomnumber01 <= 50):
    print("medium")
else:
    print("large")
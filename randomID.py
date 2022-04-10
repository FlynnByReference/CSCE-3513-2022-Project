import random

randomR1 = random.randint(1,5)
randomR2 = random.randint(1,5)
if (randomR1 == randomR2):
    while(randomR1 == randomR2):
        randomR2 = random.randint(1,5)
        
randomR1 = str(randomR1)
randomR2 = str(randomR2)
print("R1: " + randomR1)
print("R2: " + randomR2)


randomG1 = random.randint(6, 10)
randomG2 = random.randint(6, 10)
if (randomG1 == randomG2):
    while(randomG1 == randomG2):
        randomG2 = random.randint(6, 10)
        
randomG1 = str(randomG1)
randomG2 = str(randomG2)
print("G1: " + randomG1)
print("G2: " + randomG2)
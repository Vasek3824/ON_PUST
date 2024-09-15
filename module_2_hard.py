import random

def parol():
    cod = random.randint(3, 20)
    for i in range(1, 21):
        for j in range(i+1, 21):
            if cod % (i + j) == 0:
                if i >= j:
                    break
                print(f'{i}{j}', end ='')
parol()

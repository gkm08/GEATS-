import random

def guess_number():
    secretnum = random.randint(1,100)
    life = 6
    life -= 1
    while True :
        print("게임 오버", guess_number()

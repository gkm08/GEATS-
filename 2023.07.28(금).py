#백준(평균)
#n = int(input())
#m = list(map(int, input().split()))
#max = max(m)

#print(m)
#l = []
#for i in m:
 #   l.append(i / max * 100)

#print(l)
#avg = sum(l) / n
#print(avg)

#길이재기
#s = input()
#i = int(input())

#print(s[i-1])

#문자열
#t = int(input())
#for i in range(t):
 #   s = input()
 #   print(s[0]+s[-1])


import random


def save_highscore(hightscore):
    with open("highscore.txt", "w") as file:
        file.write(str(hightscore))

def load_highscore():
    with open("highscore.txt", "r") as file:
        return int(file.read())


def play_game():
    print("게임을 시작합니다 1부터 100중 아무숫자를 쓰시오")
    secrets_number = random.randint(1, 10)
    attempts = 0
    highscore = load_highscore()

    while True:
        try:
            guess = int(input("숫자를 입력하시오"))
        except ValueError:
            print("유효한 숫자를 입력하시오")
            continue
        attempts += 1

        if guess < secrets_number:
            print("작습니다")
        elif guess > secrets_number:
            print("큽니다")
        else:
            print("맞췄습니다", attempts)
            if attempts < highscore:
                highscore = attempts
                print("최고기록을 갱신했습니다")
                save_highscore(highscore)
            break

play_game()
import turtle
import random

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    # 각 단어의 앞뒤 공백 제거
    words = [word.strip() for word in words]
    return words

def select_random_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += "_"
        else:
            displayed_word += "_"
    return displayed_word

def get_user_input():
    user_input = input("알파벳을 입력하세요: ")
    return user_input.lower()

def draw_hangman(attempts):
    if attempts == 6:
        # 기둥 그리기
        turtle.penup()
        turtle.goto(-200, -300)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        turtle.forward(100)

    elif attempts == 5:
        # 얼굴 그리기
        turtle.penup()
        turtle.goto(70, -30)
        turtle.pendown()
        turtle.circle(30)

    elif attempts == 4:
        # 몸통 그리기
        turtle.penup()
        turtle.goto(100, -60)
        turtle.pendown()
        turtle.forward(100)

    elif attempts == 3:
        # 왼팔 그리기
        turtle.penup()
        turtle.goto(100, -80)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(50)

    elif attempts == 2:
        # 오른팔 그리기
        turtle.penup()
        turtle.goto(100, -80)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(50)

    elif attempts == 1:
        # 왼다리 그리기
        turtle.penup()
        turtle.goto(100, -160)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(50)

    elif attempts == 0:
        # 오른다리 그리기
        turtle.penup()
        turtle.goto(100, -160)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(50)


def play_hangman():
    file_path = "words.txt"  # 단어가 들어있는 파일 경로
    words = read_words_from_file(file_path)
    word = select_random_word(words)
    guessed_letters = []
    attempts = 7

    print("행맨 게임을 시작합니다!")

    while True:
        draw_hangman(attempts)
        turtle.update()

        print(f"남은 목숨: {attempts}")
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if "_" not in displayed_word:
            print("축하합니다! 단어를 맞추셨습니다!")
            break

        if attempts == 0:
            print(f"실패! 정답은 {word}입니다")
            break

        user_input = get_user_input()

        if len(user_input) != 1 or not user_input.isalpha():
            print("올바른 알파벳을 입력하세요!")
            continue

        if user_input in guessed_letters:
            print("이미 시도한 알파벳입니다!")
            continue

        guessed_letters.append(user_input)

        if user_input not in word:
            attempts -= 1
            print("틀렸습니다!")

    turtle.mainloop()

play_hangman()










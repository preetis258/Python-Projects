import random


def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_num:
            print("too high! Guess again.\t")
        elif guess < random_num:
            print("too low! Guess again.\t")
    print(f"yayy! You guessed the number {random_num} correctly!")

guess(20)
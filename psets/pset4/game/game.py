import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

rand_num = random.choice(range(1, n + 1))

while True:
    try:
        guess = int(input("Guess: "))
        if guess < rand_num:
            print("Too small!")
            continue
        elif guess > rand_num:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except ValueError:
        pass

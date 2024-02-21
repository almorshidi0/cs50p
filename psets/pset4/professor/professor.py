import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        fail = 0
        while fail < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                fail += 1
                continue
            if guess == x + y:
                score += 1
                fail = 0
                break
            elif fail < 2:
                print("EEE")
                fail += 1
            else:
                fail += 1
        if fail == 3:
            print(f"{x} + {y} = {x + y}")
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    start = 0 if level == 1 else pow(10, level - 1)
    end = pow(10, level)
    return random.choice(range(start, end))

if __name__ == "__main__":
    main()

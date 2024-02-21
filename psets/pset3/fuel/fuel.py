result = 0
while True:
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        pass
    else:
        if x <= y:
            try:
                result = round((x / y) * 100)
                break
            except ZeroDivisionError:
                pass
if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result}%")

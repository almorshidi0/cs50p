def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError
    if x <= y:
            return round((x / y) * 100)
    elif y == 0:
        raise ZeroDivisionError
    else:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

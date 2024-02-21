names = []
while True:
    try:
        item = input().strip()
        names.append(item)
    except EOFError:
        break
length = len(names)
if length == 1:
    print("Adieu, adieu, to", names[0])
elif length == 2:
    print("Adieu, adieu, to",names[0] , "and", names[1])
else:
    print("Adieu, adieu, to ", end="")
    index = 0
    while index < length:
        print(names[index], end="")
        if index < length - 2:
            print(", ", end="")
        elif index == length - 2:
            print(", and ", end="")
        else:
            print()
        index += 1

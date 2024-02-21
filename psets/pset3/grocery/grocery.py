grocery = {}
while True:
    try:
        item = input().strip().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        grocery = dict(sorted(list(grocery.items())))
        for item in grocery:
            print(grocery[item], item)
        break

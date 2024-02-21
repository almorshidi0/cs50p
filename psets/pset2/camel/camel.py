camelCase = input("camelCase: ")
snake_case = ""
for character in camelCase:
    if character.isupper():
        character = character.lower()
        snake_case += "_"
    snake_case += character
print(f"snake_case: {snake_case}")

def main():
    user_input = input("Type something: ")
    user_input = make_face(user_input)
    print(user_input)

def make_face(str_input):
    str_input = str_input.replace(":)", "\N{slightly smiling face}")
    str_input = str_input.replace(":(", "\N{slightly frowning face}")
    return str_input

main()

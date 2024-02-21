import validators

input_string = input("What's your email address? ")
print("Valid" if validators.email(input_string) else "Invalid")

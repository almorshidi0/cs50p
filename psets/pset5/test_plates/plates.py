def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (not (2 <= len(s) <= 6)) or (not s.isalnum()) or s[0].isdecimal():
        return False
    elif s.isalpha():
        return True
    else:
        while s[0].isalpha():
            s = s[1:]
        if s[0] == "0" or (not s.isdecimal()):
            return False
        else:
            return True

if __name__ == "__main__":
    main()

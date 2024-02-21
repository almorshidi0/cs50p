def main():
    word = input("Input: ")
    word = shorten(word)
    print("Output:", word)

def shorten(word):
    for c in word:
        if c in "aeiouAEIOU":
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()

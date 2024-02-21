word = input("Input: ")
for c in word:
    if c in "aeiouAEIOU":
        word = word.replace(c, "")
print("Output:", word)

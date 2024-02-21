import emoji

in_str = input("Input: ")
out_emoji = emoji.emojize(in_str, language="en")

if out_emoji == in_str:
    out_emoji = emoji.emojize(in_str, language="alias")

print(out_emoji)

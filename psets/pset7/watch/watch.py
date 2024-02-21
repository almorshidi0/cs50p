import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    regex = r"src=\"(?:https?://(?:www\.)?)?youtube.com/embed/(\w*)"
    match = re.search(regex, s)
    if match:
        url = f"https://youtu.be/{match.group(1)}"
        return url
    else:
        return None

if __name__ == "__main__":
    main()

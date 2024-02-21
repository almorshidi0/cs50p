import sys
import pyfiglet as figlet
if len(sys.argv) == 1:
    f=figlet.Figlet()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.Figlet().getFonts():
            f = figlet.Figlet(font=sys.argv[2])
        else:
            sys.exit(1)
    else:
        sys.exit(1)
else:
    sys.exit(1)

user_input = input("Input: ")
print("Output: ", f.renderText(user_input), sep="\n")

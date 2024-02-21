import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".py")):
    sys.exit("Not a Python file")

try:
    file_content = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

n_lines = 0

for line in file_content.readlines():
    line = line.lstrip()
    if not(line.startswith("#") or line.isspace() or line == ""):
        n_lines += 1

print(n_lines)

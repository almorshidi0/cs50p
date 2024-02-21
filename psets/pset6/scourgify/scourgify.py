import csv
import sys

lines = [["first", "last", "house"]]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")

with open(sys.argv[1]) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        try:
            last, first = row[0].replace("\"", "").split(", ")
            house = row[1]
        except ValueError:
            pass
        else:
            lines.append([first, last, house])

with open(sys.argv[2], "w") as new_file:
    csv_writer = csv.writer(new_file)
    for line in lines:
        csv_writer.writerow(line)

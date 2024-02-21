from tabulate import tabulate
import csv
import sys

table_headers = []
menu = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")
with open(sys.argv[1]) as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        menu.append([row[0], row[1], row[2]])

print(tabulate(menu[1:], headers=menu[0], tablefmt = "grid"))

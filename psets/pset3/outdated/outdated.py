months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip().casefold().title()
    try:
        month, day, year = date.split(" ")
        if day.endswith(","):
            day = day.removesuffix(",")
        else:
            continue
        day = int(day)
        year = int(year)
        if (0 < day <= 31) and (month in months) and (0 < year):
            break
        else:
            continue
    except ValueError:
        pass
    try:
        month, day, year = date.split("/")
        day = int(day)
        month = int(month)
        year = int(year)
        if (0 < day <= 31) and (0 < month <= 12) and (0 < year):
            break
        else:
            continue
    except ValueError:
        pass
if month in months:
    date = f"{year:0>2}-{(months.index(month) + 1):0>2}-{day:0>2}"
else:
    date = f"{year:0>2}-{month:0>2}-{day:0>2}"

print(date)

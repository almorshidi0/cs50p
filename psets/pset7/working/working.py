import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = r"^(\d{1,2})\:?(\d{1,2})? (\w{2}) to (\d{1,2})\:?(\d{1,2})? (\w{2})"
    matches = re.search(regex, s)
    if not matches:
        raise(ValueError)
    start_hr, start_min, start_period, end_hr, end_min, end_period = matches.groups()
    if matches:
        start_hr = int(start_hr)
        start_min = int(start_min) if start_min else 0
        end_hr = int(end_hr)
        end_min = int(end_min) if end_min else 0
    else:
        raise(ValueError)

    if not ((start_hr in range(1,13)) and (end_hr in range(1,13))):
        raise(ValueError)
    elif not ((start_min in range(0, 60)) and (end_min in range(0, 60))):
        raise(ValueError)

    return format(start_hr, start_min, start_period, end_hr, end_min, end_period)

def format(start_hr, start_min, start_period, end_hr, end_min, end_period):
    if start_period == "AM":
        if start_hr == 12:
            start_hr = 0
        if start_hr < 10:
            start_hr = f"0{start_hr}"
        else:
            start_hr = f"{start_hr}"
    elif start_period == "PM":
        if not (start_hr == 12):
            start_hr += 12
        start_hr = f"{start_hr}"
    if start_min < 10:
        start_min = f"0{start_min}"
    else:
        start_min = f"{start_min}"

    if end_period == "AM":
        if end_hr == 12:
            end_hr = 0
        if end_hr < 10:
            end_hr = f"0{end_hr}"
        else:
            end_hr = f"{end_hr}"
    elif end_period == "PM":
        if not (end_hr == 12):
            end_hr += 12
        end_hr = f"{end_hr}"
    if end_min < 10:
        end_min = f"0{end_min}"
    else:
        end_min = f"{end_min}"

    return f"{start_hr}:{start_min} to {end_hr}:{end_min}"

if __name__ == "__main__":
    main()

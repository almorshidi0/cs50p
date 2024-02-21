from datetime import date
from inflect import engine
import sys


def main():
    birth_date = get_birth_date()
    minutes_old = calc_minutes(birth_date)
    output_str = format_output(minutes_old)
    print(output_str)


def get_birth_date():
    birth_date = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth_date)
        return birth_date
    except ValueError:
        sys.exit("Invalid date")

def calc_minutes(birth_date):
    delta = date.today() - birth_date
    return int(delta.total_seconds() / 60)

def format_output(minutes_old):
    minutes_in_words = engine().number_to_words(minutes_old, andword="")
    minutes_in_words = minutes_in_words.capitalize()
    return f"{minutes_in_words} minutes"


if __name__ == "__main__":
    main()

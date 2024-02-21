fruits = [
    {"name" : "apple", "cal" : "130"},
    {"name" : "avocado", "cal" : "50"},
    {"name" : "banana", "cal" : "110"},
    {"name" : "cantaloupe", "cal" : "50"},
    {"name" : "grapefruit", "cal" : "60"},
    {"name" : "grapes", "cal" : "90"},
    {"name" : "honeydew melon", "cal" : "50"},
    {"name" : "kiwifruit", "cal" : "90"},
    {"name" : "lemon", "cal" : "15"},
    {"name" : "lime", "cal" : "20"},
    {"name" : "nectarine", "cal" : "60"},
    {"name" : "orange", "cal" : "80"},
    {"name" : "peach", "cal" : "60"},
    {"name" : "pear", "cal" : "100"},
    {"name" : "pinneapple", "cal" : "50"},
    {"name" : "plums", "cal" : "70"},
    {"name" : "strawberries", "cal" : "50"},
    {"name" : "sweet cherries", "cal" : "100"},
    {"name" : "tangerine", "cal" : "50"},
    {"name" : "watermelon", "cal" : "80"}
]

in_fruit = input("Item: ").casefold().strip()
for fruit in fruits:
    if fruit["name"] == in_fruit:
        print("Calories:", fruit["cal"])

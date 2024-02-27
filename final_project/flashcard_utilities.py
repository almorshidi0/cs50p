from re import match
import sys
import os
from prettytable import PrettyTable
from colorama import Fore, Style  # Import colorama modules for text coloring

from flashcard_class import Flashcard

class BackToMainMenu(Exception):
    pass

# Color codes for colorama
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

PROGRAM_WELCOME_STATEMENT = f"""
{Fore.GREEN}===== Flashcard Review Program ====={Style.RESET_ALL}
{Fore.GREEN}Welcome to an interactive learning experience!{Style.RESET_ALL}
-------------------------------------------------------

{Fore.YELLOW}Important Notes:{Style.RESET_ALL}
    {Fore.YELLOW}Menu Navigation:{Style.RESET_ALL}
        - Each menu element is assigned a number.
        - Choose an element by typing its number in the 'Your choice: ' prompt.

    {Fore.YELLOW}Deck Naming Guidelines:{Style.RESET_ALL}
        - Deck names must be unique.
        - Use only English letters, numbers, and underscores '_'.
        - Deck names must start with an English letter or an underscore '_'.

    {Fore.YELLOW}Flashcard (Front, Back) Input Rules:{Style.RESET_ALL}
        - Only use the letters found on common English keyboards to avoid unidentified behavior.
        - Avoid using the '|' character in any inputs; it will be automatically removed.

{Fore.YELLOW}Important Commands:{Style.RESET_ALL}
    - {Fore.GREEN}':q'{Style.RESET_ALL} or {Fore.GREEN}Ctrl + C{Style.RESET_ALL} - Exit the program at any time.
    - {Fore.GREEN}':m'{Style.RESET_ALL} - Go back to the main menu at any time.
    
{Fore.YELLOW}Notes:{Style.RESET_ALL}
    - The ':' character is necessary for these commands to work.
    - If the ':' character isn't typed explicitly, the input
      won't be considered a command and will be handled accordingly.
"""

MAIN_MENU_STATEMENT = f"""
{GREEN}Main Menu:{RESET}
    
    1. Add Deck.
    2. Edit Deck.
    3. Review Deck.
    4. Explore Decks.
    5. Statistics.
    6. Help.
    7. Quit.
"""

EDIT_DECK_MENU_STATEMENT = f"""
{YELLOW}Action:{RESET}

    1. Edit Deck name.
    2. Add Flashcard.
    3. Edit Flashcard.
    4. Choose another deck to edit.
    5. Back to main menu.
"""

COMMAND_LIST = [f"{GREEN}:q{RESET}", f"{GREEN}:m{RESET}"]

DECK_COLLECTION_PATH = "./collection/"


def get_deck_file_path(deck_name):
    """
    Returns the file path for a deck with the given name.

    Parameters:
    - deck_name (str): The name of the deck.

    Returns:
    str: The file path for the deck.
    """
    return f"{DECK_COLLECTION_PATH}fc_{deck_name}.txt"


def is_valid_deck_name_format(deck_name):
    """
    Checks if the provided deck name follows the valid format.

    Parameters:
    - deck_name (str): The name of the deck.

    Returns:
    bool: True if the deck name is in the valid format, False otherwise.
    """
    regex = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(match(regex, deck_name))


def is_existing_deck_name(deck_name):
    """
    Checks if a deck with the provided name already exists.

    Parameters:
    - deck_name (str): The name of the deck.

    Returns:
    bool: True if a deck with the given name exists, False otherwise.
    """
    return deck_name in list_existing_decks()


def is_valid_card_data_format(card_data):
    """
    Checks if the provided flashcard data follows the valid format.

    Parameters:
    - card_data (str): The flashcard data to be validated.

    Returns:
    bool: True if the flashcard data is in the valid format, False otherwise.
    """
    regex = r"^[A-Za-z0-9,.\s_!@#\$%\^&\*()-+=<>?/;:'\"[{}\]\|`~]*$"
    return bool(match(regex, card_data))


def is_existing_card_front_text(deck_name, card_front_text):
    """
    Checks if a flashcard with the provided front text already exists in a deck.

    Parameters:
    - deck_name (str): The name of the deck.
    - card_front_text (str): The front text of the flashcard.

    Returns:
    bool: True if a flashcard with the given front text exists in the deck, False otherwise.
    """
    existing_cards = list_existing_cards(deck_name)
    if existing_cards:
        for card in existing_cards:
            if card.front_text == card_front_text:
                return True
    return False


def get_choice(choice_list):
    """
    Get user input for menu choices.

    Parameters:
    - choice_list (list): List of valid choices.

    Returns:
    str: User's selected choice.
    """
    choice_list.extend(COMMAND_LIST)
    while True:
        choice = input(f"{Fore.YELLOW}Your choice:{Style.RESET_ALL} ").strip()  # Added color to the prompt
        exit_program_check(choice.lower())
        back_to_main_menu_check(choice.lower())
        try:
            choice = int(choice)
            
        except ValueError:
            pass
        
        else:
            if choice in choice_list:
                return choice
            else:
                print("Invalid choice. Try again!\n")


def get_deck_name():
    """
    Get user input for a new deck name.

    Returns:
    str: User's input for the new deck name.
    """
    while True:
        deck_name = input(f"{Fore.YELLOW}Deck Name:{Style.RESET_ALL} ").strip().lower()  # Added color to the prompt
        exit_program_check(deck_name)
        back_to_main_menu_check(deck_name)
        if not is_valid_deck_name_format(deck_name):
            print(f"{Fore.RED}Invalid deck name. Try again!\n{Style.RESET_ALL}")  # Added color to the error message
        elif is_existing_deck_name(deck_name):
            print(f"{Fore.RED}Invalid deck name. This deck name was used before. Try again!\n{Style.RESET_ALL}")  # Added color to the error message
        else:
            return deck_name


def get_card_front_text(deck_name):
    """
    Prompt the user to input the front text of a flashcard.

    Parameters:
    - deck_name (str): The name of the deck to which the flashcard belongs.

    Returns:
    str: The front text of the flashcard.
    """
    while True:
        card_front_text = input(f"{Fore.YELLOW}Front:{Style.RESET_ALL} ").strip().replace("|", "")
        exit_program_check(card_front_text)
        back_to_main_menu_check(card_front_text)
        if not is_valid_card_data_format(card_front_text):
            print(f"{Fore.RED}Invalid card front_text. Try again!\n{Style.RESET_ALL}")  # Added color to the error message
        elif is_existing_card_front_text(deck_name, card_front_text):
            print(f"{Fore.RED}Invalid card front_text. This card front_text was used before. Try again!\n{Style.RESET_ALL}")  # Added color to the error message
        else:
            return card_front_text


def get_card_back_text():
    """
    Prompt the user to input the back text of a flashcard.

    Returns:
    str: The back text of the flashcard.
    """
    while True:
        card_back_text = input(f"{Fore.CYAN}Back:{Style.RESET_ALL} ").strip()
        exit_program_check(card_back_text)
        back_to_main_menu_check(card_back_text)
        if not is_valid_card_data_format(card_back_text):
            print(f"{Fore.RED}Invalid card back_text. Try again!\n{Style.RESET_ALL}")
        else:
            return card_back_text


def list_existing_decks():
    """
    Retrieve a sorted list of existing deck names.

    Returns:
    list: A sorted list containing names of existing decks.
    """
    existing_decks = []
    for filename in os.listdir(DECK_COLLECTION_PATH):
        if filename.startswith('fc_') and filename.endswith('.txt'):
            deck_name = filename[3:-4]
            if is_valid_deck_name_format(deck_name):
                existing_decks.append(deck_name)
    return sorted(existing_decks)


def list_existing_cards(deck_name):
    """
    Retrieve a sorted list of existing flashcards within a specified deck.

    Parameters:
    - deck_name (str): The name of the deck.

    Returns:
    list: A sorted list containing existing flashcards in the specified deck.
    """
    existing_cards = []
    try:
        with open(get_deck_file_path(deck_name)) as f:
            for line in f:
                if line.startswith("#") or line.isspace() or line == "":
                    continue
                front_text, back_text, card_strength, review_interval = line.strip().split("|")
                card_strength = int(card_strength)
                review_interval = int(review_interval)
                existing_cards.append(Flashcard(front_text, back_text, card_strength, review_interval))
    
    except ValueError:
        return []
    
    return sorted(existing_cards, key=lambda card: card.front_text)
                

def print_deck_table(existing_decks):
    """
    Print a formatted table displaying the index and names of existing decks.

    Parameters:
    - existing_decks (list): A list of existing deck names.

    Returns:
    None
    """
    table = PrettyTable()
    table.field_names = [f"{Fore.YELLOW}Index{Style.RESET_ALL}", f"{Fore.YELLOW}Deck Name{Style.RESET_ALL}"]
    for index, deck_name in enumerate(existing_decks, start=1):
        table.add_row([index, deck_name])
    print(table)
    print()


def print_card_table(existing_cards):
    """
    Print a formatted table displaying the index, front and back of existing cards,
    along with their strength and review interval.

    Parameters:
    - existing_cards (list): A list of existing Card objects.

    Returns:
    None
    """
    table = PrettyTable()
    table.field_names = [
        f"{Fore.YELLOW}Index{Style.RESET_ALL}",
        f"{Fore.YELLOW}Front{Style.RESET_ALL}",
        f"{Fore.YELLOW}Back{Style.RESET_ALL}"
    ]

    for index, card in enumerate(existing_cards, start=1):
        table.add_row([index, card.front_text, card.back_text])

    print(table)
    print()
    

def change_deck_name(old_deck_name):
    """
    Renames an existing deck.

    Parameters:
    - old_deck_name (str): The current name of the deck to be changed.

    Returns:
    None
    """
    try:
        new_deck_name = get_deck_name()
        old_file_path = get_deck_file_path(old_deck_name)
        new_file_path = get_deck_file_path(new_deck_name)
        os.rename(old_file_path, new_file_path)
        print(f"Deck '{old_deck_name}' changed to {new_deck_name} {Fore.GREEN}successfully{Style.RESET_ALL}.")

    except:
        pass


def add_new_flashcard(deck_name):
    """
    Adds a new flashcard to the specified deck.

    Parameters:
    - deck_name (str): The name of the deck to which the new flashcard will be added.

    Returns:
    None
    """
    print("Enter card data: ")
    card_front_text = get_card_front_text(deck_name)
    card_back_text = get_card_back_text()

    existing_cards = list_existing_cards(deck_name)
    existing_cards.append(Flashcard(card_front_text, card_back_text))

    with open(get_deck_file_path(deck_name), "w") as f:
        for card in sorted(existing_cards, key=lambda card: card.front_text):
            f.write(f"{card.front_text}|{card.back_text}|{card.card_strength}|{card.review_interval}\n")


def edit_existing_flashcard(deck_name):
    """
    Edits an existing flashcard in the specified deck.

    Parameters:
    - deck_name (str): The name of the deck containing the flashcard to be edited.

    Returns:
    None
    """
    try:
        existing_cards = list_existing_cards(deck_name)
        if not existing_cards:
            print("This Deck is empty.")
            print("Choose '2. Add Flashcard' to start adding Flashcards.")
            print()
            return

        print_card_table(existing_cards)
        card_choice_list = list(range(1, len(existing_cards) + 1))
        card_choice = get_choice(card_choice_list)
        print("Enter new card data: ")

        card_front_text = get_card_front_text(deck_name)
        card_back_text = get_card_back_text()

        existing_cards[card_choice - 1] = Flashcard(card_front_text, card_back_text)

        with open(get_deck_file_path(deck_name), "w") as f:
            for card in sorted(existing_cards, key=lambda card: card.front_text):
                f.write(f"{card.front_text}|{card.back_text}|{card.card_strength}|{card.review_interval}\n")

    except:
        pass


def update_card(deck_name, old_card, new_card):
    """
    Edits an existing flashcard in the specified deck.

    Parameters:
    - deck_name (str): The name of the deck containing the flashcard to be edited.

    Returns:
    None
    """
    try:
        existing_cards = list_existing_cards(deck_name)
        
        for index, card in enumerate(existing_cards):
            if str(card) == str(old_card):
                existing_cards[index] = new_card
                break

        with open(get_deck_file_path(deck_name), "w") as f:
            for card in sorted(existing_cards, key=lambda card: card.front_text):
                f.write(f"{card.front_text}|{card.back_text}|{card.card_strength}|{card.review_interval}\n")

    except:
        pass


def exit_program_check(input_to_check):
    """
    Checks if the provided input signals an exit command (':q').
    If the input matches, it triggers the program exit.

    Parameters:
    - input_to_check (str): The user input to check for the exit command.

    Returns:
    None
    """
    if input_to_check == ":q":
        exit_program()


def back_to_main_menu_check(input_to_check):
    """
    Checks if the provided input signals a return to the main menu command (':m').
    If the input matches, it raises the BackToMainMenu exception.

    Parameters:
    - input_to_check (str): The user input to check for the main menu command.

    Raises:
    - BackToMainMenu: Exception indicating a request to return to the main menu.

    Returns:
    None
    """
    if input_to_check == ":m":
        raise BackToMainMenu


def exit_program():
    """
    Exits the Flashcard Review Program and displays a goodbye message.

    Parameters:
    None

    Returns:
    None
    """
    sys.exit("\nExiting the Flashcard Review Program. Goodbye!")

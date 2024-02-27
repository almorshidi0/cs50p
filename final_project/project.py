import random
import os
from flashcard_class import Flashcard
from flashcard_utilities import *
from colorama import Fore, Style


def welcome_user():
    """
    Prints the welcome statement for the flashcard review program.
    """
    print(Fore.GREEN + PROGRAM_WELCOME_STATEMENT + Style.RESET_ALL)


def initialize_collection():
    """
    Creates the collection directory if it doesn't exist.
    """
    if not os.path.exists(DECK_COLLECTION_PATH):
        os.makedirs(DECK_COLLECTION_PATH)
    

def main_menu():
    """
    Displays the main menu of the flashcard review program and handles user choices.
    """
    while True:
        try:
            print(MAIN_MENU_STATEMENT)
            choice_list = list(range(1, 8))
            choice = get_choice(choice_list)
            if choice == 1:
                create_new_deck()
                print()
                
            elif choice == 2:
                edit_existing_deck()
                print()
                
            elif choice == 3:
                initiate_deck_review()
                print()
            
            elif choice == 4:
                explore_and_review_decks()
                print()
                    
            elif choice == 5:
                display_deck_statistics()
                print()
            
            elif choice == 6:
                display_help_information()
                print()
                
            elif choice == 7:
                raise KeyboardInterrupt
        
        except BackToMainMenu:
            print(Fore.BLUE + "Returning to the main menu..." + Style.RESET_ALL)
        

def create_new_deck():
    """
    Creates a new deck for flashcards.

    This function prompts the user to input a unique deck name, creates a new deck file, and prints a success message.
    The user is then guided to choose '2. Edit Deck' to start adding cards to the newly created deck.

    Returns:
    None
    """
    try:
        deck_name = get_deck_name()

        with open(deck_file_path(deck_name), "w"):
            pass

        print(Fore.GREEN + f"Deck '{deck_name}' was added successfully." + Style.RESET_ALL)
        print(Fore.GREEN + f"Next: Choose '2. Edit Deck' to start adding cards to the new Deck '{deck_name}'." + Style.RESET_ALL)

    except BackToMainMenu:
        print(Fore.BLUE + "Returning to the main menu..." + Style.RESET_ALL)


def edit_existing_deck():
    """
    Allows the user to edit an existing flashcard deck. The user can choose a deck, then select an action:
    1. Edit the deck name.
    2. Add a new flashcard to the deck.
    3. Edit an existing flashcard in the deck.

    This function handles the interactive process of deck editing, guiding the user through the available options.

    Returns:
    None
    """
    try:
        while True:
            existing_decks = list_existing_decks()

            if not existing_decks:
                print(Fore.YELLOW + "The Decks collection is empty." + Style.RESET_ALL)
                print(Fore.YELLOW + "Choose '1. Add Deck' to start adding Decks." + Style.RESET_ALL)
                print()
                return

            print("Choose a deck to edit: ")
            deck_choice_list = list(range(1, len(existing_decks) + 1))
            print_deck_table(existing_decks)
            deck_choice = get_choice(deck_choice_list)

            while True:
                print(EDIT_DECK_MENU_STATEMENT)
                action_choice_list = list(range(1, 6))
                action_choice = get_choice(action_choice_list)
                if action_choice == 1:
                    existing_decks[deck_choice - 1] = change_deck_name(existing_decks[deck_choice - 1])

                elif action_choice == 2:
                    add_new_flashcard(existing_decks[deck_choice - 1])

                elif action_choice == 3:
                    edit_existing_flashcard(existing_decks[deck_choice - 1])

                elif action_choice == 4:
                    break

                elif action_choice == 5:
                    raise BackToMainMenu

    except BackToMainMenu:
        print(Fore.BLUE + "Returning to the main menu..." + Style.RESET_ALL)


def initiate_deck_review():
    """
    Initiate the flashcard review process.

    This function allows the user to review flashcards from a selected deck.
    If the deck or flashcards are not available, appropriate messages are displayed.

    Returns:
    None
    """
    try:
        while True:
            existing_decks = list_existing_decks()

            if not existing_decks:
                print(Fore.YELLOW + "The Decks collection is empty." + Style.RESET_ALL)
                print(Fore.YELLOW + "Choose '1. Add Deck' to start adding Decks." + Style.RESET_ALL)
                print()
                return

            print("Choose a deck to review: ")
            deck_choice_list = list(range(1, len(existing_decks) + 1))
            print_deck_table(existing_decks)
            deck_choice = get_choice(deck_choice_list)

            existing_cards = list_existing_cards(existing_decks[deck_choice - 1])

            if not existing_cards:
                print(Fore.YELLOW + "This Deck is empty." + Style.RESET_ALL)
                print(Fore.YELLOW + "Choose '2. Edit Deck' to start adding Flashcards." + Style.RESET_ALL)
                print()
                break

            while True:
                index = random.choice(range(len(existing_cards)))
                card = existing_cards[index]

                if card.review_interval == 1:
                    print(f"\nFront: {card.front_text}")
                    answer = get_card_back_text()

                    if answer.lower() == card.back_text.lower():
                        print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
                        card.card_strength += 1
                        card.review_interval = card.card_strength * 2
                    else:
                        print(Fore.RED + "Incorrect. The correct back_text is:" + Style.RESET_ALL, card.back_text)
                        card.card_strength = 1
                        card.review_interval = 1
                else:
                    card.review_interval -= 1
                    
                existing_cards[index] = card
                
                


    except BackToMainMenu:
        update_deck(existing_decks[deck_choice - 1], existing_cards)
        print(Fore.BLUE + "Returning to the main menu..." + Style.RESET_ALL)


def explore_and_review_decks():
    """
    Allows the user to explore and review flashcard decks.

    This function prompts the user to choose a deck from the existing collection.
    If the selected deck has flashcards, it displays them in a table format for review.
    If the deck or flashcards are not available, appropriate messages are displayed.

    Returns:
    None
    """
    try:
        while True:
            existing_decks = list_existing_decks()

            if not existing_decks:
                print(Fore.YELLOW + "The Decks collection is empty." + Style.RESET_ALL)
                print(Fore.YELLOW + "Choose '1. Add Deck' to start adding Decks." + Style.RESET_ALL)
                print()
                return

            print("Choose a deck to review: ")
            deck_choice_list = list(range(1, len(existing_decks) + 1))
            print_deck_table(existing_decks)
            deck_choice = get_choice(deck_choice_list)
            
            existing_cards = list_existing_cards(existing_decks[deck_choice - 1])

            if not existing_cards:
                print(Fore.YELLOW + "This Deck is empty." + Style.RESET_ALL)
                print(Fore.YELLOW + "Choose '2. Edit Deck' to start adding Flashcards." + Style.RESET_ALL)
                print()
                break
            
            print(Fore.GREEN + "Flashcards in the selected deck:" + Style.RESET_ALL)
            print_card_table(existing_cards)

    except BackToMainMenu:
        print(Fore.BLUE + "Returning to the main menu..." + Style.RESET_ALL)

def display_deck_statistics():
    """
    Display statistics for the selected deck.

    This function provides statistics on the progress of reviewing flashcards in a selected deck.
    It shows the total number of cards, the number of cards reviewed, and the overall progress.

    Returns:
    None
    """
    try:
        while True:
            existing_decks = list_existing_decks()

            # Check if there are existing decks
            if not existing_decks:
                print(Fore.YELLOW + "The Decks collection is empty." + Style.RESET_ALL)
                print(Fore.YELLOW + "Choose '1. Add Deck' to start adding Decks." + Style.RESET_ALL)
                print()
                return

            print("Choose a deck to view statistics: ")
            deck_choice_list = list(range(1, len(existing_decks) + 1))
            print_deck_table(existing_decks)
            deck_choice = get_choice(deck_choice_list)

            existing_cards = list_existing_cards(existing_decks[deck_choice - 1])
            total_cards = len(existing_cards)
            reviewed_cards = sum(1 for card in existing_cards if card.card_strength > 1)

            if total_cards == 0:
                print(Fore.YELLOW + "No cards available for progress tracking." + Style.RESET_ALL)
            elif reviewed_cards == 0:
                print(Fore.YELLOW + "No cards have been reviewed yet." + Style.RESET_ALL)
            else:
                progress_percentage = (reviewed_cards / total_cards) * 100
                print(Fore.CYAN + f"Overall Progress: {reviewed_cards}/{total_cards} cards reviewed ({progress_percentage:.2f}%)." + Style.RESET_ALL)

    except BackToMainMenu:
        print(Fore.BLUE + "Returning to the main menu..." + Style.RESET_ALL)
    

def display_help_information():
    print(PROGRAM_WELCOME_STATEMENT)


def main():
    welcome_user()
    initialize_collection()
    while True:
        try:
            main_menu()
        
        except KeyboardInterrupt:
            print()
            exit_program()
        except EOFError:
            print("\n" + Fore.BLUE + "Returning to the main menu..." + Style.RESET_ALL)
            
    
if __name__ == "__main__":
    main()

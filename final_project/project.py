import random
import sys

# Card object representing a flashcard
class Card:
    def __init__(self, question="Type a question here", answer="Type the answer to the question", strength=1, interval=1):
        """
        Initialize a new flashcard.

        Parameters:
        - question (str): The question on the flashcard.
        - answer (str): The answer to the flashcard question.
        - strength (int): The strength of the flashcard for spaced repetition.
        - interval (int): The review interval for spaced repetition.

        Returns:
        None
        """
        self.question   = question
        self.answer     = answer
        self.strength   = strength  # Card strength
        self.interval   = interval # Review interval for spaced repitition
        
    def __str__(self):
        """
        Return a formatted string representation of the flashcard.

        Returns:
        str: Formatted string representation of the flashcard.
        """
        return f"{self.question} --> {self.answer} (Strength: {self.strength}, Interval: {self.interval})"
    
    # Property and setter methods for encapsulation
    
    @property
    def question(self):
        return self._question
    
    @question.setter
    def question(self, question):
        self._question = question
    
    @property
    def answer(self):
        return self._answer
    
    @answer.setter
    def answer(self, answer):
        self._answer = answer
    
    @property
    def strength(self):
        return self._strength
    
    @strength.setter
    def strength(self, strength):
        self._strength = strength
        
    @property
    def interval(self):
        return self._interval
    
    @interval.setter
    def interval(self, interval):
        self._interval = interval
    

# Check if file exists and is valid
def is_valid_flashcards_file(filename):
    """
    Check if the file exists and contains valid flashcard data.

    Parameters:
    - filename (str): The name of the file.

    Returns:
    bool: True if the file exists and is valid, False otherwise.
    """
    if ".txt" not in filename:
        return False
    try:
        with open(filename) as f:
            # Check if file contains valid card data
            for line in f:
                if line.startswith("#") or line.isspace() or line == "":
                    continue  # Skip comment lines, white space lines, and empty lines
                question, answer, strength, interval = line.strip().split("|")
                strength = int(strength)
                interval = int(interval)
                pass
            return True
    except FileNotFoundError:
        return False
    except ValueError:
        return False

# Create a new file with initial content
def create_new_file(filename):
    """
    Create a new flashcard file with initial content.

    Parameters:
    - filename (str): The name of the file.

    Returns:
    None
    """
    with open(filename, "w") as f:
        f.write("# This is a flashcard file.\n")
        f.write("# Add your cards in the format: question,answer,strength,interval")

# Load cards from a file
def load_cards(filename):
    """
    Load flashcards from a file.

    Parameters:
    - filename (str): The name of the file.

    Returns:
    list: List of Card objects representing flashcards.
    """
    cards = []
    if is_valid_flashcards_file(filename):
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("#") or line.isspace() or line == "":
                    continue  # Skip comment lines, white space lines, and empty lines
                question, answer , strength, interval = line.strip().split("|")
                strength = int(strength)
                interval = int(interval)
                cards.append(Card(question, answer, strength, interval))
    return cards

# Save cards to a file
def save_cards(cards, filename):
    """
    Save flashcards to a file.

    Parameters:
    - cards (list): List of Card objects representing flashcards.
    - filename (str): The name of the file.

    Returns:
    None
    """
    with open(filename, "w") as f:
        for card in cards:
            f.write(f"{card.question}|{card.answer}|{card.strength}|{card.interval}\n")

# Review cards until user quits
def review_cards(cards):
    """
    Review flashcards until the user decides to quit.

    Parameters:
    - cards (list): List of Card objects representing flashcards.

    Returns:
    None
    """
    again = True
    while again and not cards ==[]:
        card = random.choice(cards)
        if card.interval == 1:
            print(f"\nQuestion: {card.question}")
            answer = input("Your answer (:q to return to the previous menu): ").strip()
            if answer.lower() == card.answer.lower():
                print("Correct!")
                # Update card's strength and review interval based on performance
                card.strength += 1
                card.interval = card.strength * 2
            elif answer.lower() == ":q":
                again = False
            else:
                print("Incorrect. The answer is:", card.answer)
                # Reset card's strength and review interval for incorrect answers
                card.strength = 1
                card.interval = 1
        else:
            card.interval -= 1

# Add a new card
def add_card(cards):
    """
    Add a new flashcard to the list.

    Parameters:
    - cards (list): List of Card objects representing flashcards.

    Returns:
    None
    """
    question = answer = "|"
    while "|" in question:
        question = input("Enter the question: ").strip()
        if "|" in question:
            print("The '|' character isn't allowed.")
    while "|" in answer:
        answer = input("Enter the answer: ").strip()
        if "|" in answer:
            print("The '|' character isn't allowed.")
    cards.append(Card(question, answer))
    print("Card added successfully!")

# Edit an existing card
def edit_card(cards):
    """
    Edit an existing flashcard.

    Parameters:
    - cards (list): List of Card objects representing flashcards.

    Returns:
    None
    """
    if not cards:
        print("No cards available to edit.")
        return
    for i, card in enumerate(cards):
        print(f"{i+1}. {card.question}")

    choice = int(input("Enter the card number to edit: ").strip()) - 1
    if 0 <= choice < len(cards):
        new_question = new_answer = "|"
        while "|" in new_question or new_question == "":
            new_question = input("Enter the new question: ").strip() or cards[choice].question
            if "|" in new_question:
                print("The '|' character isn't allowed.")
        while "|" in new_answer or new_answer == "":
            new_answer = input("Enter the new answer: ").strip() or cards[choice].answer
            if "|" in new_answer:
                print("The '|' character isn't allowed.")
        cards[choice] = Card(new_question, new_answer)
        print("Card edited successfully!")
    else:
        print("Invalid card number.")

# Track overall progress
def track_progress(cards):
    """
    Track the overall progress of flashcard review.

    Parameters:
    - cards (list): List of Card objects representing flashcards.

    Returns:
    None
    """
    total_cards = len(cards)
    reviewed_cards = sum(1 for card in cards if card.strength > 1)  # Count cards that have been reviewed more than once

    if total_cards == 0:
        print("No cards available for progress tracking.")
    elif reviewed_cards == 0:
        print("No cards have been reviewed yet.")
    else:
        progress_percentage = (reviewed_cards / total_cards) * 100
        print(f"Overall Progress: {reviewed_cards}/{total_cards} cards reviewed ({progress_percentage:.2f}%).")

# Main program loop
def main():
    """
    Main program loop for flashcard management.

    Returns:
    None
    """
    program_done = False # A flag to determine wether to quit the program
    
    # Welcome the user
    print("===== Flashcard Review Program =====")
    print("Welcome to an interactive learning experience!")
    print("------------------------------------------------------------------------\n")
    
    while not program_done:
        file_menu_done = False # A flag to determine wether to close the current file
        new = False # A flag to determine wether a file is new
        option = input("Do you want to use your own flashcard file or another existing flashcard file (y/n)? ").strip()
        if option.lower() == "y":
            print("Make sure the file is formatted as follows: ")
            print("\tType your question here|Type the answer|1|1")
            print("The '|' character is what seperates your questions, answers, and other values.")
            print("Each flashcard must be on a seperate line.")
            print("The 2 numerical values '1|1' are default values.")
            print("------------------------------------------------------------------------\n")
            while not file_menu_done:
                print("Type ':q' to exit the program, or ':b' to go back to the previous menu.")
                filename = input("Enter the name of an existing flashcards file: ").strip()
                if filename.lower() == ":q":
                    print("Exiting the Flashcard Review Program. Goodbye!")
                    program_done = True
                    break
                elif filename.lower() == ":b":
                    print("")
                    break
                
                if ".txt" not in filename:
                    filename = filename + ".txt"
                if not is_valid_flashcards_file(filename):
                    filename = filename.replace(".txt", "")
                    print(f"Error: Invalid file '{filename}'.\n")
                    file_menu_done = True
                while not file_menu_done:
                    cards = []
                    # Load cards from existing file (if not new)
                    if not new:
                        cards = load_cards(filename)
                        if cards == []:
                            print("File is empty.")
                        while not file_menu_done:
                            print("\nMenu:")
                            print("1. Review cards")
                            print("2. Add a card")
                            print("3. Edit a card")
                            print("4. Track progress")
                            print("5. Close file")

                            choice = input("Enter your choice: ").strip()

                            if choice == "1":
                                review_cards(cards)
                                # Save updated cards after review
                                save_cards(cards, filename)
                            elif choice == "2":
                                add_card(cards)
                                # Save cards after adding a new one
                                save_cards(cards, filename)
                            elif choice == "3":
                                edit_card(cards)
                                # Save cards after editing
                                save_cards(cards, filename)
                            elif choice == "4":
                                track_progress(cards)
                            elif choice == "5":
                                print("Closing the flashcard file.\n")
                                file_menu_done = True
                            else:
                                print("Invalid choice.\n")
            
        elif option == "n":
            new = True
            filename = input("Enter a filename for the new file: ").strip()
            if ".txt" not in filename:
                filename = filename + ".txt"
            create_new_file(filename)
            while (not file_menu_done) and new:
                print("\nMenu:")
                print("1. Add a card")
                print("2. Close file")
                
                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    add_card(cards)
                    # Save cards after adding a new one
                    save_cards(cards, filename)
                    new = False
                elif choice == "2":
                    print("Closing the flashcard file.\n")
                    file_menu_done = True
                else:
                    print("Invalid choice.\n")
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()

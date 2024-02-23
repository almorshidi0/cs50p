import random
import sys

# Card object
class Card:
    def __init__(self, question, answer, iterations=1):
        self.question = question
        self.answer = answer
        self.iterations = iterations  # Repetition iterations (1-4)
        
    def __str__(self):
        return str(self.question) + "\n\t" + str(self.answer)
    
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
    def iterations(self):
        return self._iterations
    
    @iterations.setter
    def iterations(self, iterations):
        self._iterations = iterations
    

# Check if file exists and is valid
def is_valid_flashcards_file(filename):
    try:
        with open(filename) as f:
            # Check if file contains valid card data
            for line in f:
                if line.startswith("#"):
                    continue  # Skip comment lines
                elif line == "":
                    continue
                question, answer = line.strip().split(",")
                pass
            return True
    except FileNotFoundError:
        return False
    except ValueError:
        return False

# Create a new file with initial content
def create_new_file(filename):
    with open(filename, "w") as f:
        f.write("# This is a flashcard file.")
        f.write("# Add your cards in the format: question,answer")

# Load cards from a file
def load_cards(filename):
    cards = []
    if is_valid_flashcards_file(filename):
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("#"):
                    continue  # Skip comment lines
                question, answer = line.strip().split(",")
                cards.append(Card(question, answer))
    return cards

# Save cards to a file
def save_cards(cards, filename):
    with open(filename, "w") as f:
        for card in cards:
            f.write(f"{card.question},{card.answer}\n")

# Review a single card
def review_cards(cards):
    again = True
    while again:
        card = random.choice(cards)
        if card.iterations < 4:
            print(f"\nQuestion: {card.question}")
            answer = input("Your answer: ")
            if answer.lower() == card.answer.lower():
                print("Correct!")
                # Update card iterations based on performance
                card.iterations = min(4, card.iterations + 1)
            else:
                print("Incorrect. The answer is:", card.answer)
                # Reset iterations for incorrect answers
                card.iterations = 1
        while True:
            again = input("Do you want to continue (y/n)? ").strip().lower()
            if again == "y":
                again = True
                break
            elif again == "n":
                again = False
                break
            else:
                print("Invalid choice")

# Add a new card
def add_card(cards):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    cards.append(Card(question, answer))
    print("Card added successfully!")

# Edit an existing card
def edit_card(cards):
    if not cards:
        print("No cards available to edit.")
        return

    for i, card in enumerate(cards):
        print(f"{i+1}. {card.question}")

    choice = int(input("Enter the card number to edit: ")) - 1
    if 0 <= choice < len(cards):
        new_question = input("Enter the new question: ") or cards[choice].question
        new_answer = input("Enter the new answer: ") or cards[choice].answer
        cards[choice] = Card(new_question, new_answer)
        print("Card edited successfully!")
    else:
        print("Invalid card number.")

# Track overall progress
def track_progress(cards):
    reviewed = len([card for card in cards if card.iterations < 4])
    total = len(cards)
    if reviewed and total:
        print(f"Progress: {reviewed}/{total} cards reviewed.")
    elif not reviewed:
        print("No cards reviewed yet.")
    else:
        print("No cards to review.")

# Main program loop
def main():
    # A flag to determine wether to quit the program
    done = False
    # A flag to determine wether a file is new
    new = False
    # Get filename from user
    filename = input("Enter the filename for flashcards (or 'new' to create a new file): ")

    # Handle new file creation
    if filename.lower() == "new":
        new = True
        new_filename = input("Enter a filename for the new file: ")
        if ".txt" not in new_filename:
            new_filename = new_filename + ".txt"
        create_new_file(new_filename)
        filename = new_filename
    # Check if existing file is valid
    else:
        if ".txt" not in filename:
            filename = filename + ".txt"
        if not is_valid_flashcards_file(filename):
            filename = filename.replace(".txt", "")
            sys.exit(f"Error: Invalid file '{filename}'.")
            
    while not done:
        # Load cards from existing file (if not new)
        if not new:
            cards = []
            cards = load_cards(filename)
            while not done:
                print("\nMenu:")
                print("1. Review cards")
                print("2. Add a card")
                print("3. Edit a card")
                print("4. Track progress")
                print("5. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    review_cards(cards)
                    # Save updated cards after each review
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
                    print("Exiting program.")
                    done = True
                else:
                    print("Invalid choice.")
        else:
            cards = []
            while (not done) and new:
                print("\nMenu:")
                print("1. Add a card")
                print("2. Exit")
                
                choice = input("Enter your choice: ")

                if choice == "1":
                    add_card(cards)
                    # Save cards after adding a new one
                    save_cards(cards, filename)
                    new = False
                elif choice == "2":
                    print("Exiting program.")
                    done = True
                    break
                else:
                    print("Invalid choice.")

if __name__ == "__main__":
    main()

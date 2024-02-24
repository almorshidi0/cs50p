import os
from project import Card, create_new_file, is_valid_flashcards_file, load_cards, save_cards


def init_file(filename):
    flashcards0_content = """What is the capital of France?|Paris|2|4
Can you name the largest mammal?|Blue Whale|1|1
What is the powerhouse of the cell?|Mitochondria|3|6
Who wrote Romeo and Juliet?|William Shakespeare|2|3
How many continents are there?|7|1|1
"""
    flashcards1_content = """# This is a comment line
What is the capital of France?|Paris|2|4

# Another comment line
Can you name the largest mammal?|Blue Whale|1|1

# Empty line
What is the powerhouse of the cell?|Mitochondria|3|6

Who wrote Romeo and Juliet?|William Shakespeare|2|3

How many continents are there?|7|1|1
"""
    if filename == "flashcards0.txt":
        file_content = flashcards0_content
    elif filename == "flashcards1.txt":
        file_content = flashcards1_content
    elif filename == "existing_file.txt":
        file_content = """This is not in the correct format
"""
        
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, "w") as f:
        f.write(file_content)
        
def remove_file(filename):
    os.remove(filename)

def test_init():
    """
    Test the initialization of the Card class.
    """
    card = Card()
    assert card.question == "Type a question here"
    assert card.answer == "Type the answer to the question"
    assert card.strength == 1
    assert card.interval == 1

    card = Card("What is the capital of France?", "Paris", 3, 5)
    assert card.question == "What is the capital of France?"
    assert card.answer == "Paris"
    assert card.strength == 3
    assert card.interval == 5


def test_str():
    """
    Test the string representation of the Card class.
    """
    card = Card()
    assert str(card) == "Type a question here --> Type the answer to the question (Strength: 1, Interval: 1)"

    card = Card("What is the capital of France?", "Paris", 3, 5)
    assert str(card) == "What is the capital of France? --> Paris (Strength: 3, Interval: 5)"


def test_is_valid():
    """
    Test the is_valid_flashcards_file function.
    """
    init_file("flashcards0.txt")
    assert is_valid_flashcards_file("flashcards0.txt") == True
    remove_file("flashcards0.txt")
    init_file("flashcards1.txt")
    assert is_valid_flashcards_file("flashcards1.txt") == True  # Valid file with comment lines, white space lines, and empty lines
    remove_file("flashcards1.txt")
    init_file("existing_file.txt")
    assert is_valid_flashcards_file("existing_file.txt") == False  # Existing file but not of the expected format
    remove_file("existing_file.txt")
    assert is_valid_flashcards_file("project.py") == False  # The program only works with .txt files
    assert is_valid_flashcards_file("non_existing_file.txt") == False


def test_create_new_file():
    """
    Test the create_new_file function.
    """
    filename = "test_file.txt"
    create_new_file(filename)
    assert os.path.exists(filename)
    with open(filename) as f:
        content = f.read().strip()
    assert content == "# This is a flashcard file.\n# Add your cards in the format: question,answer,strength,interval"
    os.remove(filename)


def test_load_cards():
    """
    Test the load_cards function.
    """
    init_file("flashcards0.txt")
    cards = load_cards('flashcards0.txt')
    remove_file("flashcards0.txt")
    assert len(cards) == 5
    assert cards[0].question == "What is the capital of France?"
    assert cards[0].answer == "Paris"


def test_save_cards():
    """
    Test the save_cards function.
    """
    cards = [Card("Q1", "A1", 2, 4), Card("Q2", "A2", 1, 2)]
    filename = "test_save.txt"
    
    # Remove the file if it exists
    if os.path.exists(filename):
        os.remove(filename)

    save_cards(cards, filename)
    assert os.path.exists(filename)
    with open(filename) as f:
        content = f.read().strip()
    assert content == "Q1|A1|2|4\nQ2|A2|1|2"
    os.remove(filename)

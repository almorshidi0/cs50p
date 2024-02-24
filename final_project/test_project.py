import os
from project import (Card, create_new_file, is_valid_flashcards_file, load_cards, save_cards)


def test_init():
    card = Card()
    assert card.question == "question"
    assert card.answer == "answer"
    assert card.iterations == 1
    card = Card("What is the capital of France?","Paris")
    assert card.question == "What is the capital of France?"
    assert card.answer == "Paris"
    assert card.iterations == 1

def test_str():
    card = Card()
    assert str(card) == "question --> answer"
    card = Card("What is the capital of France?","Paris")
    assert str(card) == "What is the capital of France? --> Paris"
    
def test_is_valid():
    assert is_valid_flashcards_file("flashcards0.txt") == True
    assert is_valid_flashcards_file("flashcards1.txt") == True # Valid file with comment lines, white space lines, and empty lines
    assert is_valid_flashcards_file("existing_file.txt") == False # existing file but of the expected format 
    assert is_valid_flashcards_file("existing_file.docx") == False # The program only works with .txt files
    assert is_valid_flashcards_file("non_existing_file.txt") == False
    
def test_create_new_file():
    filename = "test_file.txt"
    create_new_file(filename)
    assert os.path.exists(filename)
    with open(filename) as f:
        content = f.read().strip()
    assert content == "# This is a flashcard file.\n# Add your cards in the format: question,answer"
    os.remove(filename)
  
def test_load_cards():
    cards = load_cards('flashcards0.txt')
    assert len(cards) == 5
    assert cards[0].question == "What is the capital of France?"
    assert cards[0].answer == "Paris"

def test_save_cards():
    cards = [Card("Q1", "A1"), Card("Q2", "A2")]
    filename = "test_save.txt"
    save_cards(cards, filename)
    assert os.path.exists(filename)
    with open(filename) as f:
        content = f.read().strip()
    assert content == "Q1,A1\nQ2,A2"
    os.remove(filename)

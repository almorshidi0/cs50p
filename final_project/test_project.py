import os
import pytest
from flashcard_class import Flashcard
from flashcard_utilities import (BackToMainMenu, DECK_COLLECTION_PATH,
                                 get_deck_file_path, is_valid_deck_name_format,
                                 is_valid_card_data_format, back_to_main_menu_check)
# Testing ths flashcard_class.py
def test_init():
    """
    Test the initialization of the Card class.
    """
    card = Flashcard()
    assert card.front_text == "Type the front_text of the card here"
    assert card.back_text == "Type the back_text of the card here"
    assert card.card_strength == 1
    assert card.review_interval == 1

    card = Flashcard("What is the capital of France?", "Paris", 3, 5)
    assert card.front_text == "What is the capital of France?"
    assert card.back_text == "Paris"
    assert card.card_strength == 3
    assert card.review_interval == 5


def test_str():
    """
    Test the string representation of the Card class.
    """
    card = Flashcard()
    assert str(card) == "Front: Type the front_text of the card here\nBack: Type the back_text of the card here"

    card = Flashcard("What is the capital of France?", "Paris", 3, 5)
    assert str(card) == "Front: What is the capital of France?\nBack: Paris"


# Testing flashcard_utilities.py
def test_get_deck_file_path():
    deck_name = "__deck__"
    assert get_deck_file_path(deck_name) == f"{DECK_COLLECTION_PATH}fc_{deck_name}.txt"
    deck_name = "__Deck__"
    assert get_deck_file_path(deck_name) == f"{DECK_COLLECTION_PATH}fc_{deck_name}.txt"
    
    
def test_is_valid_deck_name_format():
    """
    Test the is_valid_deck_name_format function.
    """
    assert is_valid_deck_name_format("__deck__") == True # Valid deck name
    assert is_valid_deck_name_format("__Deck__") == True  # Valid deck name
    
    assert is_valid_deck_name_format("1_deck") == False  # deck names must start with a letter or an underscore '_'
    assert is_valid_deck_name_format("__#deck__") == False # deck names only consist of letters, underscores '_', and numbers
    

def test_is_valid_card_data_format():
    """
    Test the is_valid_card_data_format function.
    """
    assert is_valid_card_data_format("ValidCard123") == True
    assert is_valid_card_data_format("Card with spaces") == True
    assert is_valid_card_data_format("Special@Characters!") == True
    
    assert is_valid_card_data_format("عربي") == False


def test_back_to_main_menu_check():
    # Test case for valid input signaling a return to the main menu
    with pytest.raises(BackToMainMenu):
        back_to_main_menu_check(":m")

    # Test case for input that does not signal a return to the main menu
    try:
        back_to_main_menu_check("NotMainCommand")
    except BackToMainMenu:
        # Adding an assertion that fails to make the test case fail
        # This block will be executed if the exception is raised
        assert False, "Expected BackToMainMenu exception was not raised"

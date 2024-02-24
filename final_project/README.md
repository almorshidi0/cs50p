# Flashcard APP

## Overview

Welcome to the Flashcard Review Program! This project serves as the final assignment for the CS50's Introduction to Programming with Python course ([CS50 Python](https://cs50.harvard.edu/python/2022/)). The program is designed to facilitate interactive flashcard reviews, allowing users to create, edit, and reinforce their knowledge.

## Video Demo

To get a visual demonstration of the Flashcard Review Program, please watch this [video demo](#). This video offers a walkthrough of the program, showcasing key features such as card creation, editing, reviewing, and progress tracking. The demo aims to provide a hands-on understanding of the program's functionalities.

## Project Description

The Flashcard Review Program is implemented in Python and structured around a `Card` class, handling flashcard properties and functionalities. The main file, `project.py`, encompasses file handling, card manipulation, and the program's main loop. The accompanying `test_project.py` file contains unit tests to ensure the reliability of the implemented functions.

## Card Class

The `Card` class is central to the program, representing flashcards with properties for questions, answers, and iteration counts. It includes methods to maintain data integrity and provide a readable string representation.

## Functions in project.py

The `project.py` file hosts various functions catering to file validation, user interaction, and flashcard manipulation. Notable functions include file validation (`is_valid_flashcards_file`), card creation (`add_card`), reviewing (`review_cards`), and progress tracking (`track_progress`).

## Design Choices

The program's design emphasizes user interaction and progress tracking. Noteworthy design choices include

1. **Prerequisites:** Ensure you have `Python 3` installed on your system.
2. **Download the files:** Download the project files, including `project.py`, `test_project.py`, and `requirements.txt`.
3. **Run the program:** Open a terminal or command prompt, navigate to the project directory, and execute `python project.py` or `python3 project.py`.

- **File Validation**: Ensuring file validity to prevent errors during loading.
- **User Interaction**: Providing a user-friendly menu for an intuitive experience.
- **Card Iterations**: Utilizing iteration counts to track user progress during flashcard reviews.

## Testing

Unit tests in `test_project.py` validate the correctness of the Card class and various functions in `project.py`. These tests are integral to maintaining the reliability of the program's functionality.

## Conclusion

The Flashcard Review Program is an educational tool designed help enhance your learning experience of any subject of your choice. Dive into the code, explore the functionalities, and consider watching the video demo for a hands-on experience, and feel free to reuse and edit the code to match your own requirements or taste.

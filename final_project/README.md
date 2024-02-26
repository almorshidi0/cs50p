# Flashcard Review Program: Empowering Your Learning Journey

## Introduction

Welcome to the **Flashcard Review Program**, a comprehensive and user-friendly learning tool developed using `Python`. This project serves as the final assignment for CS50's Introduction to Programming with Python course ([CS50 Python](https://cs50.harvard.edu/python/2022/)), offering an interactive platform to strengthen your knowledge through efficient flashcard creation, review, and management.

## Video Demo

To get a visual demonstration of the Flashcard Review Program, please watch this [video demo](#). This video offers a walkthrough of the program, showcasing key features such as card creation, editing, reviewing, and progress tracking. The demo aims to provide a hands-on understanding of the program's functionalities.

## Project Overview

This program empowers you to:

* **Craft insightful flashcards:** Effortlessly create new flashcards tailored to your specific learning objectives. You have complete control over the questions, answers.
* **Engage in interactive review sessions:** The program shuffles your flashcards to prevent memorization based on sequence and tests your understanding by displaying the card's question. Based on your response, it provides immediate feedback and adjusts the card's repetition frequency to prioritize those requiring more practice. This adaptive learning approach optimizes your study sessions by focusing on areas needing reinforcement.
* **Effectively track your progress:** Gain valuable insights into your learning journey by monitoring statistics like the number of reviewed cards and those remaining. This clear overview allows you to gauge your progress and target areas for improvement.
* **Navigate seamlessly:** The program boasts a user-friendly menu-driven interface, enabling intuitive interaction and effortless access to functionalities.

## Functionality Breakdown

**1. Building Blocks:**

* **Card Class:** At the core lies the `Card` class, meticulously designed to represent individual flashcards. This class encapsulates essential attributes like the `question`, `answer`, `strength` count, and `interval` count (both used for adaptive learning). It also includes methods to ensure data integrity and present the card's information in a user-friendly format.

**2. Core Components:**

* **project.py:** This central file governs the program's logic and workflow. It encompasses functions essential for:
  * **File Management:** Validating the integrity of flashcard data files ensures seamless program operation.
  * **User Interaction:** The program employs a clear and concise menu, guiding users through various functionalities like creating, editing, reviewing, and tracking progress.
  * **Flashcard Operations:** A suite of functions empower users to add new cards, edit existing ones, and review shuffled cards for optimal knowledge assessment. The review process incorporates adaptive learning principles by adjusting card repetition based on user performance.
  * **Tracking Progress:** Users can access real-time statistics concerning their learning journey, including the number of reviewed and remaining cards.

**3. Ensuring Reliability:**

* **test_project.py:** In the pursuit of robust and dependable functionality, rigorous unit testing is implemented within the `test_project.py` file. This collection of tests is thoughtfully designed to validate the precise functioning of the `Card` class and various critical functions housed within `project.py`. Leveraging the `pytest` library, these tests serve as a robust safety net, offering an additional layer of assurance regarding the program's reliability and optimal performance.

To execute these tests locally and affirm the integrity of the program, utilize the following command within the `final_project` folder of your cloned repository:

```bash
pytest test_projects.py
```

## Beyond the Basics

* **Adaptability:** The open-source nature of this project presents exciting possibilities for customization. You can tailor the code to suit your specific learning needs, incorporate new features, or adjust the overall aesthetics. This flexibility empowers you to create a personalized learning companion.

## Getting Started

* **Prerequisites:** Ensure your system is equipped with `Python 3` to effectively launch the program. Once `` isinstalled, use the following command to guarantee all the necessary requirements for using and validating the program are in place:

```bash
pip install -r requirements.txt
```

* **Obtain the Files:** Clone the project repository from GitHub and navigate to the final_project folder:

```bash
git clone https://github.com/almorshidi0/cs50p.git
cd cs50p/final_project
```

This will provide you with the essential files and structure to seamlessly run and explore the Flashcard Review Program.

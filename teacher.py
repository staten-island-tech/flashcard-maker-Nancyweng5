import json

def save_flashcard(flashcards):
    with open("flashcard.json", "w") as file:
        json.dump(flashcards, file, indent=4) #saves flashcards to JSON file

def load_flashcard():
    try:
        with open("flashcard.json", "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = []
    return flashcards

def teacher_mode():
    flashcards = load_flashcard()
    while True:
        term = input("Enter a word or phrase : ")
        definition = input(f"Enter a definition for {term}")
        flashcards[term] = definition
    

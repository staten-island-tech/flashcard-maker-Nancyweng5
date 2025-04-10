import json

def load_flashcard():
    flashcards = {}
    try:
        with open("flashcard.json", "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = {}
    return flashcards
import json

def load_flashcard():
    flashcards = {}
    try:
        with open("flashcard.json", "r") as file:
            flashcards = json.load(file)
    except FileNotFoundError:
        flashcards = {}
    return flashcards

def student_mode():
    flashcards = load_flashcard()

    score = 0
    streak = 0 

    for term in flashcards:
        definition = input(f"what is the definition for {term} : ")
        if definition.lower() == flashcards[term].lower():
            print("Correct")
            streak += 1
            score += 1
            if streak >= 3:
                print("Bonus Points!")
                score += 1
        else:
            print(f"Wrong definition, the correct answer is : {flashcards[term]}")
            streak = 0
    print(f"Final Score : {score}")

student_mode()
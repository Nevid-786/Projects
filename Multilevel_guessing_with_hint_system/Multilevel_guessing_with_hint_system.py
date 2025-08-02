import random as r
print("welcome To advance Guessing Game!!!")
Level=input("Kindly Choose A Level(Easy,Medium,Hard):").lower().strip()
easy_words = {
    "cat": "A small, furry pet that says 'meow'.",
    "dog": "A loyal animal that barks and loves to fetch.",
    "book": "Flip the pages, gain some knowledge.",
    "sun": "It rises in the east and sets in the west.",
    "tree": "It has leaves, roots, and gives us shade.",
    "car": "Four wheels and vroom vroom!",
    "fish": "It swims in water and breathes through gills.",
    "ball": "Round and fun to kick or throw.",
    "home": "There’s no place like it.",
    "apple": "A red or green fruit, often found in lunchboxes."
}

medium_words = {
    "jungle": "Thick forest, wild animals, and adventure.",
    "planet": "Earth is one of them.",
    "silver": "A shiny metal, second to gold.",
    "danger": "Proceed with caution!",
    "bridge": "Connects two places over water or land.",
    "castle": "A king or queen might live here.",
    "forest": "Lots of trees, maybe some bears.",
    "window": "Lets in light but keeps out the rain.",
    "cloudy": "When the sky looks white or gray.",
    "garden": "Where flowers bloom and vegetables grow."
}
hard_words = {
    "phantom": "You can feel it, but can’t see it.",
    "avalanche": "A deadly rush of snow down a mountain.",
    "labyrinth": "A maze so complex, you might never leave.",
    "mystique": "A sense of mystery or magic.",
    "paradox": "It contradicts itself, yet might be true.",
    "ephemeral": "Here for a moment, gone the next.",
    "quarantine": "Stay isolated to stay safe.",
    "serendipity": "A lucky discovery made by accident.",
    "camouflage": "Blending in to stay hidden.",
    "hieroglyph": "Ancient symbols that told stories."
}
def Game(easy_words,hard_words,medium_words):

    if Level=="easy":
        secret_word=r.choice(list(easy_words.keys()))
        print(f"Hint:",easy_words[secret_word])
    elif Level=="medium":
        secret_word=r.choice(list(medium_words.keys()))
        print(f"Hint:",medium_words[secret_word])
    elif Level=="hard":
        secret_word=r.choice(list(hard_words.keys()))
        print(f"Hint:",hard_words[secret_word])
    else :
        print("Invalid choice:By default easy mode!")
        secret_word=r.choice(list(easy_words.keys()))
        print(f"Hint:",easy_words[secret_word])
    attempts=0
    print("length of word:",len(secret_word))
    while True:
        hint=""
        Guessed_word=input("Guess the word:").lower().strip()
        if len(Guessed_word)!=len(secret_word):
            print("invalid Length Guessed Word!!!")
            continue
        attempts+=1
        if Guessed_word==secret_word:
            print(f"Congrats You Gussed the Correct Word In attempts:{attempts}")
            break
        
        for i in range(len(secret_word)):
            if Guessed_word[i]==secret_word[i]:
                hint+=Guessed_word[i]
            else:
                hint+="_"
        print(f"Hint:",hint)
    if input("Start Again(Yes/No)").lower().strip()=='yes':
        Game(easy_words,hard_words,medium_words)
    else:
        return "Game Over!!!!"
print(Game(easy_words,hard_words,medium_words))
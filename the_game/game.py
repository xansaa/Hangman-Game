import random

def choose_word(category):
    countries = ["Bulgaria", "France", "Germany", "Italy", "Spain", "Belgium", "Denmark", "Netherlands", "Norway",
                 "Poland",
                 "Portugal", "Turkey", "Romania", "Serbia", "Slovakia", "Slovenia", "Moldova", "Russia", "Latvia",
                 "Malta"]
    capitals = ["Sofia", "Paris", "Berlin", "Rome", "Madrid", "Brussels", "Copenhagen", "Amsterdam", "Oslo", "Warsaw",
               "Lisbon", "Ankara", "Bucharest", "Belgrade", "Bratislava", "Moscow", "Valletta"]
    football_clubs = ["CSKA", "PSG", "Bayren", "Inter", "Barcelona", "Gent", "Ajax", "Legia", "Galatasaray", "Porto",
                     "Partizan", "Spartak", "Real", "Milan", "Juventus", "Liverpool", "Arsenal", "Levski", "Valencia"]

    if category == "countries":
        return random.choice(countries)
    elif category == "capital":
        return random.choice(capitals)
    elif category == "football_club":
        return random.choice(football_clubs)
    else:
        return None


categories = input("Choose category (countries,capital,football_club): ").lower()

if categories not in ["countries", "capital", "football_club"]:
    print("Wrong category!")
else:
    word = choose_word(categories).lower()
    if word is not None:
        print(f"Your category is = {categories}")

        current_category = ["_"] * len(word)
        current_letters = []
        attempts = 10
        while attempts > 0:
            print("Word: "," ".join(current_category))
            print("Attempting to: ", str(attempts))

            input_letter = input("Please enter letter: ").lower()

            if len(input_letter) != 1 or not input_letter.isalpha():
                print("Please enter only one letter")
                continue

            if input_letter in current_letters:
                print("You have already entered this letter")
                continue

            if input_letter not in word:
                print("Incorrect attempt to enter")
                attempts -= 1
            else:
                current_letters.append(input_letter)
                if input_letter in word:
                    for i in range(len(word)):
                        if word[i] == input_letter:
                            current_category[i] = input_letter

            if "".join(current_category) == word:
                print(f"Congratulations! You have found the {categories}!: {word.title()}")
                break

        if attempts == 0:
            print("You lost the game :(")
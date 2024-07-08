#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
import pandas as pd
data = pd.read_csv("./nato_phonetic_alphabet.csv")
data_dict = {row['letter']:row['code'] for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    try:
        user_input = input("Enter a word: ")
        result = [data_dict[word.upper()] for word in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
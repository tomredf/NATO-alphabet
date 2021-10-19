
import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
dt = {row.letter: row.code for(index, row) in df.iterrows()}

loop = True
while loop:
    try:
        word = input("Please enter a word: ").upper()
        result = [dt[letter] for letter in word]
    except KeyError:
        pass
    else:
        error = False
        print(result)


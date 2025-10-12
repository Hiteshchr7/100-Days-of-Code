import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict ={row.letter : row.code for (index,row) in data.iterrows()}

def generate_phonetic():
    user_input = input("Give the word: ")
    try:
        phonetic_list = [phonetic_dict[letter.upper()] for letter in user_input]
    except KeyError :
        print("Please provide a valid input i.e. alphabets.")
        generate_phonetic()
    else :
        print(phonetic_list)
generate_phonetic()
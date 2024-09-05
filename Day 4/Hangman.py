print('''
 _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_| ''')
print()

hangman_list = ['''
  *---*
  |   |
      |
      |
      |
      |
=========''', '''
  *---*
  |   |
  O   |
      |
      |
      |
=========''', '''
  *---*
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  *---*
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  *---*
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  *---*
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  *---*
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Generating a random word which we will need to guess
from wonderwords import RandomWord
word = RandomWord().word()

# Generating no. of blanks as total no. of letters in the word
blanks=["_"]*len(word)
var= "".join(blanks)
print(var)

# Ask the user to guess a letter until game is won or game is over
no_of_lives = 7
a = 7-no_of_lives
hang=False
while no_of_lives > 0  and "_" in blanks:
    guess = input("Guess a letter: ").lower()
    if guess in word and guess not in blanks:
        for i in range(len(word)):
            if word[i]==guess:
                blanks[i]=guess
        var= "".join(blanks)
        print(var)
        if hang:
            print(hangman_list[a])

    elif guess in blanks :
        print("Don't repeat the same letter")

    else :
        no_of_lives = no_of_lives - 1
        a = 7-(no_of_lives+1)
        hang=True
        print(var)
        print(hangman_list[a])
    print(f"Lifes remaining : {no_of_lives}/7 \n")
                
print("Correct Word: ", word)
if "_" in blanks:
    print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_|
                                                               
                                                               ''')
else:
    print('''
__   _____  _   _  __        _____  _   _ 
\ \ / / _ \| | | | \ \      / / _ \| \ | |
 \ V / | | | | | |  \ \ /\ / / | | |  \| |
  | || |_| | |_| |   \ V  V /| |_| | |\  |
  |_| \___/ \___/     \_/\_/  \___/|_| \_|''')



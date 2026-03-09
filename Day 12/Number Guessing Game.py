import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while diff not in ["easy", "hard"]:
    print("Choose a valid response.")
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

num =  random.randint(1,100)
if diff == "easy" :
    no_of_attempts = 10
else :
    no_of_attempts =  5
        
for i in range(no_of_attempts+1):
    if no_of_attempts-i == 0 :
        print("You have run out of guesses. YOU LOSE ")
        print(num)
        break
        
    print(f"You have {no_of_attempts-i} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == num :
        print(f"You got it. The answer was {guess}. YOU WIN!")
        break
    elif guess < num :
        print("Too low.")
        print("Guess again.\n")
    else :
        print("Too high.")
        print("Guess again.\n")



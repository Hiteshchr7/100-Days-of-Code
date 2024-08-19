rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
import random
your_choice = input("Choose: 0 for Rock, 1 for Paper, 2 for Scissors \n")
choices = [rock,paper,scissors]
computers_choice = random.choice(choices)

if your_choice == "0" and computers_choice == rock:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("It's a TIE")

elif your_choice == "0" and computers_choice == paper:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("You Lose")

elif your_choice == "0" and computers_choice == scissors:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("You Win")

elif your_choice == "1" and computers_choice == rock:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("You Win")

elif your_choice == "1" and computers_choice == paper:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("It's a TIE")

elif your_choice == "1" and computers_choice == scissors:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("You Lose")

elif your_choice == "2" and computers_choice == rock:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("You Lose")

elif your_choice == "2" and computers_choice == paper:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("You Win")

elif your_choice == "2" and computers_choice == scissors:
    print(choices[int(your_choice)])
    print(f"Computer chose:\n{computers_choice} ")
    print("It's a TIE")

else:
    print("you didn't choose from given choices.")
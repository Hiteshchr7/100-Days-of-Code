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
your_choice = int(input("Choose: 0 for Rock, 1 for Paper, 2 for Scissors \n"))
choices = [rock,paper,scissors]
computers_choice = random.randint(0,2)

if your_choice != 0 and your_choice != 1 and your_choice != 2 :
    print("INVALID CHOICE !! you didn't choose from given choices of inputs.")

print(f"You Choose: {choices[your_choice]}")
print(f"Computer Choose: {choices[computers_choice]} ")

if your_choice == computers_choice :
    print("It's a DRAW")

elif (your_choice == 0 and computers_choice == 2) or (your_choice == computers_choice + 1) :
    print("You Win")

elif (your_choice == 2 and computers_choice == 0) or (computers_choice == your_choice + 1):
    print("You Lose")
    
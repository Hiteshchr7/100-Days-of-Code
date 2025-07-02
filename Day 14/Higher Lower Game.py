import random
from art import logo,vs
from game_data import data

A = random.choice(data)
score = 0
print(logo)

while True :
    
    B = random.choice(data)
    while B == A :
        B = random.choice(data)
    
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} ")
    print(vs)
    print(f"Against B: {B['name']}, a {B["description"]}, from {B['country']}")


    A_score = A['follower_count']
    B_score = B['follower_count']
    
    evaluate = input("Which has more followers? 'A' or 'B' : ").upper()
    while evaluate not in ["A","B"] :
        print("Please select a valid choice for input.")
        evaluate = input("Which has more followers? 'A' or 'B' : ")
    print(logo)

    if (A_score > B_score and evaluate == "A") or (B_score > A_score and evaluate == "B"):
        score+= 1
        print(f"You are right! Current Score: {score}")
        A = B
        
    else :
        print(f"Sorry, that's wrong. Final Score: {score}")
        break


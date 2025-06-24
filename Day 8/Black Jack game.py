import random
list_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


while True :
    game = input("Do you want to play the game of blackjack? Type 'y' or 'n': ")
    while game!= "y" and game != "n" :
        print("Choose from 'y' or 'n' only. DON'T MAKE INVALID CHOICES") 
        game = input("Do you want to play the game of blackjack? Type 'y' or 'n': ")


    if game == "y" :
        your_cards = random.choices(list_of_cards,k=2)
        computer_cards = random.choices(list_of_cards,k=1)
        print(f"your_cards: {your_cards} , current score: {sum(your_cards)} ")
        print(f"Computer's first card: {computer_cards[0]}")
        if sum(your_cards) == 21 :
                print("Black Jack !!!")
                print("You Win")

        else :
            while sum(your_cards)<=21 :
                choose_next_card = input("Type 'y' to get another card, type 'n' to pass: ")
                while choose_next_card not in ['y','n'] :
                    print("Your choice was not valid. Choose again from given inputs.")
                    choose_next_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if choose_next_card == "n" :
                    while sum(computer_cards) < 18 :
                        computer_cards.append(random.choice(list_of_cards))
                    while sum(computer_cards) > 21 and 11 in computer_cards:
                        computer_cards[computer_cards.index(11)] = 1
            
                    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
                    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                    if sum(computer_cards)>21 :
                        print("Opponent went over. YOU WIN !!! ")   
                    else:
                        if sum(computer_cards) < sum(your_cards) :
                            print("YOU WIN")
                        elif sum(computer_cards) == sum(your_cards) :
                            print("DRAW")
                        else :
                            print("YOU LOSE")
                    break
                        
                            
                else :
                    your_cards.append(random.choice(list_of_cards))
                    while sum(your_cards) >21 and 11 in your_cards :
                        your_cards[your_cards.index(11)]=1
                    print(f"your_cards: {your_cards} , current score: {sum(your_cards)} ")
                    print(f"Computer's first card: {computer_cards[0]}")
                    if sum(your_cards)>21 :
                        print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
                        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                        print("You went over. YOU LOSE !!! ")
                        break
                        
    play_again = input("Do you want to play another game? Type 'y' or 'n': ")
    while play_again != "y" and play_again != "n":
        print("Choose from 'y' or 'n' only.")
        play_again = input("Do you want to play another game? Type 'y' or 'n': ")
    if play_again == "n":
        print("Thanks for playing. Goodbye!")
        break
        
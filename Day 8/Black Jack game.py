import random



def bust(l1):
    return sum(l1) > 21

# Case for Ace :

def ace() :
    if 11 in your_cards and your_score > 21 :
        for card in your_cards :
            if card == 11 :
                card = 1
        return list(your_cards)
        
    if 11 in computer_cards and sum(computer_cards) > 21 :
        for card in computer_cards :
            if card == 11 :
                card = 1
        return list(computer_cards)
####################################################################################################################

cards_list = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]

your_cards = list(random.choices(cards_list,k=2))
your_score = sum(your_cards)

computer_cards = list(random.choices(cards_list))

print(f"Your Cards: {your_cards}, Current Score: {your_score}")
print(f"Computer's first card: {computer_cards[0]}")

if your_score == 21 :
    print("Black Jack !!!")
    print("You Win")

else :

    choose_next_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while choose_next_card not in ['y','n'] :
        print("Your choice was not valid. Choose again from fiven inputs.")
        choose_next_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if choose_next_card == 'n' :
        computer_score = sum(computer_cards)

        while computer_score <= 21 :
            computer_cards.append(random.choice(cards_list))
            ace()
            print(computer_cards)
            if  sum(computer_cards) > 21:
                computer_cards.pop()
                if sum(computer_cards) <=15 :
                    computer_cards.append(random.choice(cards_list))
                    ace()
                    sum(computer_cards)
                break

            computer_score = sum(computer_cards)

        
        if sum(computer_cards) > 21 :
            print(f"Your final hand: {your_cards}, Final Score: {your_score}")
            print(f"Computer's final hand: {computer_cards}, Final Score: {sum(computer_cards)} ")
            print("Your opponent went over. You Win")
        else :
            print(f"Your final hand: {your_cards}, Final Score: {your_score}")
            print(f"Computer's final hand: {computer_cards}, Final Score: {sum(computer_cards)} ")
            if your_score > sum(computer_cards) :
                print("Your opponent's score is less than yours. You Win")
            elif your_score < sum(computer_cards) :
                print("Your opponent's score is more than yours. You lose. ")
            else :
                print("It's a draw. ")
    else:
        pass
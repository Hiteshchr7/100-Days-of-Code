logo = """
                          _________
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''----------'' '-'
                          )"""""""(
                         |_________|
                         
                       .-------------.
                      /_______________\ """
print(logo,'\n')

def max_bid(bid_data):
    highest_bid = 0
    winner = ""
    for bidder in bid_data :
        bid_value = bid_data[bidder]
        if bid_value > highest_bid :
            highest_bid = bid_value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

start = True
data = {}
while start :
    
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $")) 
    print()
    data[name] = bid

    next_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while next_bid != 'yes' and next_bid !=  'no' :
        print("You didn't choose from specified inputs. Choose Again from 'yes' or 'no'")
        next_bid = input("Are there any other bidders? Type 'yes' or 'no'.")
    if next_bid == "no" :
        
        start = False
        max_bid(data)
    


size = input("Size of pizza you need? S,M or L: ")
pepperoni = input("If you want to add pepperoni on pizza? Y or N: ")
extra_cheese = input("Do you need extra cheese on pizza? Y or N: ")

#creating a variable bill to get bill for different cases
bill = 15

if size == "S":

    if pepperoni == "Y" :
        bill += 2
    else:
        pass
    if extra_cheese =="Y":
        bill += 1
    else :
        pass

elif size == "M":
    bill += 5 
    if pepperoni == "Y" :
        bill += 3
    else:
        pass
    if extra_cheese =="Y":
        bill += 1
    else :
        pass

elif size == "L":
    bill += 10 
    if pepperoni == "Y" :
        bill += 3
    else:
        pass
    if extra_cheese =="Y":
        bill += 1
    else :
        pass
else:
    pass

print(f"Total bill for your pizza is: {bill}$")
         


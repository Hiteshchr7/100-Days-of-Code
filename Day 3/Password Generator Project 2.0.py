#Password Generator Project Without use of Loops 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_of_letters= int(input("How many letters would you like in your password?\n")) 
no_of_symbols = int(input(f"How many symbols would you like?\n"))
no_of_numbers = int(input(f"How many numbers would you like?\n"))

letter=random.choices(letters,k=no_of_letters)
num=random.choices(numbers,k=no_of_numbers)
sym=random.choices(symbols,k=no_of_symbols)
arr=letter+num+sym


#Eazy Level - Order not randomised:
ans=''.join(arr)
print(ans)

#Hard Level - Order of characters randomised:
random.shuffle(arr)
ans=''.join(arr)
print(ans)



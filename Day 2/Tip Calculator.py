# calculating amount to be paid by each person after giving some tip 

print("Welcome to Tip Calculator")

bill = float(input("Total Bill is: $"))
tip = float(input("Tip given(10%, 12%, 15%, etc) = "))
people = int(input("People among which we are splitting the bill: "))
bill_with_tip = bill + bill*tip/100
each_person_amount = round(bill_with_tip/people, 2)

print(f"Each person should pay: ${each_person_amount}")
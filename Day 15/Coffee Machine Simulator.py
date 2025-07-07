MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

def validate_input(prompt, valid_inp_list ):
    inp = input(prompt)
    while inp not in valid_inp_list :
        print("Please enter a valid input.")
        inp = input(prompt)
    return inp

def check_suff_res(res,ask):

    for key in MENU :
        if ask == key :
            for ingredient in MENU[key]["ingredients"] :
                    if res[ingredient] < MENU[key]["ingredients"][ingredient]:
                        print(f"Sorry there's not enough {ingredient}.") 
                        return False
            return True                
    return False       


ask = validate_input("What would you like? (espresso/latte/cappuccino):",["report","off","latte","cappuccino","espresso"])

while ask != "off" :

    if ask == "report" :
        for key in resources :
            if key != "coffee" :
                print(f"{key.title()}: {resources[key]}ml")  
            else :
                print(f"{key.title()}: {resources[key]}g")
        print(f"Money: ${money}")


    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    for key in MENU :
        if ask == key :

            if check_suff_res(resources,ask) == True :
                print("Please insert the coins.")
                quarters =  int(input("How many quarters?: "))
                dimes =  int(input("How many dimes?: "))
                nickels =  int(input("How many nickels?: "))
                pennies =  int(input("How many pennies?: "))
                total_money_received = quarter*quarters + dime*dimes + nickel*nickels + penny*pennies
                change = 0

                change = round(total_money_received - MENU[key]["cost"],2)
                if change >=0 :
                    for ingredient in MENU[key]["ingredients"] :
                        resources[ingredient] -=  MENU[key]["ingredients"][ingredient]
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {key}☕ Enjoy!")
                    money += MENU[key]["cost"]
                else :
                    print("Sorry that's not enough money. Money Refunded.")
    ask = validate_input("What would you like? (espresso/latte/cappuccino):",["report","off","latte","cappuccino","espresso"])






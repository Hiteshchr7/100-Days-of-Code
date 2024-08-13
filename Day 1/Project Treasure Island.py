# Interesting use of Ascii art for our project
X =''' 
*****************************************************************************
______________|_____________|_______________|______________|_______________|___
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************'''

print('''Welcome to Treasure Island.
Your mission is to find the great treasure.''')

# You start by choosing one path out of right and left path for island.
path = input("R or L: ").upper()
if path == "R" :
    print("Game Over [Died due to falling in deep pit.]")
#Choose the way to cross the lake for treasure island
elif path == "L" :
    way = input("Swim or Wait for Boat? S or B: ").upper()
    if way == "S" :
        print("Game Over [Died by drowning/Eaten by crocodiles.]")
#Choose The Door of treasure to win the treasure
    elif way == "B" :
        treasure_door = input("red,yellow or blue door: ").lower()
        if treasure_door == "red" :
            print("Game Over [Died due to fire behind red door.]")
        elif treasure_door == "blue" :
            print(" Game Over [Died by falling from chasm.]")
        elif treasure_door == "yellow":
            print(f"""YOU WON THE TREASURE !!!
                  {X}""")
else :
    print("typing error or wrong choice of selection.")

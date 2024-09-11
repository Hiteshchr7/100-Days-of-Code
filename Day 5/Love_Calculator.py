# Love Compatibility calculator (Makes use of user-defined function, loops, lists, strings and their methods)
def calculate_love_score(name_1,name_2):
    true_list = ["T","R","U","E"]
    love_list = ["L","O","V","E"]   
    num_true_list = []
    num_love_list = []  

    for letter in true_list :
        letters_of_true = name_1.upper().count(letter) + name_2.upper().count(letter)
        num_true_list.append(letters_of_true) # total number of each letters of word TRUE in name 1 and 2 combined
    total_1 = sum(num_true_list)    
    for letter in love_list :
        letters_of_love = name_1.upper().count(letter) + name_2.upper().count(letter)
        num_love_list.append(letters_of_love) # total number of each letters of word LOVE in name 1 and 2 combined
    total_2 = sum(num_love_list)

    if total_2 >= 10 :
        total_2 = 0
        if total_1 > 10 :
            total_1 = 10
        else :
            pass

    print(f"Love compatibility between {name_1} & {name_2} is {total_1}{total_2}/100")

calculate_love_score(input("Name of first person: "),input("Name of second person: "))
# Logic used for calculating love score is the number of times letters of word TRUE and LOVE come in names of 2 persons then we take sum of them and put them in ten's and one's place to give the score
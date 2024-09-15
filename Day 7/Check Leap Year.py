def is_leap_year(year):

    if year%4 != 0 :
        return False
    else :
        if year % 100 != 0 :
            return True
        elif year % 100 == 0 and year % 400 != 0 :
            return False
        elif year % 100 == 0 and year % 400 == 0 :
            return True


year_to_check = int(input("Year you want to check for leap year is: "))
                    
print(f"Is {year_to_check} a leap year?\n",is_leap_year(year_to_check),sep="")
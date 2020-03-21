# Link - https://www.hackerrank.com/challenges/day-of-the-programmer/

def dayOfProgrammer(year):
    
    is_leap = bool()
    if year == 1918:
        return "26.09.1918"
    
    elif year >= 1700 and year <= 1917:
        is_leap = False if year % 4 else True

    elif year >=1919:
        if year % 4 == 0 and year % 100 == 0:
            is_leap = True
        elif year % 400 == 0:
            is_leap = True
        else:
            is_leap = False

    return "12.09."+str(year) if is_leap else "13.09."+str(year)

print(dayOfProgrammer(2016))

    

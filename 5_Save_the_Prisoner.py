# https://www.hackerrank.com/challenges/save-the-prisoner/problem

def saveThePrisoner(prisoners_count, candies_count, starting_seat):
    prisoner_seats = list(range(1,prisoners_count+1))
    is_starting_seat_served = False
    last_prisoner_seat = 0
    
    while candies_count != 0:
        if not is_starting_seat_served:
            is_starting_seat_served = True
            for i in range(starting_seat,len(prisoner_seats)+1):
                print(i, candies_count)
                if candies_count == 0:
                    last_prisoner_seat = i-1
                    break
                else:
                    candies_count -= 1
        else:
            for i in range(1, len(prisoner_seats)+1):
                print(i, candies_count)
                if candies_count == 0:
                    last_prisoner_seat = i-1
                    break
                else:
                    candies_count  -= 1
    if last_prisoner_seat == 0:
        last_prisoner_seat = prisoners_count
    return last_prisoner_seat

print(saveThePrisoner(7, 19, 2))
print("=============")
# print(saveThePrisoner(3,7,3))
# print("=============")
# print(saveThePrisoner(5,2,1))
# print("=============")
# print(saveThePrisoner(5,2,2))
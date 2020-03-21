# https://www.hackerrank.com/challenges/counting-valleys/problem
from time import time
def countingValleys(steps_count, steps):
    # Valley = path goes down from sea level then comes back to the sea level
    steps = list(steps)
    valleys = 0
    is_went_down = False
    is_went_up = False
    altitude = 0
    for step in steps:
        altitude = altitude-1 if step == "D" else altitude +1
        if step == "D" and not is_went_up:
            is_went_down = True
            
        elif step == "U" and not is_went_down:
            is_went_up = True
        
        if altitude == 0:
            if is_went_down:
                valleys+=1
                is_went_down = False
            elif is_went_up:
                is_went_up = False
    
    return valleys



if __name__ == '__main__':
    start_time = time()
    
    n = 8
    s = "DDUUDDUDUUUD"
    result = countingValleys(n, s)
    print(result)
    print("---------------------")
    n = 8
    s = "UDDDUDUU"
    result = countingValleys(n, s)
    print(result)

    passed_time = time() - start_time
    print(f"It took {passed_time}")
 
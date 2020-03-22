# https://www.hackerrank.com/challenges/electronics-shop/problem
from time import time

def getMoneySpent(keyboards, drives, b):
    currentMaxVal = 0
    for keyboard in keyboards:
        for drive in drives:
            if keyboard+drive <= b and keyboard+drive > currentMaxVal:
                currentMaxVal = keyboard+drive

    return -1 if currentMaxVal == 0 else currentMaxVal


if __name__ == '__main__':
    start_time = time()

    result = getMoneySpent([3,1], [5,2,8], 10)
    print(result)
    print("---------------------------")

    result = getMoneySpent([4], [5], 5)
    print(result)
    print("---------------------------")

    result = getMoneySpent([40,50,60], [5,8,12], 60)
    print(result)
    print("---------------------------")

    passed_time = time() - start_time
    print(f"It took {passed_time}")
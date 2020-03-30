# https://www.hackerrank.com/challenges/picking-numbers/problem
import itertools

def pickingNumbers(a):
    result_set = []
    # power_set = list(itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(2, len(a)+1)))
    
    for n in range(2, len(a)+1):
        power_set = list(itertools.combinations(a,n))
        for subset in power_set:
            all_diff = False
            for index, number_1 in enumerate(subset):
                for number_2 in subset[index+1:]:
                    if int(((number_1 - number_2)**2)**0.5) > 1:
                        all_diff = False
                        break
                    else:
                        all_diff = True
                if all_diff is False:
                    break
            
            if all_diff:
                result_set = subset
    
    return len(result_set)

if __name__ == '__main__':
    # print(pickingNumbers([4,6,5,3,3,1]))
    # print("==============================")
    # print(pickingNumbers([1,2,2,3,1,2]))
    # print("==============================")
    # print(pickingNumbers([1,1,2,2,4,4,5,5,5]))
    x = "4 2 3 4 4 9 98 98 3 3 3 4 2 98 1 98 98 1 1 4 98 2 98 3 9 9 3 1 4 1 98 9 9 2 9 4 2 2 9 98 4 98 1 3 4 9 1 98 98 4 2 3 98 98 1 99 9 98 98 3 98 98 4 98 2 98 4 2 1 1 9 2 4"
    print(pickingNumbers(list(map(int, x.split()))))
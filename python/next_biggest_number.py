#!/usr/bin/python3
import sys

def main():
    print(next_biggest_number(sys.argv[1]))


def next_biggest_number(num):
    number = int(num)
        
    # deal with Zero as it is a known bad result
    if number == 0:
        return -1
    #check for decending order it is also a known bad result
    if isDescending(number):
        return -1

    if number > 0:
        return next_biggest_positive(number)

    return -1

def isDescending(num):
    ListOfValues = [x for x in str(num)]
    for i in range( len(ListOfValues) - 1 ):
        if ListOfValues[i] < ListOfValues[i+1]:
            return False
    return True

def next_biggest_positive(num):
    
    ListOfValues = [x for x in reversed(str(num))]

    first_number = -1
    second_number = -1
    for index,val in enumerate(zip(ListOfValues, ListOfValues[1:])):
        if val[0] > val[1]:
            first_number = index +1
            break

    smallest = int(10)
    smallest_index = -1
    for index,lp in enumerate(ListOfValues[:first_number]):
        
        if int(lp) < int(smallest) and int(lp) > int(val[1]):
            smallest = lp
            smallest_index = index

    
    ListOfValues[first_number],ListOfValues[smallest_index] = ListOfValues[smallest_index],ListOfValues[first_number]
    newlist = sorted(ListOfValues[:first_number],reverse=True) + ListOfValues[first_number:]
    result = int(''.join(reversed(newlist)))
    

    return result


if __name__ == "__main__":
    main()




#!/usr/bin/python3
import sys

def main():
    print(next_biggest_number(sys.argv[1]))


def next_biggest_number(num):
    number = int(num)
    #print(number)    
    # deal with Zero as it is a know result
    if number == 0:
        return -1
    #check for decending order
    if isDescending(number):
        return -1

    if number > 0:
        return next_biggest_positive(number)

    # prob need to make positive
    #ListOfValues = [int(x) for x in str(num)]
    #print(ListOfValues)
    return 0

def isDescending(num):
    ListOfValues = [x for x in str(num)]
    for i in range( len(ListOfValues) - 1 ):
        if ListOfValues[i] < ListOfValues[i+1]:
            return False
        return True

def next_biggest_positive(num):
    #print("positive")
    ListOfValues = [x for x in reversed(str(num))]
    #print(ListOfValues)

    first_number = -1
    second_number = -1
    for index,val in enumerate(zip(ListOfValues, ListOfValues[1:])):
        if val[0] > val[1]:
            first_number = index +1
            break

    #print(first_number, val[1])
    #print(ListOfValues[:first_number])
    #print(min(ListOfValues[:first_number]))

    smallest = int(10)
    smallest_index = -1
    for index,lp in enumerate(ListOfValues[:first_number]):
        #print(index,lp)
        if int(lp) < int(smallest) and int(lp) > int(val[1]):
            smallest = lp
            smallest_index = index

    
    ListOfValues[first_number],ListOfValues[smallest_index] = ListOfValues[smallest_index],ListOfValues[first_number]
    newlist = sorted(ListOfValues[:first_number],reverse=True) + ListOfValues[first_number:]
    result = ''.join(reversed(newlist))
    #print(result)

    return result


if __name__ == "__main__":
    main()




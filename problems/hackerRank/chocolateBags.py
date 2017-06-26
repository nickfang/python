#!/bin/python3

import sys

def minimumChocolateMoves(n, X):
    # Complete this function
    # Check if nothing needs to be moved
    movesNeeded = []
    numberOfChocolates = 0
    extraChocolatesInUnsetBags = 0
    extraChocolatesInSetBags = 0
    numBagsThatNeedChocolate = 0
    for index, value in enumerate(X):
        numberOfChocolates += value
        # if we're on an odd index and have an even number of vice versa,
        if ((index % 2 == 1) and (value % 2 == 0)) or \
           ((index % 2 == 0) and (value % 2 == 1)):
            # save the index of this bag
            movesNeeded.append(index)
            # if the bag has more than one chocolate, it can donate an odd number of chocolates
            if value > 1:
                extraChocolatesInUnsetBags += value - 1
            else:
                # if it only has one chocolate, it is a chocolate consumer.
                numBagsThatNeedChocolate += 1
        if index % 2 == 0:
            extraChocolatesInSetBags += value - 2
        else:
            extraChocolatesInSetBags += value -1

    # all even indexes are even and all odd indexes are odd
    if len(movesNeeded) == 0:
        return 0

    # check for basic invalid cases
    numOddBags = len(X[1::2])
    # if there are an odd number of odd bags and an even number of all chocolates or
    # if there are an even number of odd bags and an odd number of all chocolates
    # then there's going to be a chocolate that doesn't fit anywhere
    if (numOddBags % 2 == 1 and numberOfChocolates % 2 == 0) or \
       (numOddBags % 2 == 0 and numberOfChocolates % 2 == 1):
        return -1

    # if there are not enough chocolates to satisfy a minimun number of chocolates in each bag
    minNumChocolates = len(X[::2]) * 2 + numOddBags
    if numberOfChocolates < minNumChocolates:
        return -1

    # TODO: figure out the number of chocolates that need to be moved
    # first fill all the chocolate consumers.
    # then figure out if the leftover bags
    numMovesNeeded = 0
    if (len(movesNeeded) - numBagsThatNeedChocolate) // 2 > extraChocolatesInUnsetBags:
        numMovesNeeded = (len(movesNeeded) - numBagsThatNeedChocolate) // 2

    numMovesNeeded += numBagsThatNeedChocolate
    return numMovesNeeded


#  Return the minimum number of chocolates that need to be moved, or -1 if it's impossible.
with open("chocolateBagsData.txt", "r") as f:
    q = int(f.readline().strip())
    for a0 in range(q):
        n = int(f.readline().strip())
        X = list(map(int, f.readline().strip().split(' ')))
        result = minimumChocolateMoves(n, X)
        print(result)
# q = int(input().strip())
# for a0 in range(q):
#     n = int(input().strip())
#     X = list(map(int, input().strip().split(' ')))
#     result = minimumChocolateMoves(n, X)
#     print(result)
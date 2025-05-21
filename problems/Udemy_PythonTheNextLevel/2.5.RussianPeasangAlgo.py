##: The Russian Peasant's Algorithm
##: Been around for a long long time. (Seventeenth Century B.C.)

##: Multiply two numbers together.
##: Requirements: multiply by 2, divide by 2, and Add numbers

##: AKA =  Mediation and Duplation Method

##:
##: Inputs ->  two numbers
##: Output ->  the solution to those two numbers
##:             multiplied together using the Russian Peasent Algorithm

# 17 in base 2:  10001 = 17           10001
#                 >> 1                 << 1
#                 1000 = 8           100010 = 34
import math


def russian(a,b):
    sum = 0
    while a > 1:
        a =  a // 2
        b = b * 2
        if a % 2 != 0:
            sum += b
    print("answer: ", sum)

def russian2(a,b):
    sum = 0
    while a > 1:
        a = a >> 1
        b = b << 1
        if a % 2 != 0:
            sum += b
    print("answer: ", sum)

print("Russian Peasant's Algorithm")
russian(8, 13)
russian(238, 13)
russian(24, 16)
russian2(8, 13)
russian2(238, 13)
russian2(24, 16)

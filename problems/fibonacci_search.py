#!/bin/python3

fibonacci = [1,2,3,5,8,13,21,34,55,89]

# this function assumes that arr is sorted
def fibonacci_search(arr, value):
   if len(arr) == 0:
      return -1
   
   if arr[0] == value:
      return 0
   if len(arr) == 1:
      if arr[0] != value:
         return -1
   
   fib_index = 0
   base_index = 0
   length = len(arr)
   while True:
      current_value = arr[fibonacci[fib_index]+base_index]
      if current_value == value:
         return fibonacci[fib_index]+base_index 
      elif current_value < value:
         fib_index += 1
         if fibonacci[fib_index]+base_index >= length:
            # add previous fibonacci number to base and start over with sequence
            base_index = base_index+fibonacci[fib_index-1]
            fib_index = 0
            # got to the end and didn't find the number (number is bigger than any number in arr)
            if base_index+fibonacci[fib_index] >= length:
               return -1
      elif current_value > value:
         if fib_index == 0:
            return -1
         base_index = fibonacci[fib_index-1]
         fib_index =0
       

print(fibonacci_search([0], 2)==-1)
print(fibonacci_search([0], 0)==0)
print(fibonacci_search([0,1], 0)==0)
print(fibonacci_search([0,1], 1)==1)
print(fibonacci_search([0,10], 2)==-1)
print(fibonacci_search([0,1,2,3,4], 2)==2)
print(fibonacci_search([0,1,3,5,7], 7)==4)
print(fibonacci_search([0,1,3,5,7], 4)==-1)
print(fibonacci_search([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], 15)==15)
print(fibonacci_search([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22], 25)==-1)
print(fibonacci_search([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 15)==15)
print(fibonacci_search([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30], 24)==12)


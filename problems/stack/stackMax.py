# You have an empty sequence, and you will be given N queries. Each query is one of these three types:

# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.


# Sample Input
# 10
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 2
# 3
# 1 91
# 3

# Sample Output
# 26
# 91

def getMax(stack):
  max = 0
  stack = [int(x) for x in stack]
  for itr in stack:
    if itr > max:
      max = itr
  return max

def maximumElement():
  stack = []

  n = input()
  max = 0
  for x in range(int(n)):
    query = input()
    parts = query.split(" ")
    if parts[0] == "1":
      val = int(parts[1])
      if val > max:
        max = val
      stack.append(val)
    elif parts[0] == "2":
      val = stack.pop()
      if max == val:
        max = getMax(stack)
    elif parts[0] == "3":
      print(max)


# From Hacker Rank: https://www.hackerrank.com/challenges/balanced-brackets

# Sample Input:
# 3
# {[()]}
# {[(])}
# {{[[(())]]}}

# Sample Output
# YES
# NO
# YES

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
  s = input().strip()
  if len(s) % 2 != 0:
    print("NO")
    break
  stack = []
  balanced = "YES"
  for itr in s:
    if itr in "{([":
      stack.append(itr)
    else:
      if len(stack) == 0:
        balanced = "NO"
        break
      closing = stack.pop()
      if itr in "}" and closing not in "{":
        balanced = "NO"
        break
      elif itr in ")" and closing not in "(":
        balanced = "NO"
        break
      elif itr in "]" and closing not in "[":
        balanced = "NO"
        break;
  if len(stack) != 0:
    print("NO")
  else:
    print(balanced)
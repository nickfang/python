#!/bin/python3

import sys

def checkBrackets(s):
    bracketStack = []
    # if there is an odd number of characters in the string
    if len(s) % 2 == 1:
        return "NO"
    for bracket in s:
        if bracket in "{[(":
            bracketStack.append(bracket)
        elif bracket in "}])":
            # if there is no opening bracket on the stack that corresponds with the closing bracket
            if len(bracketStack) == 0:
                return "NO"
            openBracket = bracketStack.pop()
            if (bracket in "}" and openBracket in "{") or \
               (bracket in "]" and openBracket in "[") or \
               (bracket in ")" and openBracket in "("):
                continue
            else:
                return "NO"
    if len(bracketStack) == 0:
        return "YES"
    else:
        return "NO"

# t = int(input().strip())
# for a0 in range(t):
#     s = input().strip()
#     print(checkBrackets(s))

# YES
print(checkBrackets("{[()]}"))
# NO
print(checkBrackets("{[(])}"))
# YES
print(checkBrackets("{{[[(())]]}}"))
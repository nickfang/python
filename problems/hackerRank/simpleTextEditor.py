#!/bin/python3

# create a simple text editor.
# 1. append(W) - append stringW to the end of S
# 2. delete(k) - delete the last k characters of S
# 3. print(k) - print the kth character of S
# 4. undo - undo the last (previously undone) operation of type 1 or 2,
#           reverting S to the state it was in prior to that operation.

t = int(input().strip())
S = ""
undoStack = []
for _ in range(t):
    s = input().strip()
    command = s.split(" ")
    # Append to String
    if command[0] == "1":
        S = S + command[1]
        undoStack.append("{0} {1}".format("1",command[1]))
    # Remove last k letters
    elif command[0] == "2":
        deletedString = S[-int(command[1]):]
        S = S[0:-int(command[1])]
        undoStack.append("{0} {1}".format("2", deletedString))
    # Print the current String
    elif command[0] == "3":
        print(S[int(command[1])-1])
    # Undo the last command
    elif command[0] == "4":
        undoCommand = undoStack.pop().split(" ")
        if undoCommand[0] == "1":
            S = S[0:-len(undoCommand[1])]
        elif undoCommand[0] == "2":
            S = S + undoCommand[1]
    #print(command, ": ", S)

# input
# 8
# 1 abc
# 3 3
# 2 3
# 1 xy
# 3 2
# 4
# 4
# 3 1

# output
# c
# y
# a
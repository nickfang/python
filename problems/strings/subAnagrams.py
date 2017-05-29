import random
import string
import time


def checkAnagram(word1, word2):
    # create a sorted list of each word.  Compare letters until something doesn't match or there are no more letters.
    # size of the words passed in are expected to be the same
    # this will exit pretty quick if they are not anagrams
    chars1 = sorted([char for char in word1])
    chars2 = sorted([char for char in word2])
    for x,val in enumerate(chars1):
        if val != chars2[x]:
            return False
    return True

def checkAnagram2(word1, word2):
    chars = {}
    # create dict of chars in first word
    for char in word1:
        if char in chars:
            chars[char] += 1
        else:
            chars.setdefault(char, 1)
    # go through each letter in second word and remove from dict.
    for char in word2:
        if char in chars:
            # decrement letter and remove if necessary
            if chars[char] == 1:
                chars.pop(char)
            else:
                chars[char] -= 1
        # if char (letter in word2) is not in chars (letters in word1), not an anagram
        else:
            return False
    return True



# RETURN AN EMPTY LIST IF NO ANAGRAM FOUND
def getAnagramIndices(haystack, needle, checkAnagramFunction):
    # WRITE YOUR CODE HERE
    results = []
    # if there is nothing to search for return an empty list
    if len(needle) == 0:
        return results

    # if haystack has less letters than needles, we don't have to check it
    if len(haystack) < len(needle):
        return results

    # if needle is just one letter do a search through the string
    if len(needle) == 1:
        for x, char in enumerate(haystack):
            if char == needle:
                results.append(x)
        return results

    # get segments of haystack that are the same size as needle and pass both into checkAnagram()
    # if nothing is found, an empty list is returned
    for x in range(0, len(haystack) - len(needle)):
        if checkAnagramFunction(haystack[x:len(needle)+x] , needle):
            results.append(x)

    return results

# 3 of 11 passed

def getRandomString(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

haystack = getRandomString(100000)
needle = getRandomString(1000)

startTime = time.time()
result = getAnagramIndices(haystack, needle, checkAnagram)
endTime = time.time() - startTime
print("Method1: ", endTime)

startTime = time.time()
result = getAnagramIndices(haystack, needle, checkAnagram2)
endTime = time.time() - startTime
print("Method2: ", endTime)

# for x in result:
#     print(haystack[x:x+len(needle)])
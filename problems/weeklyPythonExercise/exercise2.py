def read_n(filename, numLines):
    if not isinstance(numLines, int):
        print("Please provide an integer for the number of lines parameter")
        return
    if numLines < 1:
        print("Please specify a positive number of lines")
        return
    with open(filename, 'r') as fileObj:
        lineCount = 0
        output = ""
        for line in fileObj:
            lineCount += 1
            output += line
            # trying to be a little memory effecient here if the file is huge then the lineCount could get very large.
            # resetting to 0 will keep it from taking any extra memory
            if lineCount == numLines:
                yield output
                lineCount = 0
                output = ""
        yield output


def read_n2(filename, numlines):
    with open(filename, 'r') as f:
        pass

for lines in read_n('exercise2.txt', 4):
    print(lines)
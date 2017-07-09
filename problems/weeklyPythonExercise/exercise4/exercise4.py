#!python3

import re

logData = []
with open("mini-access-log.txt", "r") as fileObj:
    for line in fileObj:
        logParse = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\[(.*?)\]\s\"(.*?)\"")
        # logParse = re.compile(".*")
        dataElement = {}
        components = logParse.search(line)
        dataElement["ip_address"] = components.group(1)
        dataElement["timestamp"] = components.group(2)
        dataElement["request"] = components.group(3)
        logData.append(dataElement)
print(len(logData))
# for data in logData:
#     print(data)

#from solution

def lineToDict(lineFromLog):
    regexFilter = ('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'   # match ip address
                   '.*?'                                    # stuff in between ip address and date string
                   '\[(.*?)\]'                              # match date string, don't include include []
                   '\s'                                     # date string and request are separated by a space.
                   '\"(.*?)\"')                             # match request
    logParse = re.compile(regexFilter)
    components = logParse.search(lineFromLog)
    dataElement = {}
    dataElement["ip_address"] = components.group(1)
    dataElement["timestamp"] = components.group(2)
    dataElement["request"] = components.group(3)
    return dataElement

def logToDict(filename):
    return [lineToDict(line) for line in open(filename)]

for data in logToDict("mini-access-log.txt"):
    print(data)
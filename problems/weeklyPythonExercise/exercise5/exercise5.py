#!python3

import re
import time
import operator

# t = strptime('31/Jan/2010:21:08:00 +0200', '%d/%b/%Y:%H:%M:%S %z')
# sys.getsizeof(t) => 120
# sys.getsizeof('31/Jan/2010:21:08:00 +0200') => 75
# The size of a string is a little more than half of the size of a time object, so store the timestamp as a string

class ListOfDicts(object):
    def __init__(self, logFile):
        # [self.lineToDict(line) for line in open(logFile, 'r')]
        self._timeFormat = '%d/%b/%Y:%H:%M:%S %z'
        with open(logFile, 'r') as fileObj:
            self._logData = [self.lineToDict(line) for line in fileObj]

    def lineToDict(self, line):
        regEx = ('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'    # ip address
                 '.*?'                                     # ---
                 '\[(.*?)\]'                               # timestamp always between []
                 '\s'                                      # ---
                 '\"(GET.*?)\"')                           # request that starts with GET

        logParse = re.compile(regEx)
        components = logParse.search(line)
        if components:
            ip_address = components.group(1)
            timestamp = components.group(2)
            request = components.group(3)
        else:
            ip_address, timestamp, request = "", "", ""

        #if nothing is found
        dataElement = { "ip_address": ip_address,
                        "timestamp": timestamp,
                        "request": request }
        return dataElement

    def iterdicts(self, searchKey=None):
        if searchKey:
            return (dataElement for dataElement in sorted(self._logData, key=lambda d: d[searchKey]))
        else:
            return (dataElement for dataElement in self._logData)

    def dicts(self, searchKey=None):
        return list(self.iterdicts(searchKey))

    def earliest(self):
        return min(self._logData, key=lambda d: time.strptime(d['timestamp'], self._timeFormat))

    def latest(self):
        return max(self._logData, key=lambda d: time.strptime(d['timestamp'], self._timeFormat))

    def forIP(self, ipAddress, key=None):
        return [dataElement for dataElement in self._logData if ipAddress == dataElement['ip_address']]

    def forRequest(self, text, key=None):
        return [dataElement for dataElement in self._logData if text in dataElement['request']]

ld = ListOfDicts("mini-access-log.txt")
print(ld.dicts())
print(type(ld.dicts()))
print(type(ld.iterdicts()))
print(ld.earliest())
print(ld.latest())
print(ld.forIP('67.218.116.165'))
print(ld.forRequest('one_node'))
print(ld.dicts("ip_address"))
for dataElement in ld.iterdicts("ip_address"):
    print(dataElement)
# print(ld.dicts(key=operator.itemgetter('request')[0]))
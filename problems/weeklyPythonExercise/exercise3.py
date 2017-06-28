#!/bin/python3

def myrange2(par1, *pars):
    step = 1
    if len(pars) == 0:
        begin = 0
        end = par1
    else:
        begin = par1
        end = pars[0]
        if len(pars) == 2:
            step = pars[1]
    output = []
    count = begin
    while count < end:
        output.append(count)
        count += step
    return(output)


def myrange3(par1, *pars):
    step = 1
    if len(pars) == 0:
        begin = 0
        end = par1
    else:
        begin = par1
        end = pars[0]
        if len(pars) == 2:
            step = pars[1]
    output = []
    count = begin
    while count < end:
        yield count
        count += step

print(myrange2(5))
print(myrange2(5,10))
print(myrange2(5,20,4))

for x in myrange3(5):
    print(x)
print()

for x in myrange3(15,10):
    print(x)
print()

for x in myrange3(5,20,3):
    print(x)
print()
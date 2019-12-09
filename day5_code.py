# Advent of code 2019 day 5

import numpy as np

filename = 'day5_input.txt'
datopen = open(filename)
data = datopen.read()
data = data.split(',')

indat = [0] *len(data)
for i in range(len(data)):
    indat[i] = int(data[i])

rules = {'1110':'f,s,st = clist[index+1],clist[index+2],index+3','1100':'s,st = clist[index+2],index+3','1010':'f,st = clist[index+1],index+3','1000':'st = index+3','110':'f,s = clist[index+1],clist[index+2]','100':'s = clist[index+2]','10':'f = clist[index+1]'}
#operation = {1:'add', 2:'multiply', 3:'input', 4:'output'}

# function takes in code and decides what to do
def whatdo(clist,index,rule):
    #rules = {'1110':'f,s,st = clist[index+1],clist[index+2],index+3','1100':'s,st = clist[index+2],index+3','1010':'f,st = clist[index+1],index+3','1000':'st = index+3','110':'f,s = clist[index+1],clist[index+2]','100':'s = clist[index+2]','10':'f = clist[index+1]'}
    n = len(str(clist[index]))
    # f is first, s is second, and st is store
    #debug
    print('your code and params:',clist[index:index+4])
    opcdstr = str(clist[index])
    #debug
    print(n)
    try:
        f = clist[clist[index+1]]
    except:
        pass
    try:
        s = clist[clist[index+2]]
    except:
        pass
    try:
        st = clist[index+3]
        #opcdstr = str(clist[index])
    except:
        pass
    if n > 1:
        param = opcdstr[:-1]
        exec(rules[param])
        #debug
        print(rules[param])
        print(f)
    if opcdstr[-1] == '1':
        clist[st] = f + s
        if n > 1:
            print('f should be',rules[param],'...',clist[index+1],', this is what f is:',f)
    else:
        clist[st] = f * s
    index += 4
    print('done')
    return index
    
    
itt = 0

while indat[itt] != 99:
    if indat[itt] == 3:
        indat[indat[itt+1]] = int(input('Please enter the starting value 1:'))
        itt += 2
        # debug
        #print('3')
    elif indat[itt] == 4:
        print(indat[indat[itt+1]])
        itt += 2
    elif indat[itt] == 104:
        print(indat[itt+1])
        itt += 2
    else:
        itt = whatdo(indat,itt,rules)

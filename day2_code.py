# Advent of code 2019 day 2

#import numpy as np

#practice set
#datinss ='1,9,10,3,2,3,11,0,99,30,40,50\n'

filename = 'day2_input.txt'
datin = open(filename)
datinss = datin.readline()
datas = datinss.split(',')




# changing string values to int
for i in range(len(datas)):
    datas[i] = int(datas[i])
    

def opcode(slist,pos):
    if slist[pos] == 1:
        temp = slist[slist[pos + 1]] + slist[slist[pos + 2]]
        slist[slist[pos + 3]] = temp
        print(temp)
    elif slist[pos] == 2:
        temp = slist[slist[pos + 1]] * slist[slist[pos + 2]]
        slist[slist[pos + 3]] = temp
        print(temp)
    elif slist[pos] == 99:
        return
    else:
        print('some issues happened')
        return

datas[1] = 12
datas[2] = 2

itt = 0
while datas[itt] != 99:
    opcode(datas,itt)
    itt = itt + 4
    
print("number in position 0 is:", datas[0])
        
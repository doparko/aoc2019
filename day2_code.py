# Advent of code 2019 day 2

import numpy as np

#practice set
#datinss ='1,9,10,3,2,3,11,0,99,30,40,50\n'

filename = 'day2_input.txt'
datin = open(filename)
datinss = datin.readline()
datas = datinss.split(',')




# changing string values to int
for i in range(len(datas)):
    datas[i] = int(datas[i])

# for part 2 data
datas2 = datas[:]    

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

nounslist = np.linspace(0,99,100)
verbslist = np.linspace(0,99,100)

nouns , verbs = np.meshgrid(nounslist,verbslist)
#flat nouns and verbs make it easy to go over
nflat = nouns.flatten()
vflat = verbs.flatten()

# Part 2
def opnounverb(inst,nns,vbs):
    for jay in range(len(nflat)):
        temp = inst[:]
        jtt = 0
        temp[1] = int(nns[jay])
        temp[2] = int(vbs[jay])
        while inst[jtt] != 99:
            opcode(temp,jtt)
            jtt = jtt + 4
        if temp[0] == 19690720:
            print('Found solution. noun:',nns[jay],' verb:',vbs[jay],' 100*noun+verb:',100*nns[jay] + vbs[jay])
            break

opnounverb(datas2,nflat,vflat)

            
    

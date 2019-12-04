# 2019 advent of code day 4
import numpy as np
begin = 134792
end = 675810



count = 0
codelist = set()

alnums = np.linspace(begin,end,end - begin + 1)

def checkascend(number):
    stnum = str(number)
    for j in range(len(stnum)):
        if j == len(stnum) -1:
            break
        elif int(stnum[j]) > int(stnum[j+1]):
            return 0
    return 1

def checkdub(number):
    stnum = str(number)
    for k in range(1,10):
        if stnum.find(str(k)+str(k)) != -1:
            return 1
    return 0


for n in alnums:
    i = int(n)
    if checkascend(i) == 1 and checkdub(i) == 1:
        count += 1
        codelist.add(i)
        
print('Your amount of codes is:',count)

codelist2 = set()
testset = set([ 577899,225666,135555,])

for ii in codelist:
    #print(ii) # debugging
    sstr = str(ii)
    digs = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for jj in range(1,10):
        #print(jj) #debugging
        slook = 0
        rule = True
        while rule == True:
            if sstr.find(str(jj),slook) != -1:
                #print('found',jj,'here:',sstr.find(str(jj),slook)) #debugging
                digs[jj] += 1
                slook = sstr.find(str(jj),slook) + 1
                #print('new look starts:',slook) #debugging
            else:
                rule = False
    #print(digs) #debugging
    if digs[1] == 2 or digs[2] == 2 or digs[3] == 2 or digs[4] == 2 or digs[5] == 2 or digs[6] == 2 or digs[7] == 2 or digs[8] == 2 or digs[9] == 2:
        codelist2.add(ii)
        
print('Your amount of codes is:',len(codelist2))   
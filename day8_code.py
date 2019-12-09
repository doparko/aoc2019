# Advent of code 2019 day 8
import operator

filename = 'day8_input.txt'
datopen = open(filename)
datas = datopen.read()

n = len(datas)

pixnum = 25*6

numlayers = int(n/pixnum)

layers = [0] * (numlayers-1)

for i in range(numlayers-1): # maybe -1 from range
    itt = i*pixnum
    layers[i] = datas[itt:itt+pixnum]

zcount = [0] * len(layers)
onecount = [0] * len(layers)
twocount = [0] * len(layers)


#loop to count zeroes
jtt = 0
for k in layers:
    for j in k:
        if j == '0':
            zcount[jtt] += 1
        elif j == '1':
            onecount[jtt] += 1
        elif j == '2':
            twocount[jtt] += 1
    jtt += 1
counts = {}
for n in range(len(zcount)):
    counts[n] = zcount[n]
    
max0 = min(counts.items(), key=operator.itemgetter(1))[0]

print('The answer to 1s * 2s is:',onecount[max0]*twocount[max0])



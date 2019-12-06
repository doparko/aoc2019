# Advent of code 2019 day 6

import operator

filename = 'day6_input.txt'
datopen = open(filename)
datain = datopen.readlines()

#test
#datain = ['COM)BBB','BBB)CCC','CCC)DDD','DDD)EEE','EEE)FFF','BBB)GGG','GGG)HHH','DDD)III','EEE)JJJ','JJJ)KKK','KKK)LLL','KKK)YOU','III)SAN']

planets = [0]*len(datain)

def countorb(planet,orbmap):
    ans = 0
    if planet == 'COM':
        return 0
    ans = 1 + countorb(orbmap[planet],orbmap)
    return ans

def countsanta(planet,orbmap,common):
    ans = 0
    #print(planet)
    if planet == common:
        return 0
    ans = 1 + countsanta(orbmap[planet],orbmap,common)
    return ans

def pathorb(planet,orbmap,pathset):
    pathset.add(orbmap[planet])
    #print(orbmap[planet])
    if planet == 'COM' or orbmap[planet] == 'COM':
        #print('made to com')
        return
    pathorb(orbmap[planet],orbmap,pathset)
    return

mdata = [0]*len(datain)

for n in range(len(datain)):
    mdata[n] = datain[n][:-1]

#remember to replace datain with mdata here!!!
for j in range(len(mdata)):
    planets[j] = mdata[j][-3:]
    

orblist = {}
    
for i in mdata:
    cent,orbits = i.split(')')
    orblist[orbits] = cent

totorb = 0
for k in planets:
    totorb += countorb(k,orblist)

#part 2
youpath = set()
sanpath = set()

pathorb('YOU',orblist,youpath)
pathorb('SAN',orblist,sanpath)

commonpath = youpath.intersection(sanpath)
commonlength = {}

for m in commonpath:
    commonlength[m] = countorb(m,orblist)

commonorbit = max(commonlength.items(), key=operator.itemgetter(1))[0]

solution = countsanta('YOU',orblist,commonorbit) + countsanta('SAN',orblist,commonorbit) - 2
print("Solution to part 2, jumps you need to get to santa:",solution)

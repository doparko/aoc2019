# aoc 2019 day 1 code

import numpy as np
filename = 'day1_input.txt'
dataopen = open(filename)
datin = dataopen.readlines()

def massfuel(mass):
	fuel = np.floor(int(mass)/3) - 2
	return fuel

def fuelfuel(mass):
    tempmass = int(mass)
    tots = 0
    while (np.floor(tempmass/3) -2) > 0:
        tots = tots + (np.floor(tempmass/3) -2)
        tempmass = (np.floor(tempmass/3) -2)
    return tots

sum = 0

whichpart = int(input("which part do you want to do (1/2)?:"))
#part 1
if whichpart == 1:
    for i in datin:
    	sum = sum + massfuel(i)
    
    print("Your total fuel needed is:",sum)
elif whichpart ==2:
    #part 2 here
    for j in datin:
        sum = sum + fuelfuel(j)
    print("Your total fuel needed is:",sum)
else:
    print("bad input buddy")
    


def fuelfuel(mass,sums):
    tempmass = int(mass)
    tots = 0
    while tempmass > 0:
        tots = tots + (np.floor(tempmass/3) -2)
        tempmass = (np.floor(tempmass/3) -2)
    return tots
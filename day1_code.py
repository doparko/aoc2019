# aoc 2019 day 1 code

import numpy as np
filename = 'day1_input.txt'
dataopen = open(filename)
datin = dataopen.readlines()

def massfuel(mass):
	fuel = np.floor(int(mass)/3) - 2
	return fuel
sum = 0
for i in datin:
	sum = sum + massfuel(i)

print("Your total fuel needed is:",sum)


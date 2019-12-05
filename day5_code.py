# Advent of code 2019 day 5

import numpy as np

filename = 'day5_input.txt'
datopen = open(filename)
data = datopen.readlines()
data = data.split(',')

indat = [0] *len(data)
for i in range(len(data)):
    indat[i] = int(loo[i])


operation = {1:'add', 2:'multiply', 3:'input', 4:'output'}

# function takes in code and decides what to do
def whatdo(clist,index):
    
    
itt = 0

while indat[itt] != 99:
    if indat[itt] == 3:
        
    whatdo()

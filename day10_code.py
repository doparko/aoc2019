# Advent of code 2019 day 10

import numpy as np

filename = 'day10_input.txt'
datopen = open(filename)
datas = datopen.readlines()

n = len(datas)

mapast = np.array([])

for i in range(n):
    ary = np.array(list(datas[i][:-1]))
    mapast[i,:] = ary 

# Advent of code 2019 day 3

import numpy as np

filename = 'day3_input.txt'
datin = open(filename)
datas = datin.readlines()

w1 = datas[0]
w2 = datas[1]

wire1 = w1.split(',')
wire2 = w2.split(',')

#practice lists
##wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
##wire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
##
##wire4 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
##wire3 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
##
##wire5 = ['R8','U5','L5','D3']
##wire6 = ['U7','R6','D4','L4']

board1 = ''
##board2 = ''
##board3 = ''
##board3_wire2 = ''

def plotwire1(wire,circuit):
    rowcor = 0
    colcor = 0
    for i in wire:
        direc = i[0]
        step = int(i[1:])
        if direc == 'R':
            for j in range(step):
                circuit += str(rowcor)+'x'+str(colcor + j) + 'c'
            colcor += step
        elif direc == 'L':
            for j in range(step):
                circuit += str(rowcor)+'x'+str(colcor - j) + 'c'
            colcor -= step
        elif direc == 'U':
            for j in range(step):
                circuit += str(rowcor + j)+'x'+str(colcor) + 'c'
            rowcor += step
        elif direc == 'D':
            for j in range(step):
                circuit += str(rowcor - j)+'x'+str(colcor) + 'c'
            rowcor -= step
        else:
            print('bad instruction')
            break
    return circuit

def plotwire2(wire,other):
    dist =[]
    rowcor = 0
    colcor = 0
    for i in wire:
        direc = i[0]
        step = int(i[1:])
        if direc == 'R':
            for j in range(step):
                if other.find('c'+str(rowcor)+'x'+str(colcor + j) + 'c') !=-1:
                    dist.append(abs(rowcor) + abs(colcor + j))
            colcor += step
        elif direc == 'L':
            for j in range(step):
                if other.find('c'+str(rowcor)+'x'+str(colcor - j) + 'c') !=-1:
                   dist.append(abs(rowcor) + abs(colcor - j)) 
            colcor -= step
        elif direc == 'U':
            for j in range(step):
                if other.find('c'+str(rowcor + j)+'x'+str(colcor) + 'c') !=-1:
                    dist.append(abs(rowcor + j) + abs(colcor) )
            rowcor += step
        elif direc == 'D':
            for j in range(step):
                if other.find('c'+str(rowcor - j)+'x'+str(colcor) + 'c') !=-1:
                    dist.append(abs(rowcor - j) + abs(colcor))
            rowcor -= step
        else:
            print('bad instruction')
            break
    return dist
        
board1 = plotwire1(wire1,board1)
mandist1 = plotwire2(wire2,board1)

##board2 = plotwire1(wire3,board2)
##mandist2 = plotwire2(wire4,board2)
##
##board3 = plotwire1(wire5,board3)
##mandist3 = plotwire2(wire6,board3)
##
##board3_wire2 = plotwire1(wire6,board3_wire2)

##print(mandist1)
##print(mandist2)
##print(mandist3)

print(min(mandist1[1:]))
##print(min(mandist2[1:]))
##print(min(mandist3[1:]))
            

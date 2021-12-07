# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:41:48 2021

@author: User
"""
# Part 1

ver_pos = 0
hor_pos = 0

with open('input.txt') as f:
    for line in f:
        if line.startswith('forward'):
            hor_pos = hor_pos + int(line.split(' ')[1])
        elif line.startswith('up'):
            ver_pos = ver_pos - int(line.split(' ')[1])
        elif line.startswith('down'):
            ver_pos = ver_pos + int(line.split(' ')[1])
        else:
            pass
        
print(ver_pos*hor_pos)


# Part 2

ver_pos = 0
hor_pos = 0
aim = 0

with open('input.txt') as f:
    for line in f:
        if line.startswith('forward'):
            hor_pos = hor_pos + int(line.split(' ')[1])
            ver_pos = ver_pos + aim * int(line.split(' ')[1])
        elif line.startswith('up'):
            aim = aim - int(line.split(' ')[1])
        elif line.startswith('down'):
            aim = aim + int(line.split(' ')[1])
        else:
            pass
        
print(ver_pos*hor_pos)

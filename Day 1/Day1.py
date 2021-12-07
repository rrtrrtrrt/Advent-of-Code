# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:08:41 2021

@author: User
"""

# Part 1

with open('input.txt') as f:
    input_list = [int(line) for line in f]
print(sum(input_list[i+1]-input_list[i] > 0 for i in range(len(input_list)-1)))


# Part 2

rolling_window = []
for i in range(len(input_list)-2):
    rolling_window.append(input_list[i+2]+input_list[i+1]+input_list[i])
    
print(sum(rolling_window[i+1]-rolling_window[i] > 0 for i in range(len(rolling_window)-1)))

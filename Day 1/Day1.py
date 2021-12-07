# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:08:41 2021

@author: User
"""

with open('input.txt') as f:
    input_list = [int(line) for line in f]
print(sum(input_list[i+1]-input_list[i] > 0 for i in range(len(input_list)-1)))
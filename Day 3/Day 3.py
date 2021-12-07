# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:11:02 2021

@author: User
"""

# Part 1

with open('input.txt') as f:
        input_list = [line for line in f]

sum_dig = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma_rate = []

for i in range(0,12):
    for x in range(len(input_list)):
        sum_dig[i] = sum_dig[i] + int(input_list[x][i])
    if sum_dig[i] / (len(input_list)+1) >= 0.5:
        gamma_rate.append(1)
    else:
        gamma_rate.append(0)

gamma_rate_str = str(''.join(map(str, gamma_rate)))

epsilon_rate = ''

for i in gamma_rate_str:
    
    if i == '0':
        epsilon_rate += '1'
          
    else:
        epsilon_rate += '0'


print(int(gamma_rate_str, 2)*int(epsilon_rate, 2))
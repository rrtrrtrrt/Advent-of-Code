# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 12:11:02 2021

@author: User
"""

# Part 1

with open('input.txt') as f:
        input_list = [line for line in f]

sum_dig = [0]*(len(input_list[0])-1)
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


# Part 2

import pandas as pd

df = pd.DataFrame(input_list)
df = df.rename(columns = {0 : 'Source'})
df[0]=df['Source'].str.slice(stop=1)
df[1]=df['Source'].str.slice(start=1, stop=2)
df[2]=df['Source'].str.slice(start=2, stop=3)
df[3]=df['Source'].str.slice(start=3, stop=4)
df[4]=df['Source'].str.slice(start=4, stop=5)
df[5]=df['Source'].str.slice(start=5, stop=6)
df[6]=df['Source'].str.slice(start=6, stop=7)
df[7]=df['Source'].str.slice(start=7, stop=8)
df[8]=df['Source'].str.slice(start=8, stop=9)
df[9]=df['Source'].str.slice(start=9, stop=10)
df[10]=df['Source'].str.slice(start=10, stop=11)
df[11]=df['Source'].str.slice(start=11, stop=12)
df[[0,1,2,3,4,5,6,7,8,9,10,11]] = df[[0,1,2,3,4,5,6,7,8,9,10,11]].astype(int)


for i in range(0,12):
    if len(df.index) == 1:
        break
    elif len(df[i].mode()) > 1:
        df = df[df[i] == 1]
    elif df[i].mode()[0] == 0:
        df = df[df[i] == 0]
    else:
        df = df[df[i] == 1]

         
oxygen_gen_rating = df.iloc[0,0]


df = pd.DataFrame(input_list)
df = df.rename(columns = {0 : 'Source'})
df[0]=df['Source'].str.slice(stop=1)
df[1]=df['Source'].str.slice(start=1, stop=2)
df[2]=df['Source'].str.slice(start=2, stop=3)
df[3]=df['Source'].str.slice(start=3, stop=4)
df[4]=df['Source'].str.slice(start=4, stop=5)
df[5]=df['Source'].str.slice(start=5, stop=6)
df[6]=df['Source'].str.slice(start=6, stop=7)
df[7]=df['Source'].str.slice(start=7, stop=8)
df[8]=df['Source'].str.slice(start=8, stop=9)
df[9]=df['Source'].str.slice(start=9, stop=10)
df[10]=df['Source'].str.slice(start=10, stop=11)
df[11]=df['Source'].str.slice(start=11, stop=12)
df[[0,1,2,3,4,5,6,7,8,9,10,11]] = df[[0,1,2,3,4,5,6,7,8,9,10,11]].astype(int)


for i in range(0,12):
    if len(df.index) == 1:
        break
    elif len(df[i].mode()) > 1:
        df = df[df[i] == 0]    
    elif df[i].mode()[0] == 0:
        df = df[df[i] == 1]   
    else:
        df = df[df[i] == 0]        
        
co2_gen_rating = df.iloc[0,0]

print(int(oxygen_gen_rating, 2)*int(co2_gen_rating, 2))

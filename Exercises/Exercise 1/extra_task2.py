# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:50:40 2022

@author: kahko
"""

import numpy as np
import numpy.ma as ma

m10x10 = np.random.rand(10,10)*50
mask10x10 = np.zeros((10,10))

randomIndexes = []

while len(randomIndexes) < 10 :
    candidate = np.random.randint(0, 100)
    if candidate not in randomIndexes:
        randomIndexes.append(candidate)

for i in randomIndexes:
    m10x10[i//10][i%10] = -100
    mask10x10[i//10][i%10] = 1
    
mx10x10 = ma.masked_array(m10x10, mask=mask10x10, fill_value=0)


print(f'{m10x10.sum()= :.2f}')
print(f'{mx10x10.sum()= :.2f}')

            
for i, y in enumerate(mask10x10):
    for j, x in enumerate(y):
        if x == 1:
            m10x10[i][j] = 0


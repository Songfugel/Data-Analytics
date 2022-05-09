# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:43:14 2022

@author: kahko
"""

import numpy as np

m15x15 = np.random.rand(15,15)

np.savetxt('matrix.txt',m15x15)

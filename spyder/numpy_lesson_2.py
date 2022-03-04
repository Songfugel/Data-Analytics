# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:21:30 2022

@author: kahko
"""

import numpy as np

data = np.arange(1, 101)

squares = np.sqrt(data)
values = np.arange(0, 100).reshape(10, 10)
total = values.sum()

total_rows = values.sum(axis=1)

total_columns = values.sum(axis=0)

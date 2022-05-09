# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:28:20 2022

@author: kahko
"""
import numpy as np

man_years = np.random.randint(2010, 2021, 10)
print(man_years)

sell_price = np.random.randint(2000, 60000, 10)
print(sell_price)

man_years_sorter = np.argsort(man_years)

for i in range(10):
    print(f'Year: {man_years[man_years_sorter][i]} \
          - price: {sell_price[man_years_sorter][i]}')
          
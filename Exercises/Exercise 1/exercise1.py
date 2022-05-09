# Exercise 1 Santtu Kähkönen
import numpy as np

'''
Using letter prefixing as namespaces to avoid using
explicit global variable assignment with functions
to be able to see them in variable explorer

'''
print('\nEXERCISE 1.\n')
a1_ones = [1]*15
print(a1_ones)
print('\n')

print('\n')
a2_sevens = [7]*15
print (a2_sevens)


print('\n')
a3_100to150 = list(range(100, 151))
print (a3_100to150)


print('\n')
a4_even0to100 = list(range(2, 100, 2))
print (a4_even0to100)

print('\n')
a4_result = list(range(1952, 2020, 4))
print (a4_result)


print('\nEXERCISE 2.\n')

b1_zeroes = np.zeros(15)
print(b1_zeroes)

print('\n')
b2_ones = np.ones(15)
print (b2_ones)

print('\n')
b3_sevens = np.ones(15)*7
print (b3_sevens)

print('\n')
b4_100to150 = np.arange(100, 151)
print (b4_100to150 )

print('\n')
b5_1900to2021 = np.arange(1900, 2022)
print (b5_1900to2021)

print('\n')
b6_even_0to100 = np.arange(2, 100, 2)
print (b6_even_0to100)

print('\n')
b7_result = np.arange(1952, 2020, 4)
print (b7_result)

# normal slightly easier and more logical. Numpy is ofc 
# much much faster and more efficient

print('\nEXERCISE 3.\n')

c1_7x7 = np.arange(1,50).reshape(7,7)
print(c1_7x7)

# no np
c1_extra = []

c1_rows = 7 
c1_columns = 7
for c1_y in range(0, c1_rows):
    c1_extra.append([
        c1_y * c1_rows+ c1_x +1
        for c1_x in range(0,c1_columns)
        ])

print (c1_extra)

c2_rand8x8 = np.random.rand(8,8)*5
print(c2_rand8x8)

c3_stand_8x8 = np.random.randn(8,8)
print(c3_stand_8x8)


print('\nEXERCISE 4.\n')
d1_0to1 = np.linspace(0, 1, 10)
print(d1_0to1)

d2_10x10 = np.linspace(0,5,10*10).reshape(10,10)
print(d2_10x10)


d2_r = 10 
d2_c = 10

d2_step = (5-0) / ((d2_r*d2_c)-1)


d2_extra = []
for d2_y in range(0, d2_r):
    d2_extra.append([
        (d2_y * d2_r+ d2_x)*d2_step
        for d2_x in range(0,d2_c)
        ])
    
print(d2_extra)


print('\nEXERCISE 5.\n')
e1 = np.array([[23,34,54,34,56],[33,56,78,65,78],[41,32,11,34,56]])
print(e1)

e2 = np.arange(128, 256).reshape(16,8)
print(e2)

e3 = np.linspace(0.05, 5, 100).reshape(10,10)
print(e3)

print('\nEXERCISE 6.\n')

f_dataset = np.arange(1, 37).reshape(6,6)

f1_slice = f_dataset[3:, 2:]
print(f1_slice)

f2_slice = f_dataset[:4, 3]
print(f2_slice)

f3_slice = f_dataset[2]
print(f'{f3_slice=}')

f4_slice = f_dataset[3:]
print(f'{f4_slice=}')

print('\nEXERCISE 7.\n')

g_dataset = np.arange(1,50).reshape(7,7)

g_dataset[:] += 50
print(f'{g_dataset=}')

g1_sum = np.sum(g_dataset)
print(f'{g1_sum=}')

g_dataset_odd = g_dataset[g_dataset% 2 == 1]
g2_sum_odd = np.sum(g_dataset_odd)
print(f'{g2_sum_odd=}')

g3_std = np.std(g_dataset)
print(f'{g3_std=}')

g4_sum_by_row = np.sum(g_dataset, axis=1)
print(f'{g4_sum_by_row=}')

g5_sum_by_column = np.sum(g_dataset, axis=0)
print(f'{g5_sum_by_column=}')


g_list = c1_extra.copy()

g_extra_sum = 0
g_extra_row_sums = []
g_extra_column_sums = []

# rows in normal loop
for y in range(len(g_list)):    
    for x in range(len(g_list[y])):
        g_list[y][x] += 50
        
    row_sum = sum(g_list[y])
    g_extra_sum += row_sum
    g_extra_row_sums.append(row_sum)

# columns in transposed loop
for x in range(len(g_list[0])):
    col_sum = 0
    for y in range(len(g_list)):
        col_sum += g_list[y][x]
    g_extra_column_sums.append(col_sum)
        


print(f'\n{g_extra_sum= }')
print(f'{g_extra_row_sums= }')
print(f'{g_extra_column_sums= }')






















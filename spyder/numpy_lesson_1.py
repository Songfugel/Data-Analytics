# the following part can be copy-pasted into a python file as is

# ex.1
import numpy as np

numbers = [3,5,6,2]

# 1-dimensional list
data1_1 = np.array(numbers)

day1 = [3,5,6,2]
day2 = [2,4,6,2]
day3 = [1,5,30,2]
temperatures = [day1, day2, day3]

#2-dimensional table/matrix
data1_2 = np.array(temperatures)


# ex.2
# you can easily make lists with number ranges

#make a list from 0 to 9
data2_1 = np.arange(0, 10)

# generate a list of even numbers between 0 and 10, using step size parameter 2
data2_2 = np.arange(0, 11, 2)

# ex. 3

# NumPy has an easy way to make interpolated lists
# from 0 to 5 in 10 steps, so it automatically generates a 10 item list with each value evenly distributed between 0 and 5
data3_1 = np.linspace(0, 5, 10)

# ex. 4

# NumPy has a powerful random generator
data4_1 = np.random.rand(5)

# matrix version
data4_2 = np.random.rand(5, 5)

# sample values from standard normal distribution, values from -3 to 3
data4_3 = np.random.randn(3)
data4_4 = np.random.randn(5, 5)



# RESHAPE - Tuomas's favourite feature of Numpy
# Basically allows us to convert a number list into a number matrix, like splitting a list into rows and columns

# ex. 5
#generate numbers from + to 24
data5_1 = np.arange(25)

data5_2 = data5_1.reshape(5, 5)
# ! tip you can also chain functions in numpy
data5_3 = np.arange(25).reshape(5,5)

# max and min value in dataset

data = np.random.randn(1000)
max_value = data.max()
min_value = data.min()

#you can also do it this way:
max_value2 = np.max(data)

# you can also get the index locations of max and min values
max_value_position = data.argmax()
min_value_position = data.argmin()


# ex. 6
# if for some reason you need to find the shape of your data
data = np.random.randn(5,5,5)

shape = data.shape

# getting the data type, you see this easily in spyder's variable explorer too
datatype = data.dtype

# our data, matrix... list of lists,

matrix = np.arange(25).reshape(5, 5)
# we can get rows from the matrix
matrix_row = matrix[0]

# THIS IS POWERFUL! you can get sections of the data
matrix_section1 = matrix[:2,1:]

# 2nd column, basically " take all rows, but only 2nd column
matrix_column = matrix[:, 1]

# rows from index 1 to 4 and columns from 1 to 4, basically a square are cut
# from the matrix
matrix_section2 = matrix[1:4, 1:4]

# a very useful shorthand to filter data, this filters data values by > 5 condition
data = np.arange(1, 21)
filtered_data = data[data > 5]

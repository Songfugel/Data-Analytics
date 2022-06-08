import seaborn as sb

import matplotlib.pyplot as plt

COL_MPG = 'mpg'
COL_DISP = 'displacement'
COL_CYL = 'cylinders'
COL_HP = 'horsepower'
COL_WEIGHT = 'weight'
COL_ACC = 'acceleration'
COL_YEAR = 'model_year'
COL_ORIG = 'origin'
COL_NAME = 'name'
COL_LTR_PER_100KM = 'liters_per_100km'

mpg = sb.load_dataset('mpg')
df = mpg.copy()


print(ex = ''' << Exercise 3.2.x >>

In this exercise, use the 'mpg' dataset from seaborn! 
(sns.load_dataset('mpg')). mpg stands for "miles per gallon", 
which is a common way to represent fuel consumption in USA
----------------------------------------------------------------------------
''')

# 1. Clean up the data
# Definitions
USGALLON = 3.785411784 # in liters
MILE = 1.609344 # Kilometers

# Create a new column: "liters_per_100km" , which converts the mpg to liters
# per 100 km

df[COL_LTR_PER_100KM] = df.apply(
    lambda x: ((100 * USGALLON) / (MILE * x[COL_MPG])), axis=1)

# Remove the original mpg –column
df_filt = df.drop(COL_MPG, axis=1)

# Remove the "name" –column
df_filt = df_filt.drop(COL_NAME, axis=1)

# After this, create a correlation matrix.
df_corr = df_filt.corr()

# There are two columns that do not correlate as much as the others,
# remove these two from the dataset

df_filt = df_filt.drop(COL_YEAR, axis=1
    ).drop(COL_ACC, axis=1)

df_corr2 = df_filt.corr()

# A) There are three different columns that are strongly connected to the car's
# efficiency (both power and consumption), select one of them and remove the
# others from the dataset

ex1_a = '''SOLUTION: Hmm, but there are 4 of them, not three
    * cylinders, displacement, horsepower and weight
    * but I guess weight is supposed to be the odd man out in here, so
      ignoring it  
'''

df_filt = df_filt.drop(COL_HP, axis=1
    ).drop(COL_CYL, axis=1)
 
# B) Which column is the best selection to indicate the car’s efficiency, and
# why? (cylinders, horsepower or displacement/engine size
ex1_b = '''SOLUTION: Choosing displacement, since it seems to be having
extremely high correlation with weight, cylinders, horsepower and is close
2nd in consumption   
'''

#2. Finally, use the pair plot and hue (origin)

plt.clf()
sb.pairplot(df_filt, hue=COL_ORIG)
plt.figure()

# A) Which origin country tends have bigger fuel consumption in cars?
ex2_a = '''SOLUTION: unsurprisingly the USA by far the biggest fuel
consumption by up to several magnitudes'''

# Which is generally the origin with lowest consumption? 
# (more specific plots might be a good idea here, for example:
# box plot, scatter plot etc., pandas functions are helpful too!)

plt.clf()
sb.boxplot(data=df_filt, x=COL_ORIG, y=COL_LTR_PER_100KM, hue=COL_ORIG)
plt.figure()

ex2_b = '''SOLUTION: Consumption is smallest in Japan with a small margin
ahead of Europe'''

# What other features the cars seem to have that result into bigger
# or lower consumption
plt.clf()
sb.pairplot(df, hue=COL_ORIG)
plt.figure()

ex2_c = '''SOLUTION: Higher displacement, weight, cylinders and horse power
 seem to all correlate significantly with higher consumption.
 
 Also higher the model year and acceleration the lower the consumption seems
 to be. This is easily explained by improved technology and the fact that 
 hybrid cars have an insanely high acceleration rate due to their electric 
 motors instant torque and significantly lower weight, when compared to 
 combustion engines. '''

import seaborn as sb
import pandas as pd

import matplotlib.pyplot as plt

ex = ''' << Exercise 3.3.x >>

csv-data, pandas and seaborn

This dataset has been downloaded from kaggle. 
Download the "groceries.csv" from Moodle. 
Load the data by using pandas. (read_csv() etc.)
Note: since this is an actual dataset from the internet, the data is in
quite a rough format.
----------------------------------------------------------------------------
'''
print(ex)

CSV_FILE = "groceries.csv"

data = pd.read_csv(CSV_FILE)
df = data.copy()

from enum import Enum, unique

@unique
class Col(Enum):
    MONTH = 'Month'
    YEAR = 'Year'
    RICE = 'Rice'
    WHEAT = 'Wheat'
    BARLEY = 'Barley'
    CORN = 'Corn'
    PEANUTS = 'Peanuts'
    SUGAR = 'Sugar'
    COCONUT_OIL = 'Coconut-oil'
    PALM_OIL = 'Palm-oil'	
    SUNFLOWER_OIL = 'Sunflower-oil'
    CHICKEN = 'Chicken'
    BEEF = 'Beef'
    PORK = 'Pork'
    FISH = 'Fish'
    TEA = 'Tea'
    COFFEE = 'Coffee'
    
    def __str__(self):
        return '{0}'.format(self.value)
 
    
    

# If you take a look at the data, you will notice three columns 
# have NaN –values. You can either remove these columns all 
# together, or you can fill the missing values with average values 
# of that column. For example, for the Fish -column you could do 
# something like this:
#   food['Fish'].fillna((food['Fish'].mean()), inplace=True)
#   In this case, food is the name of the DataFrame we just got 
#   from the csv-file. Do this same operation to the two other 
#   columns with missing values

df[Col.FISH.value].fillna(df[Col.FISH.value].mean(), inplace=True)
df[Col.SUNFLOWER_OIL.value].fillna(df[Col.SUNFLOWER_OIL.value].mean(),
                                   inplace=True)
df[Col.PORK.value].fillna(df[Col.PORK.value].mean(), inplace=True)


#• In this data, the date column is a bit difficult to use, since it's 
#  not completely in numerical format. Split the Month-column 
#  so, that you have two different columns: Month and Year
#   o For month, use a numeric format 1-12
#   o For year, use the full year 1990-2020
#   o Check out the examples in Moodle, this one is a bit 
#     tricky, but very neat to know how it's done!

import calendar

def change_month(row):
    return list(calendar.month_abbr).index(row[Col.MONTH.value])


def fix_year(row):
    year = int(row[Col.YEAR.value])
    if year > 50:
        return int(f"19{row['Year']}")
    else:
        return int(f"20{row['Year']}")

#split the original date into two columns:
df[[Col.MONTH.value, Col.YEAR.value]] = df[Col.MONTH.value].str.split(
    '-', 1, expand=True)

year_col = df.pop(Col.YEAR.value)
df.insert(1, Col.YEAR.value, year_col)

df[Col.MONTH.value] = df.apply(change_month, axis=1)
df[Col.YEAR.value] = df.apply(fix_year, axis=1)



#• After the cleanups, create a correlation matrix of the data. 
#  Create a heatmap on the correlations as well. 
#  
#  Which grocery stands out? (i.e. there seems to be one grocery 
#  item whose price doesn't follow other groceries at all)

#• Which groceries seem to correlate to each other's prices? What 
#  do they have in common

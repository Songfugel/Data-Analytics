import seaborn as sb
import pandas as pd

import matplotlib.pyplot as plt
import math

ex = ''' << Exercise 3.extras.x >>'''
print(ex)


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
    
@unique
class Titanic(Enum):
    ALIVE = 'alive'
    ADULT_MALE = 'adult_male'
    DECK = 'deck'
    WHO = 'who'
    EMBARKED = 'embarked'
    EMBARK_TOWN = 'embark_town'
    
    def __str__(self):
        return '{0}'.format(self.value)

''' 
1. seaborn: Try out Boxenplot and/or Dendrogram in any of the
previous dataset exercises. Do these plot types provide some 
interesting info on the data? (Google for examples on these 
plot types)
• You may also consider some other plots, for 
example: displot, catplot, relplot
'''

'''
2. Use the "titanic" dataset from the seaborn datasets 
(sns.load_dataset('titanic')). Find out the features of a typical 
person that survived or did not survive the sinking of Titanic.
'''
titanic = sb.load_dataset('titanic')
df = titanic.copy()

df.drop(Titanic.ALIVE.value, axis=1, inplace=True)
df.drop(Titanic.EMBARK_TOWN.value, axis=1, inplace=True)
df.dropna(subset=[Titanic.EMBARKED.value], inplace=True)
def fix_deck(row):
    deck = row['deck']
    if deck == 'A':
        return 7
    if deck == 'B':
        return 6
    if deck == 'C':
        return 5
    if deck == 'D':
        return 4
    if deck == 'E':
        return 3
    if deck == 'F':
        return 2
    if deck == 'G':
        return 1
    return 0

df.insert(5+7, 'deck_number', df.apply(fix_deck, axis=1))
df.drop('deck', axis=1, inplace=True)

def fix_age(row):
    age = row['age']
    if not math.isnan(age):
        return age
    
    who = row['who']
    
    if who == 'child':
        return df[df['who'] == 'child']['age'].median()
    return df[df['who'] != 'child']['age'].median()
    

df['age'] = df.apply(fix_age, axis=1)

df['is_child'] = df['who'] == 'child'
df['is_woman'] = df['who'] == 'woman'
df.drop('who', axis=1, inplace=True)

df_corr = df.corr()['survived']

ex2_sol = '''SOLUTION: as suspected, there seems to be pretty heavy negative
 correlation with being an adult male for surviving and an equal but opposite
 correlation to being a woman for surviving
 
 A huge surprise however, is that being a child has almost not correlation to
 survival chances. Even pclass, fare and deck number had more correlation than
 being a child
 '''


'''
3. Use the "taxis" dataset from the seaborn datasets
(sns.load_dataset('taxis')). Find out any correlations or 
interesting behaviors based on any columns in the data (color, 
payment, pickup_borough, dropoff_borough etc.)
Notes and ideas to try out:
Consider removing the pickup_zone and dropoff_zone, since 
there are way too many alternatives. Borough is the larger area 
in question, which can be helpful while grouping data (hue!)
How about pickup and dropoff times, should they be modified? 
From taxi point of view, is the weekday and time of day 
(morning, day, evening, night) more interesting than the actual 
dates?
These are just ideas, you're free to come up with your own 
ideas regarding the data!
'''

'''
4. Try out any of the previous examples and exercises by using 
any or many of the following additional plotting libraries:
• Matplotlib (this is the most common in addition to 
seaborn, recommended)
https://matplotlib.org/stable/tutorials/index.html#introd
uctory
• Plotly 
https://plotly.com/python/getting-started/
• Bokeh
https://docs.bokeh.org/en/latest/docs/user_guide.html
'''


'''
5. Try out any of the datasets below, or find yourself an 
interesting csv-dataset from kaggle! 
Use all your skills in numpy, pandas and seaborn, and find out 
features in the data. 
Was there something that is surprising in the dataset? What 
interesting correlations did you find?
Some interesting datasets, examples (you can find you own 
too!):
• https://www.kaggle.com/anamvillalpando/worldhappiness-ranking
• https://www.kaggle.com/sakshigoyal7/credit-cardcustomers
• https://www.kaggle.com/lucabasa/dutch-energy
• https://www.kaggle.com/yamaerenay/spotify-dataset19212020-160k-tracks?select=data_w_genres.csv
• https://www.kaggle.com/kboghe/android-appsmetadata?select=Android+apps+csv.csv
• https://www.kaggle.com/sudalairajkumar/cryptocurrency
pricehistory?select=coin_Bitcoin.csv

Note: These datasets can be quite rough to handle at first, feel 
free to ask tips from your instructor if some dataset interests 
you
'''

 

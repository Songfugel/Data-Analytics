import seaborn as sb
import pandas as pd

import matplotlib.pyplot as plt
import math

ex = ''' << Exercise 3.extras.x >>'''
print(ex)


from enum import Enum, unique

# Assignment 1 is after 2.

'''
2. Use the "titanic" dataset from the seaborn datasets 
(sns.load_dataset('titanic')). Find out the features of a typical 
person that survived or did not survive the sinking of Titanic.
'''

@unique
class Titanic(Enum):
    ALIVE = 'alive'
    ADULT_MALE = 'adult_male'
    DECK = 'deck'
    WHO = 'who'
    EMBARKED = 'embarked'
    EMBARK_TOWN = 'embark_town'
    SURVIVED = 'survived'
    
    def __str__(self):
        return '{0}'.format(self.value)
    
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
    

#df['age'] = df.apply(fix_age, axis=1)

#df['is_child'] = df['who'] == 'child'
#df['is_woman'] = df['who'] == 'woman'
#df.drop('who', axis=1, inplace=True)

#df_corr = df.corr()['survived']

ex2_sol = '''SOLUTION: as suspected, there seems to be pretty heavy negative
 correlation with being an adult male for surviving and an equal but opposite
 correlation to being a woman for surviving
 
 A huge surprise however, is that being a child has almost not correlation to
 survival chances. Even pclass, fare and deck number had more correlation than
 being a child
 '''

# Assignment 1.
''' 
1. seaborn: Try out Boxenplot and/or Dendrogram in any of the
previous dataset exercises. Do these plot types provide some 
interesting info on the data? (Google for examples on these 
plot types)
• You may also consider some other plots, for 
example: displot, catplot, relplot
'''

#plt.clf()
#sb.boxenplot(data=df['age'])
#plt.figure()

#plt.clf()
#sb.boxenplot(data=df['deck_number'])
#plt.figure()

#plt.clf()
#sb.boxenplot(data=df['pclass'])
#plt.figure()

#plt.clf()
#sb.clustermap(data=df.corr())
#plt.figure()

ex1_sol = '''SOLUTION: Boxenplot shows the distribution of values in each
column

Observations:

boxenplot:
    Ages - seem to be distributed by normal distribution slightly offset to the
    elder side and most passangers were between 18 to 45 years

    Deck Number - Most people were evenly distributed between decks 0 to 5,
    deck 6 had half the amount on deck 5 and deck 7 roughly 4-5 times less than
    on deck 6
    
    pclass - 2nd and 3rd pclass are each twice as numerous as first class

Clustermap (contains dendrogram?)
    adult males were most likely to be alone, while children and women much
    less likely
    
    fare and deck number with being woman and surviving all have a high
    correlation with each other
    
    I don't know what parch and sibsp mean but they seem to have a connection
    to being a child, so maybe they have something to do with families
    
'''

'''
3. Use the "taxis" dataset from the seaborn datasets
(sns.load_dataset('taxis')). 
'''

class Taxis():
    def __init__(self, data):
        self.data = data
    
    def pickup(self):
        return self.data['pickup']
    
    def dropoff(self):
        return self.data['dropoff']
    
    def passengers(self):
        return self.data['passengers']
    
    def distance(self):
        return self.data['distance']
    
    def fare(self):
        return self.data['fare']
    
    def tip(self):
        return self.data['tip']
    
    def tolls(self):
        return self.data['tolls']
    
    def total(self):
        return self.data['total']
    
    def color(self):
        return self.data['color']
    
    def payment(self):
        return self.data['payment']
    
    def pickup_zone(self):
        return self.data['pickup_zone']
    
    def dropoff_zone(self):
        return self.data['dropoff_zone']
    
    def pickup_borough(self):
        return self.data['pickup_borough']
    
    def dropoff_borough(self):
        return self.data['dropoff_borough']

taxi_data = sb.load_dataset('taxis')

taxis = Taxis(taxi_data)

# Notes and ideas to try out:
# Consider removing the pickup_zone and dropoff_zone, since
# there are way too many alternatives.

# data cleanup

# nan payment changed to cash which is default in US
taxis.payment().fillna('cash', inplace=True)
taxis.data.drop('pickup_zone', axis=1, inplace=True)
taxis.data.drop('dropoff_zone', axis=1, inplace=True)

taxis_corr = taxis.data.corr()

# Find out any correlations or 
# interesting behaviors based on any columns in the data (color, 
# payment, pickup_borough, dropoff_borough etc.)


#plt.clf()
#sb.clustermap(data=taxis_corr)
#plt.figure()


''' SOLUTION: Unsurprisingly total, distance and fare have an almost 90 to 100%
    correleation
    
    total amount and tips also have a very strong correlation'''



# From taxi point of view, is the weekday and time of day 
# (morning, day, evening, night) more interesting than the actual 
# dates?
# These are just ideas, you're free to come up with your own 
# ideas regarding the data!

from datetime import datetime, date

def is_weekday(row):
    return row['weekday'] < 5

def get_weekday(row):
    return datetime.strptime(row['dropoff'], '%Y-%m-%d %H:%M:%S').weekday()

taxis.data['weekday'] = taxis.data.apply(get_weekday, axis=1)
   
taxis.data['is_weekday'] = taxis.data.apply(is_weekday, axis=1)

plt.clf()
sb.barplot(data=taxis.data, y='total', x='weekday')
plt.figure()

plt.clf()
sb.barplot(data=taxis.data, y='total', x='weekday', estimator=sum)
plt.figure()


plt.clf()
sb.displot(data=taxis.data, y='total', x='weekday')
plt.figure()


''' SOLUTION: It seems that the mean total is slightly higher during weekdays,
and the highest on mondays and wednesdays

fare totals on the otherhand seems to peak on Friday instead, while Wednesday
 and Saturday share second place and on mondays. Monday while having the
 highest mean total fare, still has the smallest total overall
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
# drawing a similar distribution plot as in previous task "manually" with
# pyplots scatter plot

plt.scatter('weekday', 'total', c='lightblue', s=20, data=taxis.data)
plt.xlabel('weekdays')
plt.ylabel('fares')
plt.show()

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

 

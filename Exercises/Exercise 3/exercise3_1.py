print('''
< < < EXERCISES 3.1.x > > >''')
ex = '''
----------------------------------------------------------------------------
EXERCISES 3.1.x

(ANSWER FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER)

{The exercises description and forewords/assignments/prepwork should be here}
----------------------------------------------------------------------------'''
# IMPORTS HERE
# ex.:
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

COL_SPECIES = 'species'
COL_ISLAND = 'island'
COL_BILL_LENGTH = 'bill_length_mm'
COL_BILL_DEPTH = 'bill_depth_mm'
COL_BODY_MASS = 'body_mass_g'
COL_SEX = 'sex'
COL_FLIPPER_LENGTH  = 'flipper_length_mm' 

penguins = sb.load_dataset('penguins')

df = penguins.copy()


ex1 = ''' << Exercise 1. >>
In this exercise, use the 'penguins' dataset from seaborn! 

   (sns.load_dataset('penguins'))
  

----------------------------------------------------------------------------'''

# 1 Create a pair plot of the data
# SOLUTION

plt.clf()
sb.pairplot(df, hue=COL_SPECIES)
plt.figure()

plt.clf()
sb.displot(df[COL_BILL_LENGTH], kde=True, bins=10)
plt.figure()


plt.clf()
sb.kdeplot(df[COL_BODY_MASS])
plt.figure()

plt.clf()
sb.countplot(df[COL_SPECIES] + df[COL_ISLAND])
plt.figure()

plt.clf()
sb.boxplot(x=COL_SPECIES, y=COL_BODY_MASS, data=df, hue=COL_SEX)
plt.figure()

plt.clf()
sb.violinplot(x=COL_SPECIES, y=COL_BILL_LENGTH, 
              data=df, hue=COL_SEX, split = True)
plt.figure()

plt.clf()
sb.stripplot(x=COL_SPECIES, y=COL_BODY_MASS, 
              data=df, jitter=True,
              hue=COL_SEX, split = True)
plt.figure()

plt.clf()
sb.swarmplot(x=COL_SPECIES, y=COL_BODY_MASS, 
              data=df,
              hue=COL_SEX, split = True)
plt.figure()


df_corr = df.corr()

sb.heatmap(df_corr, annot=True, cmap='coolwarm')

plt.figure()

df_pivot = df.pivot_table(index=COL_SPECIES, columns = COL_SEX, 
                          values = COL_BODY_MASS)
plt.clf()
sb.heatmap(df_pivot, cmap='magma')
plt.figure()

plt.clf()
sb.clustermap(df_pivot, cmap='coolwarm', standard_scale=1)
plt.figure()


plt.clf()
sb.pairplot(df)
plt.figure()

# 2 What correlations can you immediately see?
# 2.extra: check out the correlation matrix for this dataset too 

df_corr = df.corr()
plt.clf()
sb.heatmap(df_corr, annot=True, cmap='coolwarm')
plt.figure()


ex2_sol = ''' SOLUTION: Body mass has a very strong correlation with flipper length and 
strong correlation with bill length and a fair negative correlation
with bill depth

Flipper length also has a fairly strong correlation with bill length
and a strong negative correlation with bill depth
'''

ex3 ='''3. Use hue for the "island" column, what do you learn from
the data this way?'''
plt.clf()
sb.pairplot(df, hue=COL_ISLAND)
plt.figure()
ex3_sol = ''' SOLUTION: Biscoe penguins seem to grow far more massive and have longer flippers,
shallower bill depth and the bill lenghts seem to be fairly uniform and long

Torgersen and Dream penguins seem to be much closer to each other than
the Biscoe penguins. Torgersen penguins also seem to have the shortests peaks,
while Dream's penguins seem to have the greatest variation in bill lengths
'''


ex4 = '''4. Find the amount of penguins on each island by using pandas
(value_counts()). Which island does not belong in the group?
4.extra: visualize the counts with a bar plot'''

df_islands = pd.value_counts(df[COL_ISLAND])
plt.clf()
sb.barplot(x=df_islands.index, y=df_islands)
plt.figure()
ex4_sol = '''SOLUTION: Torgersen seems to have significantly less penguins than
the other two islands
'''

ex5 = '''5. Create now another pair plot, and use hue for the "species"
 –column'''
plt.clf()
sb.pairplot(df, hue=COL_SPECIES)
plt.figure()


ex6 = '''6. Is there a difference when compared to islands?'''

ex6_sol = '''SOLUTION: Yes, but the distances are rather small. However Bill
Length seems to vary greatly between species and island distribution

Biscoe penguins seem to have a clear majority of long length billed penguins,
while Adelie penguins seem to have the shortest peaks and they are the majority
'''

ex6_ex = '''6.extra: How much does the "sex"-column affect the result?
(MALE / FEMALE)'''

plt.clf()
sb.pairplot(df, hue=COL_SEX)
plt.figure()

plt.clf()

df_males = df[df[COL_SEX] == 'Male']
plot6_m = sb.pairplot(df_males, hue=COL_SPECIES)
plot6_m.fig.suptitle('males')
plt.figure()

plt.clf()
df_females = df[df[COL_SEX] == 'Female']
plot6_f = sb.pairplot(df_females, hue=COL_SPECIES)
plot6_f.fig.suptitle('females')
plt.figure()

ex6_ex_sol = ''' SOLUTION: Male's seem to be slightly larger by default.
Chinstrap penguins also seem to have hair smaller difference between males
and females in size.

males alos seem to have less outliers and variation compared to females
'''
 
ex7 = '''7. Create a scatter plot for bill_length_mm and 
  flipper_length_mm, use species as hue (try also island as 
  hue)'''

plt.clf()
plot7_species = sb.scatterplot(data=df,x=COL_BILL_LENGTH, y=COL_FLIPPER_LENGTH,
                               hue=COL_SPECIES)
plt.figure()
plt.clf()

plot7_island = sb.scatterplot(data=df,x=COL_BILL_LENGTH, y=COL_FLIPPER_LENGTH,
                              hue=COL_ISLAND)
plt.figure()

ex8 = '''8. Which affects the result more, species or island?
 Use box plot, violin plot or swarm plot:'''

plt.clf()
sb.boxplot(data=df, x=COL_ISLAND, y=COL_FLIPPER_LENGTH, hue=COL_SPECIES)
plt.figure()

plt.clf()
sb.boxplot(data=df, x=COL_ISLAND, y=COL_BILL_LENGTH, hue=COL_SPECIES)
plt.figure()

ex8_sol = ''' SOLUTION: Species seem to have a massive impact on both values,
why island seems to make only marginal difference in variance
'''

ex9 = '''9. inspect the following information:
    • flipper_length_mm
    • bill_length_mm
    • body_mass_g
    • hue = island, x= species
  What interesting features can you find this way'''
  
plt.clf()
sb.boxplot(data=df, x=COL_SPECIES, y=COL_FLIPPER_LENGTH, hue=COL_ISLAND)
plt.figure()

plt.clf()
sb.boxplot(data=df, x=COL_SPECIES, y=COL_BILL_LENGTH, hue=COL_ISLAND)
plt.figure()

plt.clf()
sb.boxplot(data=df, x=COL_SPECIES, y=COL_BODY_MASS, hue=COL_ISLAND)
plt.figure()

ex9_sol = ''' SOLUTION: Gentoo are far bigger than adelie and chinstrap species
by mass and flipper length, but has shorter bill length than chinstraps.

Adelies are spread over all the islands and adelies on biscoe seem to have less
 variationin bill lenghts than those on torgersen.
'''
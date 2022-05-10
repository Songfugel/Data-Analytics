import pandas as pd

ex = '''
EXERCISES 2.3.x
FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER

Download the data_salaries_india.csv from Moodle, and consider the 
following questions of the data. Use any means in pandas (or even 
NumPy) you wish to explain your answers.
'''
print(ex)

df_salaries_india = pd.read_csv("data_salaries_india.csv")

df = df_salaries_india

ex1 = '''
1. Before we can do anything with the salaries, we have to convert 
them into something more usable
  o Note: the salaries can be yearly, monthly or hourly salaries
      □ We don't also need the Indian rupee –sign (₹)
  o You can use the template in Moodle to help you out with this 
    (Salary filtering, pandas exercise 3)

'''
print(ex1)
ex1_answer = ''

ex2 = '''
2. What are the most common values in different fields (Job Titles, Companies,
Location)? Based on the distribution, is the data balanced or not?
    o Extra task: there seem to be some Job Titles that are almost the same,
      like "Machine Learning Data Associate and Machine Learning Associate,
      combine these into something common
'''
print(ex2)
ex2_answer = ''

ex3 = '''
3. Are there any outliers in the data that might affect the averages 
negatively (certain salaries)? Manage the outliers as you best see 
fit (either remove them or leave them, based on your analysis
     
     o If we want to correlate upon categories (ordinal or binary), we 
       need to use factorize(). Factorize the Role-column, and add the 
       new column to the DataFrame.
     o Note: using factorize() for nominal categories (Job Title, 
       Location, Company Name) doesn't work well, because the 
       numbers do not have any numeric magnitude. In other 
       words, these categories don't measure anything, they just 
       group data, so numerical comparison / correlation doesn't 
       mean anything statistically.

# example:
# factorize Role level into numbers
label1, unique1 = pd.factorize(df['Role'], sort=False)
df['ManagerRole'] = label1
'''
print(ex3)
ex3_answer = ''

ex4 = '''
Finally, check out the correlations. Does anything correlate with 
anything? Can we make any assumptions?
    o Tip: When correlating against binary variables, sometimes 
      the Spearman correlation might be more sensitive, in 

pandas:
df.corr(method="spearman"
'''
print(ex4)
ex4_answer = ''
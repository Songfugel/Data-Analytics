# PYTHON ANSWERING TEMPLATE

# {} = everything inside comments marked with {} means you should change it to
# suit your exercises, and the contained stuff is only an example.
# some for any code following "# ex.:"

print('''
< < < EXERCISES {2}.{1}.x > > >''')
ex = '''
----------------------------------------------------------------------------
EXERCISES {2}.{1}.x

(ANSWER FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER)

{The exercises description and forewords/assignments/prepwork should be here}
----------------------------------------------------------------------------'''
# IMPORTS HERE
# ex.:
import pandas as pd

# column headersand strings as constant literals if they repeat more than once
# or are options you want to tweak around from one easy place
# ex.:
COL_JOB_TITLE = 'Job Title'
CSV_FILE = "data_salaries_india.csv"

# loading up / preparing data, also making a copy of original data to working
# variable df, that can change
data = pd.read_csv(CSV_FILE)
df = data.copy()

# Everything using these single-line comments in this file are guidelines for 
# using this templete. You should remove all of them from the final version
# and/or replace them with your own uncommented lines. Like the above imports

# The exercise description as a variable, so it shows in the variable explorer
# as:
#
# ex : description
# ex1 : exercise one description
# ex1__pre : backup of thethe state of the data before the assignment, ex df 
# ex1_analysis: possible ex1 analysis
# ex1_sol : the solution/answer to the exercise
# 
# this should make reading the exercises and solutions a flow directly from
# the variable explorer easy

ex1 = ''' << Exercise 1. >>
{What are the main points of this exercise?
  o {Note: some extra specification}
      □ {some clarification}
  o {Possibly some extra assignments}
============================================================================'''

ex1_analysis = ''' >> ANALYSIS: <<
{The verbal analysis of the problem as a basis for the steps taking in the
solution if taks is not self-apparent, or the analysis ispart of the 
exercise itself}
----------------------------------------------------------------------------'''
# backup of DataFrame state at start of assignment
# different prefix so they won't pollute the variable explorer
pre_pre = df.copy()

# make exercise specific imports
#ex.:
#from salary_helper import yearly_wage as fix_wage

# The exercise code here using tmp variables that identify exercise, but 
# different prefix so they won't pollute the variable explorer
tmp1_role = 'some filtering, calculations, functions etc.'

#and finally the solution
ex1_sol = '{The actual solution a df, value or a verbal answer}'


# ***************** BELOW A COMPELETE EXAMPLE ***************
# Note, it doesn't run, since it is missing previous alterations to the df

print(''' 
< < < EXERCISES 2.3.x > > >''')
ex = '''< < < EXERCISES 2.3.x > > >

(ANSWER FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER)

Download the data_salaries_india.csv from Moodle, and consider the 
following questions of the data. Use any means in pandas (or even 
NumPy) you wish to explain your answers.
----------------------------------------------------------------------------'''
import pandas as pd

# column headers as constants
COL_JOB_TITLE = 'Job Title'
COL_ROLE = 'Role'
COL_SALARY = 'Salary'
COL_LOCATION = 'Location'
COL_SALARIES_REPORTED = 'Salaries Reported'
COL_COMPANY_NAME = 'Company Name'

CSV_FILE = 'data_salaries_india.csv'
data = pd.read_csv(CSV_FILE)
df = data.copy()


print('''
< < < EXERCISES 2.1.x > > >''')

ex ='''< < < EXERCISES 2.1.x > > >
Put all your exercises in your Git-project and give the repository address to 
your instructor!

The datasets for these exercises have been collected from kaggle.com (a 
service providing different datasets for practice)

EXERCISE 2.1

import pandas and read the csv-file found in Moodle (loans.csv). Use 
Python coding with pandas to answer the questions.
----------------------------------------------------------------------------'''

ex3 = '''<< Exercise 3. >>
Are there any outliers in the data that might affect the averages 
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
============================================================================'''
pre_ex3 = df.copy()

ex3_analysis = '''>> ANALYSIS: <<
    Going over the salaries, and it seems that under 30000 and over 30000000
    salaries are 7 outliers and significantly differ from the other data as a
    whole. 

    I would surmise that extracting these data rows into their own outlier
    category would make the data more healthier as a whole
----------------------------------------------------------------------------'''

def fix_outlier_wage(row):
    if row[COL_SALARY] > 30000000 or row[COL_SALARY] < 30000:
        return 'Outlier'
    return row[COL_JOB_TITLE]

df[COL_JOB_TITLE] = df.apply(fix_outlier_wage, axis=1)
ex3_sol = df
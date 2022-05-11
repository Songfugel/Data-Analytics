''' Exercises 2 – pandas –module '''

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

import pandas as pd

CSV_FILE = "loans.csv"

data = pd.read_csv(CSV_FILE)
df = data.copy()

COL_CUSTOMER_ID = "Customer ID"
COL_CURRENT_LOAN_AMOUNT = 'Current Loan Amount'
COL_ANNUAL_INCOME = 'Annual Income'
COL_ACTUAL_ANNUAL_INCOME = "Actual Annual Income"
COL_MONTHLY_DEBT = 'Monthly Debt'
COL_LOAN_ID = 'Loan ID'
COL_HOME_OWNERSHIP = 'Home Ownership'
COL_TERM = 'Term'
COL_BANKRUPTCIES = 'Bankruptcies'
COL_PURPOSE = 'Purpose'
COL_NUMBER_OF_OPEN_ACCOUNTS = 'Number of Open Accounts'
COL_NUMBER_OF_CREDIT_PROBLEMS = 'Number of Credit Problems'

ex1 = '''<< Exercise 1. >>
Remove the Customer ID –column from data
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex1 = df.copy()
ex1_sol = df = df.drop(COL_CUSTOMER_ID, axis=1)

ex2 = '''<< Exercise 2. >>
Print the head of the data
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex2 = df.copy()
ex2_sol = df.head() 

ex3 = '''<< Exercise 3. >>
Remove rows from the data that have a too large of a loan
(Current Loan Amount should be less than 99999999)
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex3 = df.copy()
ex3_sol = df = df[df[COL_CURRENT_LOAN_AMOUNT] < 99999999]

ex4 = '''<< Exercise 4. >>
Remove rows that have the annual income as NaN (not a number
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex4 = df.copy()
ex4_sol = df.dropna(subset=[COL_ANNUAL_INCOME])

ex4extra = '''<< Exercise 4.Extra >>
use imputation to use average income as the 
value instead of NaN
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
ex4extra_sol = df = df.fillna(df[COL_ANNUAL_INCOME].mean())

ex5 = '''<< Exercise 5. >>
Get the average Current Loan Amount
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex5 = df.copy()
ex5_sol = round(df[COL_CURRENT_LOAN_AMOUNT].mean(), 2)

ex6 = ''' << Exercise 6. >>
Get the a) highest and b) lowest Annual Income in the dataset
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex6 = df.copy()
ex6a_sol = round(df[COL_ANNUAL_INCOME].max(), 2)
ex6b_sol = round(df[COL_ANNUAL_INCOME].min(), 2)

ex7 = '''<< Exercise 7. >>
Note: The Actual Annual Income should be : Annual Income – 12 * Monthly Debt

Tip: Create a new field with the above instruction to the DataFrame.
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex7 = df.copy()
ex7_sol = df[COL_ACTUAL_ANNUAL_INCOME] = df.apply(
    lambda x: x[COL_MONTHLY_DEBT]*12, axis=1)

def getValue(id_field, id_value, column_name):
    row = df[df[id_field] == id_value]
    return row.iloc[0][column_name]

ex8 = '''<< Exercise 8. >> Get the Home Ownership value of the 
Loan ID = bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex8 = df.copy()
ex8_sol = getValue(COL_LOAN_ID,
    'bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d',
     COL_HOME_OWNERSHIP)

ex9 = '''<< Exercise 9. >>
Get the Actual Annual Income of the loan with the
ID = 76fa89b9-e6a8-49af-afa1-8151315aba8e
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex9 = df.copy()
ex9_sol = getValue(COL_LOAN_ID,
    '76fa89b9-e6a8-49af-afa1-8151315aba8e',
     COL_ACTUAL_ANNUAL_INCOME)

ex10 = '''<< Exercise 10. >>
Get the Loan ID of the loan with the smallest Actual Annual Income
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex10 = df.copy()
ex10_sol = df.loc[df[COL_ANNUAL_INCOME].idxmin()][COL_LOAN_ID]

ex11 = '''<< Exercise 11. >>
How many loans are "Long term"?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex11 = df.copy()
ex11_sol = df[df[COL_TERM] == 'Long Term'].count()[0]

ex12 = ''' << Exercise 12 >>
12. How many loaners have more than 1 bankruptcy?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex12 = df.copy()
ex12_sol = df[df[COL_BANKRUPTCIES] > 1].count()[0]

ex13 = '''
<< Exercise 13. >> How many Short Term loans are for Home Improvements
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex13 = df.copy()
ex13_sol = df[(df[COL_TERM] == 'Short Term') & 
                 (df[COL_PURPOSE] == 'Home Improvements')].count()[0]

ex14 = '''<< Exercise 14. >>
How many unique loan purposes are there?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex14 = df.copy()
ex14_sol = len(df[COL_PURPOSE].unique())

ex15 = '''<< Exercise 15. >>
What are the 3 most common loan purposes?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex15 = df.copy()
ex15_sol = df.groupby(COL_PURPOSE).count().nlargest(3, COL_LOAN_ID)

ex16 = '''<< Exercise 16. >>
Is there a correlation between a) Annual Income and Number of Open Accounts or
is there a correlation between b) Number of Credit Problems and Bankruptcies
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex16 = df.copy()
ex16a_sol = df[COL_ANNUAL_INCOME].corr(df[COL_NUMBER_OF_OPEN_ACCOUNTS])
ex16a_analysis ='''>> ANALYSIS: <<
0.12 some, but not much correlation at all'
----------------------------------------------------------------------------'''

ex16b_sol_orig = df[COL_NUMBER_OF_CREDIT_PROBLEMS].corr(df[COL_BANKRUPTCIES])
ex16b_sol_orig_analysis = '''>> ANALYSIS: <<
Shows no correlation at all... which seems completely against common sense

There seems to be some insane data in bankruptcies with millions of
bankruptcies we need to remove
----------------------------------------------------------------------------'''
ex16b_sol_crazy_rows = df[df[COL_BANKRUPTCIES] > 10]
df = df[df[COL_BANKRUPTCIES] < 10]

ex16b_sol_fixed = df[COL_NUMBER_OF_CREDIT_PROBLEMS].corr(df[COL_BANKRUPTCIES])
ex16b_sol_fixed_analysis=''' >> ANALYSIS: <<
Now ~0.75 very strong correlation as expected
----------------------------------------------------------------------------'''
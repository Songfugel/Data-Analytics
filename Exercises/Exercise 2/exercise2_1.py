import pandas as pd
print('\nEXERCISES 2.1.x\n')

'''
EXERCISE FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER

'''


df_loans = pd.read_csv("loans.csv")

ex1 = '''
1. Remove the Customer ID –column from data
'''
print(ex1)
ex1_answer = df = df_loans.drop("Customer ID", axis=1)

ex2 = '''
2. Print the head of the data
'''
print(ex2)
ex2_answer = df.head() 

ex3 = '''
3. Remove rows from the data that have a too large of a loan
(Current Loan Amount should be less than 99999999)
'''
print(ex3)
ex3_answer = df = df[df['Current Loan Amount'] < 99999999]

ex4 = '''
4. Remove rows that have the annual income as NaN (not a number
'''
print(ex4)
ex4_answer = df.dropna(subset=['Annual Income'])

ex4extra = '''
4.Extra task: use imputation to use average income as the 
value instead of NaN
'''
print(ex4extra)
ex4extra_answer = df = df.fillna(df['Annual Income'].mean())

ex5 = '''
5.  Get the average Current Loan Amount
'''
print(ex5)
ex5_answer = round(df['Current Loan Amount'].mean(), 2)

ex6 = '''
6. Get the a) highest and b) lowest Annual Income in the dataset
'''
print(ex6)
ex6a_answer = round(df['Annual Income'].max(), 2)
ex6b_answer = round(df['Annual Income'].min(), 2)

ex7 = '''
7. Note: The Actual Annual Income should be : Annual Income – 12 * Monthly Debt
Tip: Create a new field with the above instruction to the DataFrame.
'''
print(ex7)
ex7_answer = df["Actual Annual Income"] = df.apply(lambda x: x['Monthly Debt']*12, axis=1)

def getValue(id_field, id_value, column_name):
    row = df[df[id_field] == id_value]
    return row.iloc[0][column_name]

ex8 = '''
8. Get the Home Ownership value of the 
Loan ID = bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d
'''
print(ex8)
ex8_answer = getValue('Loan ID',
    'bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d',
     'Home Ownership')

ex9 = '''
9. Get the Actual Annual Income of the loan with the ID = 
76fa89b9-e6a8-49af-afa1-8151315aba8e
'''
print(ex9)
ex9_answer = getValue('Loan ID',
    '76fa89b9-e6a8-49af-afa1-8151315aba8e',
     'Actual Annual Income')


ex10 = '''
10. Get the Loan ID of the loan with the smallest Actual Annual 
Income
'''
print(ex10)
ex10_answer = df.loc[df['Annual Income'].idxmin()]['Loan ID']

ex11 = '''
11. How many loans are "Long term"?
'''
print(ex11)
ex11_answer = df[df['Term'] == 'Long Term'].count()[0]

ex12 = '''
12. How many loaners have more than 1 bankruptcy?
'''
print(ex12)
ex12_answer = df[df['Bankruptcies'] > 1].count()[0]

ex13 = '''
13. How many Short Term loans are for Home Improvements
'''
print(ex13)
ex13_answer = df[(df['Term'] == 'Short Term') & (df['Purpose'] == 'Home Improvements')].count()[0]

ex14 = '''
14. How many unique loan purposes are there?
'''
print(ex14)
ex14_answer = len(df['Purpose'].unique())

ex15 = '''
15. What are the 3 most common loan purposes?
'''
print(ex15)
ex15_answer = df.groupby('Purpose').count().nlargest(3, "Loan ID")

ex16 = '''
16. Is there a correlation between a) Annual Income and Number of 
Open Accounts or is there a correlation between b) Number of 
Credit Problems and Bankruptcies
'''
print(ex16)
ex16a_answer = df['Annual Income'].corr(df['Number of Open Accounts'])
# 0.12 some, but not much correlation at all

ex16b_answer_orig = df['Number of Credit Problems'].corr(df['Bankruptcies'])
# Shows no correlation... which seems wrong
# .
# ..
# ...
# There seems to be some insane data in bankruptcies we need to remove
ex16b_answer_crazy_rows = df[df['Bankruptcies'] > 10]
df = df[df['Bankruptcies'] < 10]

ex16b_answer_fixed = df['Number of Credit Problems'].corr(df['Bankruptcies'])
# Now ~0.75 very strong correlation as expected
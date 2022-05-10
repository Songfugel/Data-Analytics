import pandas as pd

print('\nEXERCISES 2.1.x\n')

'''
1. Remove the Customer ID –column from data
'''
loans = pd.read_csv("loans.csv")

df = a1 = loans.drop("Customer ID", axis=1)
'''
2. Print the head of the data
'''

a2_head = df.head() 

'''
3. Remove rows from the data that have a too large of a loan
(Current Loan Amount should be less than 99999999)
'''
df = a3 = df[df['Current Loan Amount'] < 99999999]

'''
4. Remove rows that have the annual income as NaN (not a number
'''
a4 = df.dropna(subset=['Annual Income'])

'''
4.Extra task: use imputation to use average income as the 
value instead of NaN

'''
df = a4_extra = df.fillna(df['Annual Income'].mean())

'''
5.  Get the average Current Loan Amount
'''
a5_mean = round(df['Current Loan Amount'].mean(), 2)

'''
6. Get the highest and lowest Annual Income in the dataset
'''
a6_max = round(df['Annual Income'].max(), 2)

a6_min = round(df['Annual Income'].min(), 2)

'''
7. Note: The Actual Annual Income should be : Annual Income – 12 * Monthly Debt
Tip: Create a new field with the above instruction to the DataFrame.
'''
df["Actual Annual Income"] = df.apply(lambda x: x['Monthly Debt']*12, axis=1)

def getValue(id_field, id_value, column_name):
    row = df[df[id_field] == id_value]
    return row.iloc[0][column_name]

'''
8. Get the Home Ownership value of the 
Loan ID = bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d
'''
a8_ownership_value = getValue('Loan ID',
    'bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d',
     'Home Ownership')

'''
9. Get the Actual Annual Income of the loan with the ID = 
76fa89b9-e6a8-49af-afa1-8151315aba8e
'''
a9_actual_annual_income = getValue('Loan ID',
    '76fa89b9-e6a8-49af-afa1-8151315aba8e',
     'Actual Annual Income')


'''
10. Get the Loan ID of the loan with the smallest Actual Annual 
Income
'''
a10 = df.loc[df['Annual Income'].idxmin()]['Loan ID']

'''
11. How many loans are "Long term"?
'''
a11 = df[df['Term'] == 'Long Term'].count()[0]

'''
12. How many loaners have more than 1 bankruptcy?
'''
a12 = df[df['Bankruptcies'] > 1].count()[0]

'''
13. How many Short Term loans are for Home Improvements
'''
a13 = df[(df['Term'] == 'Short Term') & (df['Purpose'] == 'Home Improvements')].count()[0]

'''
14. How many unique loan purposes are there?
'''
a14 = len(df['Purpose'].unique())

'''
15. What are the 3 most common loan purposes?
'''
a15 = df.groupby('Purpose').count().nlargest(3, "Loan ID")

'''
16. Is there a correlation between a) Annual Income and Number of 
Open Accounts or is there a correlation between b) Number of 
Credit Problems and Bankruptcies
'''

a16a = df['Annual Income'].corr(df['Number of Open Accounts'])
# 0.12 some, but not much correlation at all

a16b_orig = df['Number of Credit Problems'].corr(df['Bankruptcies'])
# Shows no correlation... which seems wrong
# .
# ..
# ...
# There seems to be some insane data in bankruptcies we need to remove
a16b_crazy_rows = df[df['Bankruptcies'] > 10]
df = df[df['Bankruptcies'] < 10]

a16b_fixed = df['Number of Credit Problems'].corr(df['Bankruptcies'])
# Now ~0.75 very strong correlation as expected

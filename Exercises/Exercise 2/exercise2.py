import pandas as pd

print('\nEXERCISE 2.1.\n')

loans = pd.read_csv("loans.csv")

df = a1 = loans.drop("Customer ID", axis=1)

a2_head = df.head() 

df = a3 = df[df['Current Loan Amount'] < 99999999]

a4 = df.dropna(subset=['Annual Income'])
df = a4_extra = df.fillna(df['Annual Income'].mean())

a5_mean = round(df['Current Loan Amount'].mean(), 2)

a6_max = round(df['Annual Income'].max(), 2)
a7_min = round(df['Annual Income'].min(), 2)

df["Actual Annual Income"] = df.apply(lambda x: x['Monthly Debt']*12, axis=1)

def getValue(id_field, id_value, column_name):
    row = df[df[id_field] == id_value]
    return row.iloc[0][column_name]

a8_actual_annual_income = getValue('Loan ID',
    '76fa89b9-e6a8-49af-afa1-8151315aba8e',
     'Actual Annual Income')

a9_ownership_type = getValue('Loan ID',
    'bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d',
     'Home Ownership')

a10_id_of_lowest_ann_inc = df.loc[df['Annual Income'].idxmin()]['Loan ID']

a11_long_term_loans = df[df['Term'] == 'Long Term'].count()[0]
     
a12_bankruptcies = df[df['Bankruptcies'] > 1].count()[0]

a13_st_for_home_imp = df[(df['Term'] == 'Short Term') & (df['Purpose'] == 'Home Improvements')].count()[0]

a14_unq_purposes = len(df['Purpose'].unique())

a15_top3_purposes = df.groupby('Purpose').count().nlargest(3, "Loan ID")

a16_corr = df['Annual Income'].corr(df['Number of Open Accounts'])
# 0.12 some, but not much correlation at all

a17_corr = df['Number of Credit Problems'].corr(df['Bankruptcies'])
# Shows no correlation... which seems wrong
# .
# ..
# ...
# There seems to be some insane data in bankruptcies we need to remove
a17_crazy_rows = df[df['Bankruptcies'] > 10]
df = df[df['Bankruptcies'] < 10]
a17_corr_fixed = df['Number of Credit Problems'].corr(df['Bankruptcies'])
# Now ~0.75 very strong correlation as expected


print('\nEXERCISE 2.2.\n')


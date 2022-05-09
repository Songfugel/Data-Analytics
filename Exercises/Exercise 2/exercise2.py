import pandas as pd

#1

print('\nEXERCISE 1.\n')

loans = pd.read_csv("loans.csv")

df = loans.drop("Customer ID", axis=1)

df_head = df.head() 
print(df_head)

df = df[df['Current Loan Amount'] < 99999999]

df = df.dropna(subset=['Annual Income'])

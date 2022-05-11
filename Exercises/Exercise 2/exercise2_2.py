import pandas as pd


df_purchases = pd.read_csv("purchases.csv")

df = df_purchases.copy()

# column name string literals
INDEX = 'Index'
PURCHACE_ORDER_NUMBER = 'Purchase Order Number'
TOTAL_PRICE = 'Total Price'
ITEM_NAME = 'Item Name'
ITEM_DESCRIPTION = 'Item Description'
PURCHASE_DATE = 'Purchase Date'
DEPARTMENT_NAME = 'Department Name'
CREATION_DATE = 'Creation Date'
ACQUISITION_TYPE = 'Acquisition Type'

# some helper stuff
def get_rows(id_field, id_value):
    rows = df[df[id_field] == id_value]
    return rows

def get_filtered_rows(column, filter_lambda):
    rows = df[filter_lambda(df[column])]
    return rows

print('\nEXERCISES 2.2.x\n')
'''
EXERCISE FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER

'''

ex1 = '''
1. What was the total price sum of the Purchase Order Number 
018H2015? (14 rows in total
'''
print(ex1)
ex1_answer = round(get_rows(PURCHACE_ORDER_NUMBER,'018H2015')[TOTAL_PRICE].sum(), 2)

ex2 = '''
2. What is the name and description of the purchased item with the 
Purchase Order Number 3176273?
'''
print(ex2)
ex2_answer = get_rows(PURCHACE_ORDER_NUMBER, '3176273')[[PURCHACE_ORDER_NUMBER,ITEM_NAME, ITEM_DESCRIPTION]]

ex3='''
3. What are the 5 most common Departments in the data?
'''
print(ex3)
ex3_answer = get_filtered_rows(PURCHASE_DATE, lambda r: r.str.find('2013') >= 0).count()[0]

ex4 = '''
4. What are the 5 most common Departments in the data?
'''
print(ex4)
df_ex4 = df.groupby(DEPARTMENT_NAME).count()
ex4_answer = df_ex4.nlargest(5, CREATION_DATE)

ex4extra ='''
4. Extra task: What are 3 Departments using most money in 
the data
'''
print(ex4extra)
df_ex4extra = df.groupby(DEPARTMENT_NAME)[TOTAL_PRICE].sum()
ex4extra_answer = df_ex4extra.nlargest(3)

ex5 = '''
5. Sort the data by Department Name
'''
print(ex5)
ex5_answer = df.sort_values(DEPARTMENT_NAME)

ex6 = '''
6. How many purchases in the data were IT Goods and had the 
total price more than 50000 dollars?
'''
print(ex6)
ex6_answer = df[(df[ACQUISITION_TYPE] == 'IT Goods') & (df[TOTAL_PRICE] > 50000)].count()[0]

ex7 = '''
7. How many of the purchases have anything to do with IT? (IT 
Goods, IT Services, IT Telecommunications
'''
print(ex7)
ex7_answer = df[df[ACQUISITION_TYPE].isin(['IT Goods', 'IT Services', 'IT Telecommunications'])].count()[0]

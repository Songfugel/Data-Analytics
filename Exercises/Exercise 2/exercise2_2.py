import pandas as pd


df_purchases = pd.read_csv("purchases.csv")

df = df_purchases

# column name string literals
INDEX = 'Index'
PURCHACE_ORDER_NUMBER = 'Purchase Order Number'
TOTAL_PRICE = 'Total Price'
ITEM_NAME = 'Item Name'
ITEM_DESCRIPTION = 'Item Description'
PURCHASE_DATE = 'Purchase Date'
DEPARTMENT_NAME = 'Department Name'
CREATION_DATE = 'Creation Date'

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

ex1_answer = round(get_rows(PURCHACE_ORDER_NUMBER,'018H2015')[TOTAL_PRICE].sum(), 2)

ex2 = '''
2. What is the name and description of the purchased item with the 
Purchase Order Number 3176273?
'''
ex2_answer = get_rows(PURCHACE_ORDER_NUMBER, '3176273')[[PURCHACE_ORDER_NUMBER,ITEM_NAME, ITEM_DESCRIPTION]]

ex3='''
3. What are the 5 most common Departments in the data?
'''
ex3_answer = get_filtered_rows(PURCHASE_DATE, lambda r: r.str.find('2013') >= 0).count()[0]


ex4 = '''
4. What are the 5 most common Departments in the data?
'''
df_ex4 = df.groupby(DEPARTMENT_NAME).count()
ex4_answer = df_ex4.nlargest(5, CREATION_DATE)


'''
4. Extra task: What are 3 Departments using most money in 
the data
'''
df_ex4extra = df.groupby(DEPARTMENT_NAME)[TOTAL_PRICE].sum()
ex4extra_answer = df_ex4extra.nlargest(3)




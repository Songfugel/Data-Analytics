import pandas as pd

print('\nEXERCISE 2.2.\n')

purchases = pd.read_csv("purchases.csv")

df = purchases

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

'''
2.1 What was the total price sum of the Purchase Order Number 
018H2015? (14 rows in total
'''

a1_purch_total = round(get_rows(PURCHACE_ORDER_NUMBER,'018H2015')[TOTAL_PRICE].sum(), 2)

'''
2.2 What is the name and description of the purchased item with the 
Purchase Order Number 3176273?
'''

a2_name_n_desc = get_rows(PURCHACE_ORDER_NUMBER, '3176273')[[PURCHACE_ORDER_NUMBER,ITEM_NAME, ITEM_DESCRIPTION]]

'''
2.3 What are the 5 most common Departments in the data?
'''
a3_purch_count_in_2013 = get_filtered_rows(PURCHASE_DATE, lambda r: r.str.find('2013') >= 0).count()[0]


'''
2.4 What are the 5 most common Departments in the data?
'''

a4_grouped = df.groupby(DEPARTMENT_NAME).count()
a4_five_most_com_deps = a4_grouped.nlargest(5, CREATION_DATE)


'''
2.4 Extra task: What are 3 Departments using most money in 
the data
'''
a4_extra_grouped = df.groupby(DEPARTMENT_NAME)[TOTAL_PRICE].sum()
a4_extra_top3_spenders = a4_extra_grouped.nlargest(3)




print(''' 
< < < EXERCISES 2.2.x > > >''')

ex ='''< < < EXERCISES 2.2.x > > >
Put all your exercises in your Git-project and give the repository address to 
your instructor!

The datasets for these exercises have been collected from kaggle.com (a 
service providing different datasets for practice)

EXERCISE 2.1

import pandas and read the csv-file found in Moodle (loans.csv). Use 
Python coding with pandas to answer the questions.
----------------------------------------------------------------------------'''

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

import pandas as pd

CSV_FILE = "purchases.csv"

data = pd.read_csv(CSV_FILE)
df = data.copy()

# some helper stuff, that aren't that useful, but just tried them out
def get_rows(column, val):
    rows = df[df[column] == val]
    return rows

def get_filtered_rows(column, func):
    rows = df[func(df[column])]
    return rows

ex1 = '''<< Exercise 1. >>
What was the total price sum of the Purchase Order Number 
018H2015? (14 rows in total
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex1 = df.copy()
ex1_sol = round(
    get_rows(PURCHACE_ORDER_NUMBER,'018H2015')[TOTAL_PRICE].sum(), 2)

ex2 = '''<< Exercise 2. >>
What is the name and description of the purchased item with the 
Purchase Order Number 3176273?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex2 = df.copy()
ex2_sol = get_rows(PURCHACE_ORDER_NUMBER, '3176273')[
    [PURCHACE_ORDER_NUMBER,ITEM_NAME, ITEM_DESCRIPTION]]

ex3='''<< Exercise 3. >>
What are the 5 most common Departments in the data?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex3 = df.copy()
ex3_sol = get_filtered_rows(
    PURCHASE_DATE, lambda r: r.str.find('2013') >= 0).count()[0]

ex4 = '''<< Exercise 4. >>
What are the 5 most common Departments in the data?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex3 = df.copy()
tmp4_df = df.groupby(DEPARTMENT_NAME).count()
ex4_sol = tmp4_df.nlargest(5, CREATION_DATE)

ex4extra ='''<< Exercise 4.EXTRA >>
task: What are 3 Departments using most money in the data
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex4extra = df.copy()
tmp4e_df = df.groupby(DEPARTMENT_NAME)[TOTAL_PRICE].sum()
ex4extra_sol = tmp4e_df.nlargest(3)

ex5 = '''<< Exercise 5. >>
Sort the data by Department Name
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex5 = df.copy()
ex5_sol = df.sort_values(DEPARTMENT_NAME)

ex6 = '''<< Exercise 6. >>
How many purchases in the data were IT Goods and had the total price more than
50000 dollars?
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex5 = df.copy()
ex6_sol = df[(df[ACQUISITION_TYPE] == 'IT Goods') &
                (df[TOTAL_PRICE] > 50000)].count()[0]

ex7 = '''<< Exercise 7. >>
How many of the purchases have anything to do with IT? (IT Goods, IT Services,
IT Telecommunications)
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex7 = df.copy()
ex7_sol = df[df[ACQUISITION_TYPE].isin(
    ['IT Goods', 'IT Services', 'IT Telecommunications'])].count()[0]

# PYTHON ANSWERING TEMPLATE

# {} = everything inside comments marked with {} means you should change it to
# suit your exercises, and the contained stuff is only an example.
# some for any code following "# ex.:"

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
df_salaries_india = pd.read_csv(CSV_FILE)
df = df_salaries_india.copy()

# Everything using these single-line comments in this file are guidelines for 
# using this templete. You should remove all of them from the final version
# and/or replace them with your own uncommented lines. Like the above imports

print(''' 
      ¤ ¤ ¤ ¤ ¤ ¤    EXERCISES {2}.{3}.x    ¤ ¤ ¤ ¤ ¤ ¤''')

ex = '''
x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-
EXERCISES {2}.{3}.x

(ANSWER FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER)

{The exercises description and forewords/assignments/prepwork should be here}
x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-'''

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

ex1 = '''
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
Exercise 1. {What are the main points of this exercise?
  o {Note: some extra specification}
      □ {some clarification}
  o {Possibly some extra assignments}
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''

ex1_analysis = '''
----------------------------------------------------------------------------
ANALYSIS: {The verbal analysis of the problem as a basis for the steps taking in the
solution if taks is not self-apparent, or the analysis ispart of the 
exercise itself}
----------------------------------------------------------------------------'''
# backup of DataFrame state at start of assignment
ex1__pre = df.copy()

# make exercise specific imports
#ex.:
#from salary_helper import yearly_wage as fix_wage

# The exercise code here using tmp variables that identify exercise, but 
# different prefix so they won't pollute the variable explorer
tmp1_role = 'some filtering, calculations, functions etc.'

#and finally the solution
ex1_sol = '{The actual solution a df, value or a verbal answer}'

print(''' 
< < < EXERCISES 2.3.x > > >''')
ex = '''< < < EXERCISES 2.3.x > > >

(ANSWER FORMAT OPTIMIZED FOR SPYDER VARIABLE EXPLORER)

Download the data_salaries_india.csv from Moodle, and consider the 
following questions of the data. Use any means in pandas (or even 
NumPy) you wish to explain your answers.
----------------------------------------------------------------------------'''
import pandas as pd
from salary_helper import yearly_wage as fix_wage

# column headers as constants
COL_JOB_TITLE = 'Job Title'
COL_ROLE = 'Role'
COL_SALARY = 'Salary'
COL_LOCATION = 'Location'
COL_SALARIES_REPORTED = 'Salaries Reported'
COL_COMPANY_NAME = 'Company Name'

CSV_FILE = 'data_salaries_india.csv'
data = pd.read_csv(CSV_FILE)
df = data.copy()


ex1 = '''<< Exercise 1. >>
Before we can do anything with the salaries, we have to convert 
them into something more usable
  o Note: the salaries can be yearly, monthly or hourly salaries
      □ We don't also need the Indian rupee –sign (₹)
  o You can use the template in Moodle to help you out with this 
    (Salary filtering, pandas exercise 3)
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex1 = df.copy()

ex1_analysis = '''>> ANALYSIS: <<
    The reported salaries seems to be completely irrelevant and unusable data
    column, since it doesn't seem too relevant of an information for anything
    and the data between the entries stays relatively the same with few
    outliers. So I think it should be dropped.
    
    Also the wages should be reformatted into number format
----------------------------------------------------------------------------'''

df = df.drop(COL_SALARIES_REPORTED, axis=1)
ex1_sol = df[COL_SALARY]= df.apply(fix_wage, axis=1)

ex2 = '''<< Exercise 2. >>
What are the most common values in different fields (Job Titles, Companies,
Location)? Based on the distribution, is the data balanced or not?
    o Extra task: there seem to be some Job Titles that are almost the same,
      like "Machine Learning Data Associate and Machine Learning Associate,
      combine these into something common
      
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex2 = df.copy()

# DFs for analysis purposes
ex2_tmp_role = df.groupby(COL_ROLE).count()
ex2_tmp_title = df.groupby(COL_JOB_TITLE).count()
ex2_tmp_location = df.groupby(COL_LOCATION).count()

ex2_analysis = '''>> ANALYSIS: <<
    ROLE:
    There seem to be a only two roles, and 5:1 ratio of specialists vs managers

    LOCATION:
    There are only 5 different locations, and the location data is extremely
    balanced with all but Bangalore having similar amount of entries. Even 
    Bangalore has only twice as much as the others.
        Bangalore
        Hyderabad
        Mumbai
        New Delhi
        Pune

    JOB TITLE: 
    There seem to be 4 titles that are extremely common
        Data Analyst
        Data Engineer
        Data Scientist
        Machine Learning Engineer
    
    Then each of these have several sub-categories based on experience and
    alternative spelling like "Software Engineer - Machine Learning" vs
    Machine Learning Engineer
    
    SOLUTION
    New categories:
        Data Analyst
        Data Engineer
        Data Scientist
        Machine Learning Engineer
        Other

    Logic to relabel titles:
        
    if machine learning ->
        Machine Learning Engineer
        
    else if DATA ->
        if analyst -> Data Analyst    
        if engineer -> Data Engineer
        if scientist -> Data Scientist
    else
     Other
----------------------------------------------------------------------------'''

def retiteler(title:str)-> str:
    '''
    Simple function to re-title the Job Titles to more compact and loosely def.
    categories to make the data slightly less accurate, but more much more
    healthy
    
    Parameters
    ----------
    title : str
        Job title of the row

    Returns
    -------
    str
        Re-assigned job title.
    '''
    title = title.lower()
    if 'machine learning' in title:
        return 'Machine Learning Engineer'
    if 'data' in title:
        if 'analyst' in title: return 'Data Analyst'
        if 'engineer' in title: return 'Data Engineer'
        if 'scientist' in title: return 'Data Scientist'
    return 'Other'

df[COL_JOB_TITLE] = df[COL_JOB_TITLE].apply(retiteler)
ex2_sol = df.groupby(COL_JOB_TITLE).count()

ex3 = '''<< Exercise 3. >>
Are there any outliers in the data that might affect the averages 
negatively (certain salaries)? Manage the outliers as you best see 
fit (either remove them or leave them, based on your analysis
     
     o If we want to correlate upon categories (ordinal or binary), we 
       need to use factorize(). Factorize the Role-column, and add the 
       new column to the DataFrame.
     o Note: using factorize() for nominal categories (Job Title, 
       Location, Company Name) doesn't work well, because the 
       numbers do not have any numeric magnitude. In other 
       words, these categories don't measure anything, they just 
       group data, so numerical comparison / correlation doesn't 
       mean anything statistically.

# example:
# factorize Role level into numbers
label1, unique1 = pd.factorize(df['Role'], sort=False)
df['ManagerRole'] = label1
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex3 = df.copy()

ex3_analysis = '''>> ANALYSIS: <<
    Going over the salaries, and it seems that under 30000 and over 30000000
    salaries are 7 outliers and significantly differ from the other data as a
    whole. 

    I would surmise that extracting these data rows into their own outlier
    category would make the data more healthier as a whole
----------------------------------------------------------------------------'''

def fix_outlier_wage(row):
    if row[COL_SALARY] > 30000000 or row[COL_SALARY] < 30000:
        return 'Outlier'
    return row[COL_JOB_TITLE]

df[COL_JOB_TITLE] = df.apply(fix_outlier_wage, axis=1)
ex3_sol = df

ex4 = '''<< Exercise 4. >>
Finally, check out the correlations. Does anything correlate with 
anything? Can we make any assumptions?
    o Tip: When correlating against binary variables, sometimes 
      the Spearman correlation might be more sensitive, in 

pandas:
df.corr(method="spearman"
¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤'''
pre_ex4 = df.copy()

# need to factorize data first
df[COL_JOB_TITLE + '_f'], n1 = pd.factorize(df[COL_JOB_TITLE], sort=False)
df[COL_ROLE + '_f'], n2 = pd.factorize(df[COL_ROLE], sort=False)
df[COL_LOCATION + '_f'], n3 = pd.factorize(df[COL_LOCATION], sort=False)
df[COL_COMPANY_NAME + '_f'], n4 = pd.factorize(df[COL_LOCATION], sort=False)

ex4_corr_loc = df[COL_SALARY].corr(df[COL_LOCATION+ '_f'])
ex4_corr_title = df[COL_SALARY].corr(df[COL_JOB_TITLE+ '_f'])
ex4_corr_role = df[COL_SALARY].corr(df[COL_ROLE+ '_f'])
ex4_corr_company = df[COL_SALARY].corr(df[COL_COMPANY_NAME+ '_f'])

ex4_corr_loc_spear = df[COL_SALARY].corr(
    df[COL_LOCATION+ '_f'], method="spearman")

ex4_corr_title_spear = df[COL_SALARY].corr(
    df[COL_JOB_TITLE+ '_f'], method="spearman")

ex4_corr_role_spear = df[COL_SALARY].corr(
    df[COL_ROLE+ '_f'], method="spearman")

ex4_corr_company_spear = df[COL_SALARY].corr(
    df[COL_COMPANY_NAME+ '_f'], method="spearman")


ex4_sol = '''>> ANALYSIS: <<
    Going over the correlations
    
    Company:     -0.05 <- NONE
    Comp spear:  -0.11 <- NONE
    
    loc:         -0.05 <- NONE
    loc spear:   -0.11 <- NONE
    
    role:         0.40 <- Quite a bit of correlation
    role spear:   0.43 <- Spear shows even more correlation
    
    title:       -0.08 <- NONE
    title spear: -0.19 <- SOME corr, but not that significant

    It would seem that location and title has no direct correlation to salary, 
    but role seems to have a significant correlation to salary.
    
    From common sense, a more thorough study might identify a more deeper
    correlation with a combination of location, company and role with price
----------------------------------------------------------------------------'''
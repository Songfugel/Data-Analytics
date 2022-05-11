# helper function for pandas to convert all salaries
# into yearly integer salaries
def yearly_wage(row):
    # the last two characters determine if it's yearly, monthly, hourly
    period = row['Salary'][-2:]
    
    # remove all commas and combine all numbers
    number = int(''.join(filter(str.isdigit, row['Salary'])))
    
    # if it's hourly, the average work hours per year in India is
    # approximately 2117.01 (might change in future)
    if period == "hr":
        number = int(number * 2117.01)
    elif period == "mo":
        # months to year
        number = int(number * 12)
    
    # return the yearly salary in integer format
    return number
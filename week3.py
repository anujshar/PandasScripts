# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 17:15:32 2018

@author: anujs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame([{'Name':'Chris', 'Item Purchased': 'Sponge', 'Cost' : 22.50},
                   {'Name':'Kevin', 'Item Purchased': 'Kitty Litter', 'Cost' : 2.50},
                   {'Name':'Filip', 'Item Purchased': 'Spoon', 'Cost' : 5.00}], 
                    index = ['Store 1', 'Store 2', 'Store 3'])

#creating a new column using a hard-coded list

df['Date'] = {'December 1', 'March 1', 'November 1'}
df['Delivered'] = True
df['Feedback'] = pd.Series({'Store 1': 'Positive', 'Store 3': 'Negative'}) # in this example pandas put NaN for missing values

                #print(df)
                
#merging data frames

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')

student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

all_df = pd.merge(staff_df, student_df, how = 'outer', left_index = True, right_index = True)

left_df = pd.merge(staff_df, student_df, how = 'left', left_index = True, right_index = True)

right_df = pd.merge(staff_df, student_df, how = 'right', left_index = True, right_index = True)

#print(left_df)

#print(right_df)

#merging data frames using multiple indeces and multiple columns

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])

merger_df = pd.merge(staff_df, student_df, how='outer', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])
                #print(merger_df)
                
#pandas idioms

census_df = pd.read_csv('census.csv')
#calling multiple functions in one statement
(census_df.where(census_df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

census_df.set_index(['STNAME', 'CTYNAME'])

                #print(census_df.head())

#apply function to find min or max

def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    #to add columns in the existing data frame
    #row['max'] = np.max(data)
    #row['min'] = np.min(data)
    #return row
    return pd.Series({'min': np.min(data), 'max': np.max(data)})
                #print(census_df.apply(min_max, axis=1).head())
                
# apply function using lambda
                
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
                #print(census_df.apply(lambda x: np.max(x[rows]), axis=1))
                
#group by

# passing a function to the groupby function
group_df = pd.read_csv('census.csv')
group_df.set_index(['STNAME', 'CTYNAME'], inplace = True)

def fun(item):
    if item[0] == 'Texas':
        return 1
    return 2

                #print(group_df.groupby(fun).size())      

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')


#agg function on group by to aggregate results after manipulation
# groupby level = 0 groups by index
                #print(group_df.groupby(level=0).agg({'CENSUS2010POP': np.min}))

#syntax to create a new column in the dataframe                
                #print(group_df.groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average}))
#group_df = group_df.groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
#print(pd.cut(group_df['avg'], 10))


#pivot tables
cars_df = pd.read_csv('cars.csv')
                #print(cars_df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean))

#date functionality
#timestamp
                #print(pd.Timestamp('2017-01-01 10:10AM'))

#period
                #print(type(pd.Period('1/2019')))

#periodIndex

period_series = pd.Series(list('def'), [pd.Period('2017-09'), pd.Period('2017-10'), pd.Period('2017-11')])
                #print(type(period_series.index))

#converting to datetime

d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
                #print(ts3)
ts3.index = pd.to_datetime(ts3.index, dayfirst=True)
                #print(ts3)
                
#time delta
                
                #print(pd.Timestamp('2017-02-02 10:10AM') - pd.Timestamp('2017-03-03 12:03PM'))
                
#Dates in dataframe
                
dates = pd.date_range('10-01-2016', periods = 9, freq = '2W-SUN')
                #print(dates)

dates_df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5,10,9).cumsum(),
                        'Count 2': 120 + np.random.randint(-5,10,9)}, index = dates)

#weekday of date index
                #print(dates_df.index.weekday_name)
                
                #print(dates_df)
                
#difference between each dates value
                #print(dates_df.diff())

# find average by month
                #print(dates_df.resample('M').mean())
                
# values with particular year in index dates or with rangeof dates

                #print(dates_df['2017'])
                #print(dates_df['2016-11':])
                
                
# change frequency of date index; ffill method mehtods empty values with previous values
                
                #print(dates_df.asfreq('W', method = 'ffill'))
                
#plot a chart

dates_df.plot()
                

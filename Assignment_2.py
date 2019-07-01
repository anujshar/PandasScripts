# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 00:28:48 2018

@author: anujs
"""

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')

census_df = pd.read_csv('census.csv')

def answer_one():
    max = df['Total'].max()
    cf = df.where(df['Total'] == max).dropna()
    return cf.index.values[0]

def answer_two():
    df['Difference'] = abs(df['Total']-df['Total.1'])
    max = df['Difference'].max()
    cf = df.where(df['Difference'] == max).dropna()
    return cf.index.values[0]

def answer_three():
    cf = df[(df['Gold.1'] != 0) & (df['Gold'] != 0)]
    cf['Gold_difference'] = abs((cf['Gold'] - cf['Gold.1'])/(cf['Gold'] + cf['Gold.1'] + cf['Gold.2']))
    max = cf['Gold_difference'].max()
    ef = cf.where(cf['Gold_difference'] == max).dropna()
    return ef.index.values[0]

def answer_four():
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']*1
    Points = pd.Series(df['Points'])
    return Points

def answer_five():
    temp = census_df.groupby('STNAME').size().idxmax()
    return temp

def answer_six():
    temp = census_df[census_df['SUMLEV'] == 50]
    return (list)((temp.groupby('STNAME')['CENSUS2010POP'].nlargest(3).sum(level=0)).nlargest(3).index.values)

def answer_seven():
    temp = census_df[census_df['SUMLEV'] == 50].copy()
    temp.set_index('CTYNAME')
    temp['MINPOP'] = None
    temp['MAXPOP'] = None
    temp['DIFF'] = None
    temp['MINPOP'] = temp.loc[:, ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']].min(axis=1)
    temp['MAXPOP'] = temp.loc[:, ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']].max(axis=1)
    temp['DIFF'] = temp.loc[:, 'MAXPOP'] - temp.loc[:, 'MINPOP']
    answer = temp.loc[temp['DIFF'].idxmax()]
    return answer.loc['CTYNAME']
    

def answer_eight():
    temp = census_df[census_df['SUMLEV'] == 50].copy()
    temp = temp[((temp['REGION'] == 1) | (temp['REGION'] == 2)) & (temp['POPESTIMATE2015'] > temp['POPESTIMATE2014']) & (temp['CTYNAME'].str.startswith("Washington"))]
    answer = temp[['STNAME','CTYNAME']]
    return answer
print(answer_six())

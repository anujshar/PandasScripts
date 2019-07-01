# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:44:19 2019

@author: anujs
"""
import pandas as pd
import numpy as np


#read and clean energy indicators

def answer_one():
    import pandas as pd
    import numpy as np
    energy = pd.read_excel('Energy Indicators.xls', usecols = 'C:F', skiprows = 17, skipfooter=38, index_col = 0)
    energy.columns = ['Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.index.names = ['Country']
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    cols = ['Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[cols] = energy[cols].applymap(lambda x: np.nan if isinstance(x, str) else x)
    energy.rename(index={'Republic of Korea':'South Korea'},inplace=True)
    energy.rename(index={"United States of America20": "United States"},inplace=True)
    energy.rename(index={"United Kingdom of Great Britain and Northern Ireland19": "United Kingdom"},inplace=True)
    energy.rename(index={"China, Hong Kong Special Administrative Region3": "Hong Kong"},inplace=True)
    energy.rename(index={"Australia1": "Australia"},inplace=True)
    energy.rename(index={"China2": "China"},inplace=True)
    energy.rename(index={"China, Macao Special Administrative Region4": "Macao"},inplace=True)
    energy.rename(index={"Denmark5": "Denmark"},inplace=True)
    energy.rename(index={"France6": "France"},inplace=True)
    energy.rename(index={"Greenland7": "Greenland"},inplace=True)
    energy.rename(index={"Indonesia8": "Indonesia"},inplace=True)
    energy.rename(index={"Italy9": "Italy"},inplace=True)
    energy.rename(index={"Japan10": "Japan"},inplace=True)
    energy.rename(index={"Kuwait11": "Kuwait"},inplace=True)
    energy.rename(index={"Netherlands12": "Netherlands"},inplace=True)
    energy.rename(index={"Portugal13": "Portugal"},inplace=True)
    energy.rename(index={"Saudi Arabia14": "Saudi Arabia"},inplace=True)
    energy.rename(index={"Serbia15": "Serbia"},inplace=True)
    energy.rename(index={"Spain16": "Spain"},inplace=True)
    energy.rename(index={"Switzerland17": "Switzerland"},inplace=True)
    energy.rename(index={"Ukraine18": "Ukraine"},inplace=True)
    energy.rename(index={"Denmark5": "Denmark"},inplace=True)
    energy.rename(index={"Bolivia (Plurinational State of)": "Bolivia"},inplace=True)
    energy.rename(index={"Falkland Islands (Malvinas)": "Falkland Islands"},inplace=True)
    energy.rename(index={"Iran (Islamic Republic of)": "Iran"},inplace=True)
    energy.rename(index={"Micronesia (Federated States of)": "Micronesia"},inplace=True)
    energy.rename(index={"Sint Maarten (Dutch part)": "Sint Maarten"},inplace=True)
    energy.rename(index={"Venezuela (Bolivarian Republic of)": "Venezuela"},inplace=True)

#print(energy)


#read and clean world bank data

    GDP = pd.read_csv('world_bank.csv', skiprows=4, index_col=0)
    GDP.rename(index={"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"}, inplace=True)

#print(GDP.loc['Hong Kong'])

#read and clean sci-amgo journal

    ScimEn = pd.read_excel('scimagojr-3.xlsx', index_col = 1)
#print(ScimEn.head())




    merge1_df = pd.merge(energy, GDP, how = 'outer', left_index = True, right_index = True)
    merge_df = pd.merge(merge1_df, ScimEn, how = 'outer', left_index = True, right_index = True)
    columns_df = merge_df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].copy()
    #columns_df.loc['Iran']['2015'] = 0
    cols2 = ['2015', '2014']
    columns_df[cols2] = columns_df[cols2].applymap(lambda x: 0 if np.isnan(x) else x)
    answer_df = columns_df.where(columns_df['Rank'] <= 15).dropna().copy()
    answer_df[cols2] = answer_df[cols2].applymap(lambda x: np.nan if x == 0 else x)
    #answer_df.replace(0, np.nan)
    #answer_df.loc['Iran']['2015'] = np.NAN
    return answer_df
    
    

def answer_two():
    import pandas as pd
    import numpy as np
    energy = pd.read_excel('Energy Indicators.xls', parse_cols = 'C:F', skiprows = 17, skipfooter=38, index_col = 0)
    energy.columns = ['Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy.index.names = ['Country']
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    cols = ['Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[cols] = energy[cols].applymap(lambda x: np.nan if isinstance(x, str) else x)
    
    GDP = pd.read_csv('world_bank.csv', skiprows=4, index_col=0)
    GDP.rename(index={"Korea, Rep.": "South Korea","Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"}, inplace=True)
    
    ScimEn = pd.read_excel('scimagojr-3.xlsx', index_col = 1)
    
    merge1_df = pd.merge(energy, GDP, how = 'outer', left_index = True, right_index = True)
    merge_df = pd.merge(merge1_df, ScimEn, how = 'outer', left_index = True, right_index = True)
    columns_df = merge_df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].copy()
    columns_df.loc['Iran']['2015'] = 0
    count = columns_df.where(columns_df['Rank'] > 15).dropna().index.size
    return count


def answer_three():
    Top15 = answer_one()
    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    avgGDP = Top15.apply(lambda x: np.mean(x[years]), axis=1)
    return avgGDP
    
    
def answer_four():
    Top15 = answer_one()
    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    avgGDP = Top15.apply(lambda x: np.mean(x[years]), axis=1)
    answer_index = (str)(avgGDP.nlargest(6).index[-1])
    return Top15.loc[answer_index]['2015'] - Top15.loc[answer_index]['2006']
    

def answer_five():
    Top15 = answer_one()
    answer = (float)(np.mean(Top15['Energy Supply per Capita'], axis=None))
    return answer

def answer_six():
    Top15 = answer_one()
    tp = (Top15['% Renewable'].idxmax(), Top15['% Renewable'].max())
    return tp

def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15['Self-citations']/Top15['Citations']
    tp = (Top15['Ratio'].idxmax(), Top15['Ratio'].max())
    return tp


def answer_eight():
    Top15 = answer_one()
    Top15['Estimate'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    return Top15['Estimate'].nlargest(3).idxmin()

def plot9():
    import matplotlib as plt
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    correlation = Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return correlation
    

def answer_ten():
    Top15 = answer_one()
    median_value = np.median(Top15['% Renewable'])
    def ten(row):
        if row['% Renewable'] > median_value:
            row['HighRenew'] = 1
        else:
            row['HighRenew'] = 0
        return row
        
    answer_Series = Top15.apply(ten, axis=1)
    return answer_Series['HighRenew']
    

def answer_eleven():
    Top15 = answer_one()
    Top15['Estimate'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    
    merge_df = Top15.merge(pd.Series(ContinentDict).to_frame('Continent'), left_index = True, right_index = True)
    merge_df.rename(index={0:'Continent'},inplace=True)
    
    return merge_df.groupby('Continent')['Estimate'].agg({ 'size': 'size',
                           'sum':'sum',
                           'mean':'mean',
                           'std':'std'})
    

def answer_twelve():
    Top15 = answer_one()
    bin_df = pd.cut(Top15['% Renewable'],5).copy().to_frame('bins')
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    merge_df = bin_df.merge(pd.Series(ContinentDict).to_frame('Continent'), left_index = True, right_index = True)
    answer_df = merge_df.groupby(['Continent','bins']).size()
    return answer_df

def answer_thirteen():
    Top15 = answer_one()
    Top15['Estimate'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    PopEst = Top15['Estimate'].apply(lambda x : "{:,}".format(x))
    return PopEst

def plot_optional():
    import matplotlib as plt
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

print(answer_five())

import csv
import datetime as dt
import time as tm
import numpy as np
import pandas as pd


# read a csv file and convert into dictionary
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
                #print(mpg[0].keys())

# set a list for a type of dimension from the dictionary
cylinders = set(d['cyl'] for d in mpg)

# find average of a type of value from the dictionary
cylindermap = []
for c in cylinders:
    count = 0
    cylmpg = 0
    for d in mpg:
        if d['cyl'] == c:
            count += 1
            cylmpg += float(d['cty'])
    cylindermap.append([c, cylmpg/count])
cylindermap.sort(key=lambda x:x[0])
     
# create a mapping of models against classes of cars
vehicleClass = set(d['class'] for d in mpg)
vehicleMapping = []
for v in vehicleClass:
    models = []
    for d in mpg:
        if d['class'] == v:
            models.append(d['model'])
    vehicleMapping.append((v,set(models))) # set is used to pick only unique items from the list
    
                # print(vehicleClass)
                # print(vehicleMapping)

# date time and delta

                #print(tm.time())

                #print(dt.datetime.fromtimestamp(tm.time()).year)
timeDelta = dt.timedelta(days = 100)

#classes and objects
class Person:
    school = "Johnson"
    def set_Name(self, newName):
        self.name = newName
        

person_1 = Person()
person_1.set_Name("Anuj")
                #print(person_1.name, person_1.school)


#map

list_1 = [1,5,3,4]
list_2 = [4,2,13,8]

                #print(list(map(min, list_1, list_2)))

#string

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
                #print(people[0].split()[0])


#lambda

my_lambda = lambda person: person.split()[0] + ' ' + person.split()[-1]
                #print(my_lambda(people[0]))
                #print(list(map(my_lambda,people)))

#list comprehensions
comp_list = [number for number in range(1,10) if number % 2 == 0]
                #print(comp_list)


#numpy
array_1 = np.arange(36)
array_1.resize(6,6)
                #print(array_1[array_1 > 4])
                #array_1[array_1 > 4] = 5
                #print(array_1)

test_array = np.random.randint(0,18,[3,3])
#print(array_1)
#print(array_1[2:4,2:4])


#---------------------------------------------------
#week 2
#---------------------------------------------------

#panda series
series = pd.Series(comp_list)
                #print(series.index)
                #print(series.iloc[0])
                
                #print(np.sum(series))

#panda DataFrame
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
    
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Store1', 'Store1', 'Store2'])
#af = df.transpose()
                #print(df.loc['Store1']['Item Purchased'])
                #print(df['Item Purchased'])

#Slicing DataFrame to get particular columns
                
                #print(df.loc[:, ['Name', 'Cost']])

#drop row from a data frame
                #df.drop('Store2')

# appending colum to DataFrame
df['Location'] = None

                #print(df)

# appending row to the DataFrame
df.loc['Store3'] = ['Anuj', 'XBox', 300, None]
                #print(df)
df_temp = df['Cost'] * 0.8

                #print(df_temp)

#reading a csv

df_csv = pd.read_csv('olympics.csv', skiprows=1)
                #print(df_csv.head())

#rename columns in the data frame

for col in df_csv.columns:
    if col[:2] == '01':
        df_csv.rename(columns={col:'Gold'+col[4:]}, inplace = True)
    if col[:2] == '02':
        df_csv.rename(columns={col:'Silver'+col[4:]}, inplace = True)
    if col[:2] == '03':
        df_csv.rename(columns={col:'Bronze'+col[4:]}, inplace = True)
        
                    #print(df_csv.head())

#querying the data frame
                #print(df_csv.columns)               
only_gold = df_csv.where(df_csv['Gold'] > 0).dropna()
                #print(only_gold.count())

#setting a new index - set_index does not keep the current index, it has to be manually copied into a new column

                #df_csv['Country'] = df_csv.index
                #df_csv = df_csv.set_index('Gold')

#reset index - reset index promotes current index into a column and created default index
                #df_csv.reset_index()

#boolean masking
mask_output = df_csv[(df_csv['Gold'] == 0) & (df_csv['Gold.1'] > 0)]
                #print(mask_output)



census_csv = pd.read_csv('census.csv')
census_csv = census_csv[census_csv['SUMLEV'] == 50]

census_csv = census_csv.set_index(['STNAME','CTYNAME'])
                #print(census_csv.head())

#heirarchical indeces should be provided in the order of heirarchy
                #print(census_csv.loc['Alabama', 'Baldwin County'])

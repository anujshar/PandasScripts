# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 07:46:46 2019

@author: anujs
"""

import pandas as pd
import numpy as np

#binomial distribution
                #print(np.random.binomial(1000,0.5)/1000)

#running simulation 1000 times 
count = 0
for i in range(1000):
    if np.random.binomial(20,0.5) < 15:
        count += 1

                #print(count)

#running simulation 1000 times alternate version
x = np.random.binomial(20, .5, 10000)
                #print((x>=15).mean())
                
#chance of a tornado
chance_of_tornado = 0.01
                #print(np.random.binomial(100000, chance_of_tornado))

#chance of tornado two days in a row

tornado_events = np.random.binomial(1, chance_of_tornado,1000000)
days_tornado = 0

for i in range(1, len(tornado_events)-1):
    if tornado_events[i] == 1 and tornado_events[i-1] ==1:
        days_tornado += 1
        
print(days_tornado)

# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:43:22 2019

@author: anujs
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.image as mpimg
import numpy as np
import pandas as pd

#plot a chat using pyplot
                #plt.plot(3,2, 'x')
                

#plotting by interfacing with the Artist layer
fig = Figure()
canvas = FigureCanvasAgg(fig)
ax = fig.add_subplot(111)
ax.plot(3,2,'.')
canvas.print_png('test.png')
img = mpimg.imread('test.png')
                #plt.imshow(img)
                
#setting axes of a chart
                
                #plt.figure()
                #plt.plot(3,2,'x')
                #ax = plt.gca()
                #ax.axis([0,6,0,10])

#scatterplots
x = np.array([1,2,3,4,5,6])
y = x
                #plt.scatter(x,y, s = 100, c=['green', 'red'])

#zip generator - used to manipulate data into touples (useful for charts)
zip_generator = zip([1,2,3,4,5], [6,7,8,9,10])
                #print(list(zip_generator))

# different series on a scatter plot; adding labels, titles, legends
def plot_scatter():
    plt.scatter(x[:2],y[:2], s = 100, c= ['green'], label = "Tall students")
    plt.scatter(x[2:],y[2:], s = 100, c= ['blue'], label = "Short students")
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Chart title')
    plt.legend()
    
                #plot_scatter()
#line charts
                
def plot_line_chart():
    z = y**2
    plt.plot(x, '-o', z, '-o') # it uses the index of the series as the x value; we only gave y values as inputs
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Char title')
    plt.legend(['1', '2'])
    plt.gca().fill_between(range(len(z)), x, z, facecolor='green')
    
                #plot_line_chart()

def plot_line_chart_dates():
    z = y**2
    plt.figure()
    observation_dates = np.arange(np.datetime64('2017-01-01'), np.datetime64('2017-01-07'))
    observation_dates = (list)(map(pd.to_datetime, observation_dates))
    plt.plot(observation_dates, x, '-o', observation_dates, z, '-o')
    xticks = plt.gca().xaxis
    for item in xticks.get_ticklabels():
        item.set_rotation(45)

plot_line_chart_dates()
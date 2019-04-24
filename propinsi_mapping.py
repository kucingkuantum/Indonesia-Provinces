# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:18:49 2019

@author: syahr
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap

file = 'propinsi.xlsx'
df = pd.read_excel(file)
    
    # A basic map
m=Basemap(llcrnrlon=80, llcrnrlat=-15,urcrnrlon=160,urcrnrlat=20)

m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
m.drawcoastlines(linewidth=0.1, color="black")
 
# Add a marker per city of the data frame!
m.plot(df['Long'], df['Lat'], linestyle='none', marker="o", markersize=7, alpha=0.6, c="red", markeredgecolor="black", markeredgewidth=1)
plt.show()
# -*- coding: utf-8 -*-
"""Lab3<suhay.9>.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TmK4d6crdbVh4A9vz3ZxEhw-vrJMWzGy
"""

#
# (C) Authors: 
#
# (1)-(2) Professor Jian Chen
# (3)-(8): Rui Li
#
# 2022 Spring: For The Ohio State University, Intro. Data. Vis Lectures
# 
# import libraries
# Click the arrow in the upper left corner. You will get the line like this
# "Go to the following link in your browser" following by a blue link or a weblink.
# click that link, choose your google account to authorize, and accept to obtain
# an access code. Use the icon (like two squares) to copy the code and paste to the 
#  "Enter verification code:" - AND hit character return (from your keyboard)
# 
import pandas as pd
import random
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import altair as alt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('svg')

from matplotlib.lines import Line2D

import math
import re

# Import the library, authenticate, and create the interface to Sheets.
# https://colab.research.google.com/notebooks/io.ipynb?hl=en#scrollTo=sOm9PFrT8mGG
from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())

# access the google sheet and load it into pandas dataframe
#################### Do this only at the first time
wkbook = 'https://docs.google.com/spreadsheets/d/1HiVAuTr1miXHKCmxRDu_ZspUXttlRINN3ec2CvFHg1k/edit?usp=sharing'

wb = gc.open_by_url(wkbook)
sheet = wb.worksheet('Sheet1')
sheet_data = sheet.get_all_values()

df_data = pd.DataFrame(sheet_data)
# make row 0 into the column headers, then drop it
df_data.columns = df_data.iloc[0]
df_data.drop(df_data.index[0], inplace=True)

# heatmap chart
# x: year (categorical data)
# y: country (categorical data)
# color: emissions (quantitative data)
data = df_data.drop(columns=['Non-OECD Economies'])
data = data.set_index('Country\year')
data = data.apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(16, 7), dpi = 50)
ax = sns.heatmap(data.T, linewidths=.5, cmap='rainbow')

ax.set_xlabel('country')
ylabel = ax.set_ylabel('year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
yaxis = plt.yticks(fontsize=8)
title = ax.set_title('The heatmap to show the emissions of countries among years')

# heatmap chart
# x: year (categorical data)
# y: country (categorical data)
# color: emissions (quantitative data)
data = df_data.drop(columns=['Non-OECD Economies'])
data = data.set_index('Country\year')
data = data.apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(16, 7), dpi = 50)
ax = sns.heatmap(data.T, linewidths=.5, cmap='inferno')

ax.set_xlabel('country')
ylabel = ax.set_ylabel('year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
yaxis = plt.yticks(fontsize=8)
title = ax.set_title('The heatmap to show the emissions of countries among years')

chart_data = df_data.drop(columns=['Non-OECD Economies'])
chart_data = pd.melt(chart_data, id_vars=['Country\year'], var_name='year')
chart_data['value'] = chart_data['value'].apply(pd.to_numeric, errors='coerce')
chart_data.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)
chart_data

#render using altair
heatmap = alt.Chart(chart_data, title = 'Interactive Heat Map of Each Country By Year Using Extended Blackbody').mark_rect().encode(
    x=alt.X('country:N', title = 'country'),
    y=alt.Y('year:O', title = 'year'),
    color=alt.Color('emission:Q',scale=alt.Scale(scheme='inferno')),
    tooltip=['country', 'year', 'emission']
)
heatmap

#render using altair
heatmap = alt.Chart(chart_data, title = 'Interactive Heat Map of Each Country by Year Using Rainbow').mark_rect().encode(
    x=alt.X('country:N', title = 'Country'),
    y=alt.Y('year:O', title = 'Year'),
    color=alt.Color('emission:Q',scale=alt.Scale(scheme='rainbow')),
    tooltip=['country', 'year', 'emission']
)
heatmap

"""I believe that the extended blackbody color scheme makes for the better color map when compared to the rainbow color scheme. This is due to the blackbody starting with low values as black which gives whoever is looking at the visualization a basis point. When viewing the rainbow color scheme it is difficult to visualize which color represents low emission values and which shows the highest emissions. However, the blackbody shows a baseline of black and works it's way up to brighter color as the values get larger. """

# heatmap chart
# x: year (categorical data)
# y: country (categorical data)
# color: emissions (quantitative data)
data = df_data.drop(columns=['Non-OECD Economies'])
data = data.set_index('Country\year')
data = data.apply(pd.to_numeric, errors='coerce')
data.T['United States'] = np.log(data.T['United States'])
data.T['OECD - Total'] = np.log(data.T['OECD - Total'])
fig, ax = plt.subplots(figsize=(16, 7), dpi = 100)
ax = sns.heatmap(data.T, linewidths=.5, cmap="inferno")

ax.set_xlabel('country')
ylabel = ax.set_ylabel('year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
yaxis = plt.yticks(fontsize=8)
title = ax.set_title('The heatmap to show the emissions of countries among years')

# heatmap chart
# x: year (categorical data)
# y: country (categorical data)
# color: emissions (quantitative data)
data = df_data.drop(columns=['Non-OECD Economies'])
data = data.set_index('Country\year')
data = data.apply(pd.to_numeric, errors='coerce')
data3 = data.T.drop(columns=['OECD - Total', 'OECD - Europe', 'OECD America', 'European Union (28 countries)'])
fig, ax = plt.subplots(figsize=(16, 7), dpi = 100)
ax = sns.heatmap(data3, linewidths=.5, cmap="inferno")

ax.set_xlabel('country')
ylabel = ax.set_ylabel('year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
yaxis = plt.yticks(fontsize=8)
title = ax.set_title('The heatmap to show the emissions of countries among years')

"""This heatmap removes any input that consisted of a summation of countries (i.e. OECD Total, European Union, etc.) and only looks at countries individually. This allows whoever is looking at the visualization to gain a sense of which countries alone have the highest emissions. From this perspective it can be seen that the United States has much higher emissions than almost all of the other countries. The heatmaps showing all of the data could be an example of Perspective 2 as the summed inputs could be seen as outliers or misleading to the actual data as the range of color and magnitude for the United States with and without the totals is different. """
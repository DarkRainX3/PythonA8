# In this assignment, you are going to work on one of the Kaggle contests for data analysts, and you actually have
# the chance to really participate in the contest and win couple of grands !
#
# __The challenge objective__: Tell a data story about a subset of the data science community represented in this
# survey, through a combination of both narrative text and data exploration. A “story” could be defined any number
# of ways, and that’s deliberate. The challenge is to deeply explore (through data) the impact, priorities, or
# concerns of a specific group of data science and machine learning practitioners. That group can be defined
# in the macro (for example: anyone who does most of their coding in Python) or the micro (for example: female
# data science students studying machine learning in masters programs). This is an opportunity to be creative
# and tell the story of a community you identify with or are passionate about!
#
# Check Out the Kaggle page for this contest:
# https://www.kaggle.com/kaggle/kaggle-survey-2018/home?utm_medium=email&utm_source=intercom&utm_campaign=dsml-survey2018
#
# In this assignemnt, we ask you for several analyzes using data visualizations, and then you
# have the chance to improve it and make a nice story and submit it to Kaggle before the deadlines.
#
# __ note :__ You can use any visualization libraries in python for the following Figures.
#
# To start your story, reproduce the following 3 figures:

# As a first step, read the survey data from " multipleChoiceResponses.csv " and load it to a
# pandas dataframe. To observe the distribution of participants, plot the number of participants
# from different countries. Also to see which countries have the youngest developers, plot the
# participant in age range of [18-21],[22-24],[25-29] and show all the four bars for each country.

# Add your story here:
# Try to analyze your figure and start the narrative.
#
# You're Story : ....
# see fig1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('multipleChoiceResponses.csv', header=None, skiprows=[0,1], usecols=[3,4])
sums = dict()
fig, ax = plt.subplots()
countries=list()
for index,row in data.iterrows():
    if sums.get(row[4],None)==None:
        sums[row[4]]=dict()
    if sums[row[4]].get(row[3],None) != None:
        sums[row[4]][row[3]]=sums[row[4]].get(row[3],0)+1
    if sums[row[4]].get(row[3],None) == None:
        sums[row[4]][row[3]]=sums[row[4]].get(row[3],0)+1
for country in sums.keys():
    countries.append(country)
countries.sort()
ax.set_ylabel('Number of Developers')
ax.set_xlabel('Countries')
ax.set_title('Fig1. Number of developers in each country')
barw=0.2
age1821 = list()
age2224 = list()
age2529 = list()
allage = list()
index = np.arange(len(countries))
for i in countries:
    age1821.append(sums[i]['18-21'])
    age2224.append(sums[i]['22-24'])
    age2529.append(sums[i]['25-29'])
    allage.append(sum(sums[i].values()))
rects1 = ax.bar(index, allage, barw, color='orange', label='AllDevelopers')
rects2 = ax.bar(index+barw, age1821, barw, color='blue', label='Age 18-21')
rects3 = ax.bar(index+barw+barw, age2224, barw, color='purple', label='Age 22-24')
rects4 = ax.bar(index+(3*barw), age2529, barw, color='gray', label='Age 25-29')
ax.legend()
ax.set_xticks(index + 3*barw / 2)
ax.set_xticklabels(countries)
plt.xticks(rotation=90)
plt.style.use('seaborn-darkgrid')
plt.rcParams['figure.figsize']=(20,20)
fig.tight_layout()
ax.margins(x=0)
ax.annotate('Most of the young participants are from India', xy=(22.2, 1100), xytext=(25, 1100), arrowprops=dict(facecolor='black', shrink=0.05),)
ax.annotate('Most of participants are from USA', xy=(56, 4500), xytext=(40, 4500), arrowprops=dict(facecolor='black', shrink=0.05),)
plt.show()
#print(age1821)

#print(data[3])
#multipleChoiceResponses


# Fig2 (30pts)
# In this step, you're going to study the corelation between experience and income of people.
# So reproduce the following scatter plot in which the circles show each group of people and
# the size of the circle shows the number of participants in that group.
#
# Continue the Story:
# Analyze Fig2 and give more insight about the dataset.
#
# __rest of the story __ : ....
#
# Note:
# try to reproduce the same following figure. Side bar, Labels, and Title has points.
# see fig 2

# Fig3 (40 pts)
# In this part, you should plot two pie charts in the same window. The first chart shows
# the undergraduate major of the participants. You need to slice the biggest group in the pie chart.
#
# In the second pie chart, we want to see how many users use AWS, GCP and Azure among all
# other cloud computing services. So reproduce the pie chart that shows the usage percentage
# of these three, among all other (make sure to consider the participants who do not use any
# cloud providers too).
#
# Continue the Story:
# Analyze Fig3, 4 and give more insights about the dataset.
#
# __rest of the story __ : ....
#
# Note:
# Try to reproduce the same following figures. Labels and Title, picking good visible
# colors and font size, showing the percentage, Title and showing the two figures in
# the same window have all points.
# see fig3

# %matplotlib inline
# plt.style.use('seaborn-whitegrid')
# fig = plt.figure()
# ax = plt.axes()

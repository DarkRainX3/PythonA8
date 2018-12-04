import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datafirst = pd.read_csv('multipleChoiceResponses.csv', header=None, skiprows=[0, 1], usecols=[6])
datasec = pd.read_csv('multipleChoiceResponses.csv', header=None, skiprows=[0, 1], usecols=[57, 58, 59, 60, 61, 62, 63, 64])
datasec
majors = dict()
webserv = dict()
maj = list()
numbers = list()
for index, row in datasec.iterrows():
    if pd.isna(row[62]) == False:
        webserv['I have not used any cloud providers'] = webserv.get('I have not used any cloud providers', 0)+1
        continue
    listofservices = ''
    if pd.isna(row[57]) == False:
        listofservices += row[57]+', '
    if pd.isna(row[58]) == False:
        listofservices += row[58]+', '
    if pd.isna(row[59]) == False:
        listofservices += row[59]+', '
    # if pd.isna(row[63]) == False:  # or pd.isna(row[60])==False or pd.isna(row[61])==False:# or row[64]!=-1:
    #     webserv['Other'] = webserv.get("Other", 0)+1
    if len(listofservices) < 1:
        webserv['Other'] = webserv.get("Other", 0)+1
        continue
    listofservices = listofservices[:-2]
    webserv[listofservices] = webserv.get(listofservices, 0)+1
webserv
labels2 = list()
size2 = list()
for i in webserv.keys():
    labels2.append(i)
for i in labels2:
    size2.append(webserv[i])
for index, row in datafirst.iterrows():
    if pd.isna(row[6]):
        continue
    majors[row[6]] = majors.get(row[6], 0)+1
for i in majors.keys():
    maj.append(i)
for i in maj:
    numbers.append(majors[i])
labels = maj
sizes = numbers

explode = (0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
explode2 = (0, 0.1, 0, 0, 0, 0, 0, 0, 0)

font = {'family': 'normal',
        'weight': 'bold',
        'size': 12}

plt.rc('font', **font)
fig1, (ax1, ax2) = plt.subplots(2, 1)
plt.rcParams['figure.facecolor'] = 'black'
ax1.patch.set_facecolor('black')
ax2.patch.set_facecolor('black')
a, b, texts = ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', textprops=dict(color="white"), shadow=True, startangle=50)
for i in texts:
    i.set_color('blue')
a, b, texts = ax2.pie(size2, explode=explode2, labels=labels2, autopct='%1.1f%%', textprops=dict(color="white"), shadow=True, startangle=-40)
for i in texts:
    i.set_color('blue')
ax1.axis('equal')
ax1.set_title('Fig3. Undergraduate Majors of Participants', y=-0.1, color='w')
ax2.set_title('Fig4. Cloud Computing Services in Use', y=-0.1, color='w')
plt.tight_layout()
plt.rcParams['figure.figsize'] = (20, 15)
plt.show()

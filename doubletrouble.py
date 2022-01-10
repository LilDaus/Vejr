import numpy as np
import matplotlib.pyplot as plt

import csv

x = []
temp=[]
vind=[]
today=[]
d = 0

with open('DK.csv') as File:
    plots = csv.reader(File)
    next(plots)

    for row in plots:
        today.append(float(row[1]))
        d += 1
        if d ==24:
            temp.append(sum(today)/24.0)
            x.append(row[0][0:10])
            today=[]
            d = 0
with open('Vind.csv') as File:
    plots = csv.reader(File)
    next(plots)

    for row in plots:
        today.append(float(row[1]))
        d += 1
        if d ==24:
            vind.append(sum(today)/24.0)
            #x.append(row[0][0:10])
            today=[]
            d = 0


fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('date)')
ax1.set_ylabel('Tepratur[°C]', color=color)
ax1.plot(x, temp, color=color)
ax1.tick_params(axis='y', labelcolor=color)
xticks = plt.xticks(rotation=45, fontsize=5)
plt.title('TOTALT SEJT DATA')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Vind[M/s]', color=color)  # we already handled the x-label with ax1
ax2.plot(x, vind, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
every_nth = 7
for n, label in enumerate(xticks[1]):
    if n % every_nth != 0:
        label.set_visible(False)


plt.show()

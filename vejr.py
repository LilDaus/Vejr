import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook



import numpy as np
import pandas as pd
import csv

x = []
y = []

with open('DK.csv') as File:
    plots = csv.reader(File)
    next(plots)

    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

print(f"done loading data: {len(x)} datapoints")

plt.plot(x, y, color='g', label="Temp")
plt.xlabel('Date')
plt.ylabel('Temp')
plt.title('Temp Data')
plt.legend()
plt.show()
print("done")


import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook



import csv

today = []
x = []
y = []
d = 0
figure, ax = plt.subplots(2, 1,sharex='all') #laver et secondary subplot med 2 i højden og 1 i bredden.

with open('DK.csv') as File:
    plots = csv.reader(File)
    next(plots)

    for row in plots:
        today.append(float(row[1]))
        d += 1
        if d ==24:
            y.append(sum(today)/24.0)
            x.append(row[0][0:10])
            today=[]
            d = 0
    ax[0].plot(x, y, color='r', label="Temp per day [Cº]") #giver "ax[0]/det øverste plots data en defination og farve"
    xticks = plt.xticks(rotation=45, fontsize=5) #sætter skriftstørrelse og grader på datoerne
    ax[0].legend()


today = []
x = []
z = []
d = 0

with open('Vind.csv') as File:
    plots = csv.reader(File)
    next(plots)

    for row in plots:
        today.append(float(row[1]))
        d += 1
        if d ==24:
            z.append(sum(today)/24.0)
            x.append(row[0][0:10])
            today=[]
            d = 0

    ax[1].plot(x, z, color='g', label="Wind speed [M/s]") #giver "ax[1]/det nederste plots data en defination og farve"
    ax[1].legend()




every_nth = 7
for n, label in enumerate(xticks[1]):
    if n % every_nth != 0:
        label.set_visible(False)

plt.show()
print("done")

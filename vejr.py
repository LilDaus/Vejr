import matplotlib.pyplot as plt
#import matplotlib.cbook as cbook



import csv

today = []
x = []
y = []
d = 0
figure, axis = plt.subplots(2, 1)

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
    plt.plot(x, y, color='r', label="Temp per day")
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title('TOTALT SEJT DATA')
    xticks = plt.xticks(rotation=45, fontsize=5)
    # plt.grid()
    plt.legend()


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

    plt.plot(x, z, color='g', label="Wind speed")
    plt.xlabel('Date')
    plt.ylabel('[M/S]')
    plt.title('TOTALT SEJT DATA')
    xticks = plt.xticks(rotation=45, fontsize=5)
    plt.legend()




every_nth = 7
for n, label in enumerate(xticks[1]):
    if n % every_nth != 0:
        label.set_visible(False)

plt.show()
print("done")

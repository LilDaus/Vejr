import matplotlib.pyplot as plt

import csv

x = []
temp=[]
vind=[]
today=[]
#giver de forskellige variabler en liste
d = 0

with open('DK.csv') as File: #åbner filen for at procces den
    plots = csv.reader(File)
    next(plots) #skipper headeren i csv filen

    for row in plots:
        today.append(float(row[1]))
        d += 1
        if d ==24:
            temp.append(sum(today)/24.0)#da der er mange data (8000), gør jeg så den definerer gennemsnittet af hver dag.
            x.append(row[0][0:10]) # da der også er mange dage sætter jeg den så den kun viser hver 7 dag.
            today=[] #resetter "today" til 0 så loopet kan køre igen
            d = 0#resetter "d" til 0 så loopet kan køre igeg
with open('Vind.csv') as File:
    plots = csv.reader(File)
    next(plots)

    for row in plots:
        today.append(float(row[1]))
        d += 1
        if d ==24:
            vind.append(sum(today)/24.0)
            today=[]
            d = 0


fig, ax1 = plt.subplots()

color = 'tab:red' # definerer farven af den ene Y akse
ax1.set_xlabel('date)') # sætter label på X aksen
ax1.set_ylabel('Tepratur[°C]', color=color) # sætter et label på venstre Y akse
ax1.plot(x, temp, color=color) # giver plottet hvad den skal bruge for at show
ax1.tick_params(axis='y', labelcolor=color) # giver venstre Y aksen hvad den skal bruge for at vise dataen
xticks = plt.xticks(rotation=45, fontsize=5) # sætter rotationen og skriftstørrelse på datoerne der vises på X aksen
plt.title('TOTALT SEJT DATA') #giver hele plottet en titel

ax2 = ax1.twinx()  #initierer den anden Y akse med samme X akse

color = 'tab:blue'
ax2.set_ylabel('Vind[M/s]', color=color)
ax2.plot(x, vind, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
every_nth = 7 #sætter hver dato som 7 så den kun viser hver uge, men stadig viser hver dag i dataen
for n, label in enumerate(xticks[1]):
    if n % every_nth != 0:
        label.set_visible(False)


plt.show()

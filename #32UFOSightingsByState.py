#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 11, 2021
#This program is about UFO sightings

import matplotlib.pyplot as plt
import pandas as pd

sea = input("Enter name of input file: ")
weed = input("Enter name of output file: ")

face = pd.read_csv(sea)
book = face.groupby("state")
mark = book["duration (seconds)"].mean()
zucc = mark.sort_values(ascending = False)[:10]
tesla = zucc.plot.bar()
plt.xlabel('State')
plt.ylabel('Seconds')
plt.gcf().savefig(weed)




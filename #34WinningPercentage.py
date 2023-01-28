#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 14, 2021
#This program shows winning percentage

import matplotlib.pyplot as plt
import pandas as pd

hater = input("Enter name of input file: ")
simp = input("Enter name of output file: ")
linkedin = pd.read_csv(hater)
linkedin["Date"] = pd.to_datetime(linkedin["Date"].apply(str))
CEO = linkedin["Winner Pts"] + linkedin["Loser Pts"]
linkedin["% Points"] = (100 * linkedin["Winner Pts"])/(CEO)
linkedin.plot(x = "Date", y = "% Points")
plt.gcf().savefig(simp)
plt.show()



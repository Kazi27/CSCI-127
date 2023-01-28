#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 10, 2021
#This program is gives shelter census

import pandas as pd
import matplotlib.pyplot as plt

dusty = input("Enter name of input file: ")
crossaint = input("Enter name of output file: ")

ray = pd.read_csv(dusty)
ray["Fraction Single Adults"] = ray["Total Single Adults in Shelter"]/ray["Total Individuals in Shelter"]
ray.plot(x = "Date of Census", y = "Fraction Single Adults")
plt.gcf().savefig(crossaint)
plt.show()

#cism = plt.gcf()
#cism.savefig(crossaint)

#homeless = pd.read_csv("DHS_Daily_Report.csv")
#homeless["Fraction Single Adults"] = homeless["Total Single Adults in Shelter"]/homeless["Total Individuals in Shelter"]
#homeless.plot(x = "Date of Census", y = "Fraction Single Adults")
#plt.show()

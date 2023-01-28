#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 19, 2021
#This program video games

import matplotlib.pyplot as plt
import pandas as pd

sleep = input("Enter file name: ")
deprived = pd.read_csv(sleep)
number = deprived["Rank"].count()
print("There are ", number, "total games")
print(deprived["Genre"].value_counts())
print("The top 3 game publishers are")
print(deprived["Publisher"].value_counts()[:3])



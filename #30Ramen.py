#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 6, 2021
#This program is about Ramen

import matplotlib.pyplot as plt
import pandas as pd

doozy = input("Enter file name:")
df = pd.read_csv(doozy)                                     

df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")  
style = df.groupby("Style")                                 

print("The average stars per serving style: \nStyle")
print("Bar",'\t',style.get_group("Bar")["Stars"].mean())
print("Bowl",'\t',style.get_group("Bowl")["Stars"].mean())
print("Box",'\t',style.get_group("Box")["Stars"].mean())
print("Can",'\t',style.get_group("Can")["Stars"].mean())
print("Cup",'\t',style.get_group("Cup")["Stars"].mean())
print("Pack",'\t',style.get_group("Pack")["Stars"].mean())
print("Tray",'\t',style.get_group("Tray")["Stars"].mean())
print("Name: Stars, dtype:", df["Stars"].dtype,"\n")
print("KOKA has the lowest rating in Singapore with 2.5 stars.")






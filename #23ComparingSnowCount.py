#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 30, 2021
#This program counts difference in snow amount

import matplotlib.pyplot as plt
import numpy as np

image1 = input("Enter first image file name: ")
image2 = input("Enter second image file name: ")
t = float(input("Enter threshold of white pixels: "))

ca = plt.imread(image1)
countSnow = 0               

for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1
countSnowOne = countSnow
print("Snow count of first image: ", countSnowOne)

cali = plt.imread(image2)
countSnow = 0

for i in range(cali.shape[0]):
     for j in range(cali.shape[1]):
          if (cali[i,j,0] > t) and (cali[i,j,1] > t) and (cali[i,j,2] > t):
               countSnow = countSnow + 1
countSnowTwo = countSnow          
print("Snow count of second image: ", countSnowTwo)

difference = countSnowOne - countSnowTwo
print("Difference between first and second image: ", abs(difference))




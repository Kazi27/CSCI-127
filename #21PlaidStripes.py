#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: August 28, 2021
#This program makes plaid stripes


import numpy as np
import matplotlib.pyplot as plt

gridsize = int(input("Enter the size: "))
filename = input("Enter output file: ")

cry = np.ones((gridsize,gridsize,3))
cry[:gridsize,:,0]=1
cry[range(gridsize),:,1]=1
cry[range(gridsize),:,2]=1

for row in range(1,gridsize,2):
    for col in range(gridsize):
        cry[row,col,0] = 240/256
        cry[row,col,1] = 230/256
        cry[row,col,2] = 0.5490196347236633

for col in range(1,gridsize,2):
    for row in range(gridsize):
        cry[row,col,0] = 0.729411780834198
        cry[row,col,1] = 143/256
        cry[row,col,2] = 143/256
    

#plt.imshow(cry)
#plt.show()
plt.imsave(filename, cry)

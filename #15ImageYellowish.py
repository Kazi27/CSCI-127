#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 15, 2021
#This program yellows your image

import matplotlib.pyplot as plt
import numpy as np

imposter = input("Enter name of the input file: ")
syndrome = plt.imread(imposter)

aston = syndrome.copy()
aston[:,:,2] = 0
#plt.imshow(aston)
#plt.show()

martin = input("Enter name of the output file: ")
plt.imsave(martin,aston)

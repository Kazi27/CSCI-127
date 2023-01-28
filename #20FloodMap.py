#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 23, 2021
#This program makes a flood map

import numpy as np                           #imports the library for arrays
import matplotlib.pyplot as plt              #imports the library for displaying images

elevations = np.loadtxt('elevationsNYC.txt') #reads in the data to an array called elevations

mapShape = elevations.shape + (3,)           #so like this takes the txt file and adds 3 color channels (RGB)

floodMap = np.zeros(mapShape)                #this creates a blank image that's all zeros

                                             #initiates nested forloop, for all rows and all columns
for row in range(mapShape[0]):               #(wtf does [0] mean)
    for col in range(mapShape[1]):           #(wtf does [1] mean)
        if elevations[row,col] <= 0:         #below sea level
           floodMap[row,col,0] = 1.0         #sets the red channel to 100%
           floodMap[row,col,1] = 1.0         #sets the green channel to 100%
                                             #red & green at 100% makes yellow

        elif elevations[row,col] <= 5:       #below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0         #set the red channel to 100%
                                             #colors it red ofc

        elif elevations[row,col] > 5 and elevations[row,col] <= 20:
            floodMap[row,col,0] = 0.5        #sets the red channel to 50%
            floodMap[row,col,1] = 0.5        #sets the green channel to 50%
            floodMap[row,col,2] = 0.5        #sets the blue channel to 50%
                                             #all values same number so this is gray        

        else:                                #above the 6 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0        #sets the green channel to 100%
                                             #colors it green ofc

#plt.imshow(floodMap)                        #loads the flood map image into matplotlib.pyplot
#plt.show()                                  #displays the image
plt.imsave('floodMap.png', floodMap)         #saves the image

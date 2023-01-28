#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 19, 2021
#This program makes a pink P

import matplotlib.pyplot as plt
import numpy as np

time = np.zeros((30, 30, 3))    #makes an array
for i in range(6):              #makes an forloop that iterates 6 times
    time[i,:,0] = 1             #subs in 1 thru 6 in ROW, RED 100% 
    time[i,:,2] = 1             #subs in 1 thru 6 in ROW, BLUE 100%
    time[:,i,0] = 1             #subs in 1 thru 6 in COLUMN, RED 100%
    time[:,i,2] = 1             #subs in 1 thru 6 in COLUMN, BLUE 100%

for i in range(18):             #makes a for loop that iterates 18 times
    for j in range(25,30):      #makes a for loop that starts at 25, ends at 30
        time[i,j,0] = 1         #subs in those values, RED 100%
        time[i,j,2] = 1         #subs in those values, BLUE 100%

for i in range(15,21):          #makes a for loop that starts at 25, ends at 30
    time[i,:,0] = 1             #subs in those values, RED 100%
    time[i,:,2] = 1             #subs in those values, BLUE 100%
#plt.imshow(time)
#plt.show()
plt.imsave("logo.png", time)

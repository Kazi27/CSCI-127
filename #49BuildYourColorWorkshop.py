#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: November 12, 2021
#This program builds your color

import matplotlib.pyplot as plt                                                                     #imports needed library
import numpy as np                                                                                  #imports needed library


def validation(num):                                                                                #defines a function named validation that takes in input num
    if 0 <= num <= 255:                                                                             #if num is between 0 and 255, 0 and 255 included
        return num                                                                                  #return num
    elif num < 0:                                                                                   #if num is negative
        return 0                                                                                    #just return 0
    else:                                                                                           #otherwise
        return 255                                                                                  #return 255


def main():                                                                                         #defines a function named main
    print(                                                                                          #prints introductory thing ONCE and never again, this is under main()
        """
------------------------------------------
Welcome to the Color Maker!
------------------------------------------
Please enter for each rbg color the value in which to increase/decrease them.
If all 3 values given are 0, the program will end and save the resulting image.
"""
    )


color = np.zeros((10, 10, 3))                                                                       #makes a canvas that starts off as black cause np.zeros and has 10 rows 10 columns 3 color channels
red = 0                                                                                             #original values for variable red
green = 0                                                                                           #original values for variable green
blue = 0                                                                                            #original values for variable blue

suffering = input("Enter outfile name: ")                                                           #file will be saved under this name
changered = int(input("How much do you want to change the red value by? \n"))                       #how much u wanna change red by (also \n means new line)
changegreen = int(input("How much do you want to change the green value by? \n"))                   #how much u wanna change green by (also \n means new line)
changeblue = int(input("How much do you want to change the blue value by? \n"))                     #how much u wanna change blue by (also \n means new line)

red = validation(red + changered)                                                                   #red is originally 0 and ur adding what the user changed red by then subbing it into validation
green = validation(green + changegreen)                                                             #green is originally 0 and ur adding what the user changed green by then subbing it into validation
blue = validation(blue + changeblue)                                                                #blue is originally 0 and ur adding what the user changed blue by then subbing it into validation

print("The current RGB values are: [", red / 255, ",", green / 255, ",", blue / 255,"]\n")          #now u have new red, green, blue values which u divide by 255 and print :)

while changered + changegreen + changeblue != 0:                                                    #as long as user doesnt change red AND green AND blue by 0, do this. Ifr red/green/blue = 0, skip this   

    changered = int(input("How much do you want to change the red value by? \n"))                   #explained all this above so yeah
    changegreen = int(input("How much do you want to change the green value by? \n"))               #explained all this above so yeah
    changeblue = int(input("How much do you want to change the blue value by? \n"))                 #explained all this above so yeah
    
    red = validation(red + changered)                                                               #yeah
    green = validation(green + changegreen)                                                         #yeah
    blue = validation(blue + changeblue)                                                            #yeah
    
    print("The current RGB values are: [", red / 255, ",", green / 255, ",", blue / 255,"]\n")      #yeah its all the same except its in a while loop this time so it repeats as long as RGB != 0
    
color[:,:,0] = red / 255                                                                            #so now ur seeting the red channel to what color user finalized on
color[:,:,1] = green / 255                                                                          #so now ur seeting the green channel to what color user finalized on
color[:,:,2] = blue / 255                                                                           #so now ur seeting the blue channel to what color user finalized on

plt.imsave(suffering, color)                                                                        #save color under the title the user chose

if __name__ == "__main__":
    main()

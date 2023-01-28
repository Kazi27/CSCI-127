#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 19, 2021
#This program makes a colorful turtle spiral

import turtle

batman = int(input("Enter number of stamps the turtle will print: "))
hydro = turtle.Turtle()
turtle.colormode(255)
hydro.shape("circle")
hydro.penup()
steps = 20                          #setting variables
red = 186
green = 164
blue = 145
hydro.color(red,green,blue)         #original color

for i in range(batman):             #number of stamps user inputed
    hydro.stamp()
    steps += 2                      #the variable steps increases by 2
    if ((red + 3 < 255) and (green + 3 < 255) and (blue + 3 < 255)):
        red += 3
        green += 3
        blue += 3
    hydro.color(red,green,blue)     #new color
    hydro.forward(steps)            #movement w 2 added to it repeatedly (range)
    hydro.right(24)

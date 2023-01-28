#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 26, 2021
#This program makes smth cool

import turtle                   #imports turtle library
turtle.colormode(255)           #sets colormode to specify color values
turtle.bgcolor("khaki")         #sets background to khaki for aesthetic purposes
chungus = turtle.Turtle()       #creates turtle named chungus
chungus.speed(0)                #optional, just makes it go faster
chungus.pensize(5)              #specifizes pensize

for i in range(36):             #first for loop statement
    chungus.pencolor(0,(i*7),0) #slowly gets greener cause RGB, red/blue const 0
    chungus.forward(10)         #turtle goes forward 10
    chungus.left(10)            #turtle turns left 10 this is what causes the lil
                                #deviation cause if not for this square would just
                                #pile up on each other
    
    for b in range(4):          #second nested for loop statement
        chungus.left(90)        #turtle turns left 90 degrees right angle
        chungus.forward(300)    #turtle goes forward 300
        chungus.backward(50)    #turtle goes backwards 50 to create the extra thing
                                #so really it goes 300, goes back 50 so at 250 rn
                                #then just turns turns 90 again, goes forward 300
                                #again and then bacup 50 to turn again at 250 and
                                #repeats that 4 times   

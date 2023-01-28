#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: August 28, 2021
#This program draws a rhombus flower

import turtle
wn = turtle.Screen()
wn.bgcolor("khaki")

kazi = turtle.Turtle()
kazi.shape("turtle")
kazi.pencolor("black")
kazi.pensize("3")
kazi.fillcolor("green")

for i in range(6):
    kazi.forward(100)   
    kazi.left(45)
    kazi.forward(100)
    kazi.left(135)
    kazi.stamp()
    kazi.forward(100)
    kazi.left(45)
    kazi.forward(100)
    kazi.right(135)
    kazi.right(30)

wn.exitonclick()

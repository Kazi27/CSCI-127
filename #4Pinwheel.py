#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: August 28, 2021
#This program draws a pinwheel

import turtle
wn = turtle.Screen()

alex = turtle.Turtle()
alex.shape("arrow")
alex.color("purple")
alex.pensize("3")
alex.forward(30)

for i in range(3):
    alex.forward(50)
    alex.right(120)

alex.backward(30)
alex.right(90)
alex.forward(30)

for i in range(3):
    alex.forward(50)
    alex.right(120)

alex.backward(30)
alex.right(90)
alex.forward(30)

for i in range(3):
    alex.forward(50)
    alex.right(120)

alex.backward(30)
alex.right(90)
alex.forward(30)

for i in range(3):
    alex.forward(50)
    alex.right(120)

alex.backward(30)

    
wn.exitonclick()

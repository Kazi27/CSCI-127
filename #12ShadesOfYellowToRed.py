#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: August 25, 2021
#This program shows yellow to red heart in different shade

import turtle				

turtle.colormode(255)		
tess = turtle.Turtle()		
tess.shape("turtle")
tess.penup()
tess.backward(100)
tess.pendown()

for i in range(0,255,10):
     tess.forward(10)		
     tess.pensize(i)
     tess.color(255,255-i,0)

tess.penup()
tess.pensize(0)
tess.color(0,0,0)
tess.backward(260)
tess.right(90)
tess.pendown()

for i in range(0,255,10):
     tess.forward(10)		
     tess.pensize(i)
     tess.color(255,255-i,0)



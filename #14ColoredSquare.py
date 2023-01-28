#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 04, 2021
#This program ?

anwar = input("Please enter a 6-digit Hexadecimal number:")

import turtle
kazi = turtle.Turtle()
kazi.shape("turtle")
kazi.color("#"+anwar)

for i in range(3):
    kazi.forward(100)
    kazi.stamp()
    kazi.left(90)
    
kazi.forward(100)
kazi.right(360)
kazi.stamp()

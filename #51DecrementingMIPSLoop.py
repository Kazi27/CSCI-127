#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: November 18, 2021
#This program is very hard

#Sample program that loops from 10 down to 0
ADDI $s0, $zero, 100 #set s0 to 100
ADDI $s1, $zero, 25  #use to decrement counter, $s0
AGAIN: SUB $s0, $s0, $s1
BEQ $s0, $zero, DONE
J AGAIN
DONE:  #To break out of the loop

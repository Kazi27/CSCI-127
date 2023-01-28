#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: August 31, 2021
#This program shifts characters in your input by 5

lebron = input('Enter a message:')  #prompts user to input message
for c in str(lebron):               #for every letter in input
    kd = (ord(c)+5)                 #turns letter to unicode and adds 5
    steph = (chr(kd))               #turns unicode back to letter
    print(c,"shifted by 5 characters is:",steph)#prints that 

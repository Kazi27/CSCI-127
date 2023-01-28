#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 07, 2021
#This program encrypts your message

iron = input("Enter a word: ")
man = ""
for c in iron:
    if ord(c) < 76:
        dunkin = (ord(c)+13)
        donuts = (chr(dunkin))
        man += donuts
        
    else:
        star = (ord(c)-13)
        bucks = (chr(star))
        man += bucks

print("Your word in code is", man)

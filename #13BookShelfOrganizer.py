#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 14, 2021
#This program organizes your books


new = input("Enter a list of books and their authors:")
york = new.split("; ") #this is a list/splits books & authors 
i = ""
for i in york:
    city = i.split(" - ") #printing city gives u a list/splits book and name
    for j in city:
        best = j.split(" ")#also produces a list/splits first & last name
    place = best[0]#first name
    yeah = place[0]#first letter of first name
    on = best[1] #last name
    yep = on[0]#first letter of last name
    earth = city[0] #name of book
    print(earth+" by "+yeah+"."+yep+".")

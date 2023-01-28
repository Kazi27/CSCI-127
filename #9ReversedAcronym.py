# Name: Kazi Sameen Anwar
# Email: kazisameen.anwar39@myhunter.cuny.edu
# Date: September 04, 2021
# This program creates a backwards acronym

CLB = input('Enter a phrase:')  # prompts user to input
Donda = (CLB[::-1])  # reverses input string
print("Reversed phrase: ", Donda)  # prints the reversed phrase
Drake = Donda.upper()  # makes reversed phrase caps
Kanye = Drake.split()  # splits reversed phrase into words
Drizzy = ""  # puts an empty value to make it defined
for Ye in Kanye:  # is ye a placeholder?like in "for i" loop etc?
    Drizzy = Drizzy + Ye[-1]  # for loop goes through strings chooses last
print("Last letter of reversed words:", Drizzy)  # prints last letter of each word together

#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 17, 2021
#This program converts

print("Please enter the conversion you want to do:")
print("'a' for Light-Year to Parsec conversion")
print("'b' for Parsec to Light-Year conversion")
amazon = input("Your selection: ")
a = ""
if amazon == "a":
    alexa = float(input("Please enter a number of Light-Years: "))
    google = 0.306601 *alexa
    print(alexa, "Light-Years is equal to ",google ,"Parsecs.")

if amazon == "b":
    siri = float(input("Please enter a number of Parsecs: "))
    apple = 3.26156 *siri
    print(siri, "Parsecs is equal to ",apple ,"Light-Years.")

#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: September 19, 2021
#This program determines how hype you are

popularity = int(input("Enter amount of social media followers: "))
if popularity < 0:
    print("Error")
if popularity < 1000 and popularity > 0:
    print("Hyper Influencer")
if popularity < 10000 and popularity > 1000:
    print("Nano Influencer")
if popularity < 100000 and popularity > 10000:
    print("Micro Influencer")
if popularity < 500000 and popularity > 100000:
    print("Mid-Tier Influencer")
if popularity < 1000000 and popularity > 500000:
    print("Macro Influencer")
if popularity > 1000000:
    print("Celebrity Influencer")


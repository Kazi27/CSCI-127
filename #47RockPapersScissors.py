#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 14, 2021
#This program shows winning percentage

import random

def main():
    playerMove = int(input("enter 1 for rock, 2 for paper, or 3 for scissors: "))
    ComputerMove = random.randrange(1,4)
    print("computerMove:", ComputerMove)
    logic(playerMove, ComputerMove)
    while playerMove > 0:
        main()

def logic(playerMove,ComputerMove):
    if (playerMove == 1) and (ComputerMove == 1):
        print("round finished and winner is: draw")
        #main()
    if (playerMove == 1) and (ComputerMove == 2):
        print("round finished and winner is: computer")
        #main()
    if (playerMove == 1) and (ComputerMove == 3):
        print("round finished and winner is: human")
        #main()
    if (playerMove == 2) and (ComputerMove == 1):
        print("round finished and winner is: human")
        #main()
    if (playerMove == 2) and (ComputerMove == 2):
        print("round finished and winner is: draw")
        #main()
    if (playerMove == 2) and (ComputerMove == 3):
        print("round finished and winner is: computer")
        #main()
    if (playerMove == 3) and (ComputerMove == 1):
        print("round finished and winner is: computer")
        #main()
    if (playerMove == 3) and (ComputerMove == 2):
        print("round finished and winner is: human")
        #main()
    if (playerMove == 3) and (ComputerMove == 3):
        print("round finished and winner is: draw")
        #main()
    if (playerMove <= 0) or (playerMove >3):
        print("invalid")
        
if __name__ == "__main__":
    main()


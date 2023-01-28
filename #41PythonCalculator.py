#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 14, 2021
#This program is a calculator

import math
  
#Function to add two numbers 
def add(num1, num2):
    add_nums = num1 + num2
    return add_nums

  
#Function to subtract two numbers 
def subtract(num1, num2):
    sub_nums = num1 - num2
    return sub_nums

  
#Function to multiply two numbers
def multiply(num1, num2):
    mul_nums = num1 * num2
    return mul_nums

  
#Function to divide two numbers
def divide(num1, num2):
    div_nums = num1 / num2
    return div_nums


#Function to get the square root of the number
def sqrt(num1):
    sqrt1 = math.sqrt(num1)
    return sqrt1


# Function to square a number
def squared(num1):
    square_num = num1 ** 2
    return square_num
   

#Function to get a number to the exponent of another number
def exponent(num1, num2):
    exp_nums = num1 ** num2
    return exp_nums




def main():
    """Asks the user for a number to select an operation and prompts them to
       to put in two numbers to do the calculation.
       Do not change the main function !
    """
    
    print("Please select operation -\n" \
          "1. Add\n" \
          "2. Subtract\n" \
          "3. Multiply\n" \
          "4. Divide\n" \
          "5. Square root\n" \
          "6. Squared\n" \
          "7. Exponent\n")

    # Take input from the user 
    select = int(input("Select operations from: 1, 2, 3, 4, 5, 6, 7 : "))
  
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
  
    if select == 1:
        print(number_1, "+", number_2, "=",
                        add(number_1, number_2))
  
    elif select == 2:
        print(number_1, "-", number_2, "=",
                        subtract(number_1, number_2))
  
    elif select == 3:
        print(number_1, "*", number_2, "=",
                        multiply(number_1, number_2))
  
    elif select == 4:
        print(number_1, "/", number_2, "=",
                        divide(number_1, number_2))

    elif select == 5:
        print("square root of", number_1, "is",
                        sqrt(number_1))
        print("square root of", number_2, "is",
                        sqrt(number_2))
    
    elif select == 6:
        print(number_1, "squared is",
                        squared(number_1))
        print(number_2, "squared is",
                        squared(number_2))        


    elif select == 7:
        print(number_1, "to the power of", number_2, "is",
                        exponent(number_1, number_2))
                        
                                
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()

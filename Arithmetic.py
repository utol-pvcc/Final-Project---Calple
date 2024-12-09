
import math

def sum(num1S,num2S):
    return(round(num1S + num2S, 6))

def rest(num1R, num2R):
    return(round(num1R - num2R, 6))

def mult(num1, num2):
    solve = num1 * num2
    return (round(solve, 6))

def divis(num1, num2):
    solve = float(num1) / float(num2)
    print (round(solve, 6))
    

def calculator():
    print("Standar Calculator")
    print("1) Sum\n2) Rest\n3) Multiplication\n4) Division")
    userInput = int(input("Whatcha gonna do? "))
    
    if userInput == 1:
        print("Suma : +")
        num1S = float(input('Enter 1st number: '))
        num2S = float(input('Enter 2nd number: '))
        print(f'    {num1S} + {num2S} = {sum(num1S,num2S)}')

    if userInput == 2:
        print("Resta: -")
        num1R = float(input('Enter 1st number: '))
        num2R = float(input('Enter 2nd number: '))
        print(f'    {num1R} - {num2R} = {rest(num1R,num2R)}')
    
    if userInput == 3:
        print("Multiplication: x ")
        num1 = float(input('Enter 1st number: '))
        num2 = float(input('Enter 2nd number: '))
        print(mult(num1, num2))
        
    if userInput == 4:
        print("Division: / ")
        divis(float(input("1st Number: ")), float(input("2dn Number: ")))
    else:
        print("Invalid data1231")
        

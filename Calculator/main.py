
from Geometry import Geometry
from Arithmetic import calculator
from Conversion import Units

def main():
    print("Tipo de calculadora")
    print("     1) Standar: +, -, *, /")
    print("     2) Geometry: Area and Perimeter and Pythagoras")
    print("     3) Conversion ")

    UserInput = int(input("Valor: "))
    
    if UserInput == 1:
        calculator()
    if UserInput == 2:
        Geometry()
    if UserInput == 3:
        Units()

    else:
        print("Invalid data")

main()
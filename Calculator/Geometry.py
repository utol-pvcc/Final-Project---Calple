
import math

def Figuras():
    print(" 1) Circulo")
    print(" 2) Cuadrado")
    print(" 3) Triangulo")
    print(" 4) Polygon")
    print(" 5) Rectangle")

def pitagoras():
    print(" 1) Find Hypotenuse")
    print(" 2) Find a Catet")
    

def AranPer(num1):
    if num1 == 1:
        print("Area and Perimeter of the circle")
        print(" A = πr^2,   P = 2πr")
        R = float(input("Give me a Radio: "))

        #Area
        Solve = pow(R, 2) * math.pi
        print(str("Area: ") + str(round(Solve, 4)))

        #Perimeter
        solve = 2*R* math.pi
        print(str("Perimeter: ") + str(round(solve, 4))) 
    
    if num1 == 2:
        print("Area and Perimeter of the Square")
        print(" A = S^2,    P = 4xS")
        S = float(input("Give me one side of the Square: "))

        # Area
        Solve = pow(S,2)
        print(str("Area: ") + str(round(Solve,4)))

        #Perimeter     
        Solve = 4*S
        print(str("Perimeter: ") + str(round(Solve, 6)))

    if num1 == 3:
        print("Area and Perimeter of the Triangle")
        print(" A = Using Heron's formula,  P = A + B + C ")
        A = float(input("Give me side A: "))
        B = float(input("Give me side B: "))
        C = float(input("Give me side C: "))

        #Perimeter
        Solve = A + B + C
        print(str("Perimeter: ") + str(round(Solve, 6)))

        #Area
        s = (A + B + C)/2
        Solve = s*(s-A)*(s-B)*(s-C)
        root = math.sqrt(Solve)
        print(str("Area: ") + str(round(root, 2)))
    
    if num1 == 4:
        print("Area and Perimeter of the Polygon ")
        print(" A = (Perimeter*Apothem)/2,   P = N(#sides)*Lengh of one N")

        N = float(input("How many sides: "))
        L = float(input("Length of one side: "))

        #Perimeter
        P = N*L
        print(str("Perimeter: ") + str(round(P, 2)))

        #Area
        #1) We need to find the angle of one of the interior triangles of the polygon
        Angle = 360/(2*N)

        #2) We need to translate the "Degrees" to "Radians"
        Angle_Rad = math.radians(Angle)

        #3) We use trigonometric functions to find the "Apothem" or Hight
        Area = L/(2*math.tan(Angle_Rad))

        #4) Print the result
        print(str("Area: ") + str(round(Area, 2)))

    if num1 == 5:
        print("Area and Perimeter of the Rectangle ")
        print(" A = Width x Length,     P = 2(Width) + 2(Length)")
        W = float(input("Give the Width: "))
        L = float(input("Give me the Length: "))

        #Area
        solve = W*L
        print(str("Area: ") + str(round(solve, 2)))

        #Perimeter
        solve = (2*W)+(2*L)
        print(str("Perimeter: ") + str(round(solve, 2)))

def pitag(num1):
    if num1 == 1:
        print("You must give two Sides: ")
        a = float(input("Side 1: "))
        b = float(input("Side 2: "))
        Hipocr = pow(a,2) + pow(b,2)
        print (math.sqrt(Hipocr))

    if num1 == 2:
        print("You must give: Any side and hypotenuse ")
        h = float(input("Hypo : "))
        x = float(input("Cateto : "))
        
        if h > x:
            Catet = pow(h,2) - pow(x,2)
            print(math.sqrt(Catet))
        elif h < x:
            Catet = pow(x,2) - pow(h,2)
            print(math.sqrt(Catet))


def Geometry():
    print("select your option: ")
    print("1) Area and Perimeter")
    print("2) Pythagoras" )

    userInput = int(input())

    if userInput == 1:
        print(" Area and Perimeter")
        Figuras()
        AranPer(int(input("Select your figure: ")))
        
    elif userInput == 2:
        print(" Pythagoras")
        pitagoras()
        pitag(int(input("Opcion: ")))
                   
    else:
        print("Invalid data")





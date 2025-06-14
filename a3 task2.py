import math 
a=float(input("Enter a number:"))
if a < 0:
    print("The number cannot be negative")
else:
    square=math.sqrt(a)
    print("square root",math.sqrt(square))
    logarithm=math.log(a)
    print("logarithm",logarithm)
    sine=math.sin(a)
    print("sin",sine)
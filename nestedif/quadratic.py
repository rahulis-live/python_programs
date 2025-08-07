#program to find the quadratic equation 

a  = float(input("Enrer number a: "))
b  = float(input("Enrer number b:  "))
c  = float(input("Enrer number c:  "))

r = (b**2) - 4 * a *c

if r == 0:
     value = -b / (2 * a)
     print(value)
elif r > 0:  
    value1 = (-b + r**0.5) / (2 * a)
    value2 = (-b - r**0.5) / (2 * a)
    print(value1, value2)
else :
    print("No values")       
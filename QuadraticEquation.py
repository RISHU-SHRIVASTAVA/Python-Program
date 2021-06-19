#Solve Quadratic Equation ax2 +bx +c=0
import cmath

a=int(input("Enter the coeficient of x2 :"))
b=int(input("Enter the coeficient of x :"))
c=int(input("Enter the coeficient of constant:"))

#Discriment

d=b*b - 4*a*c

x1=-b +cmath.sqrt(d)/2*a
x2=-b-cmath.sqrt(d)/2*a

print("Roots of Quadratic Equation {0} and {1} ".format(x1,x2))
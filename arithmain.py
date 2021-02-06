#import Arithmetic.add.add1
from Arithmetic.add import add1
from Arithmetic.sub import sub1 as s
from Arithmetic.carithmetic import *
try:
    x=int(input("Enter 1st number:"))
    y=int(input("Enter 2nd number:"))
    print("Addition of",x,"and",y,"is",add1(x,y))
    print("Substraction of",x,"and",y,"is",s(x,y))
    print("Multiplication of",x,"and",y,"is",mul1(x,y))
    print("Division of",x,"and",y,"is",div1(x,y))
except ValueError as ve:
    print(ve)

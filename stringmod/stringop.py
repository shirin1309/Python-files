#1.Create a module ‘stringop’ with functions to
#a
def rev(a):
    return a[::-1]
#b
def uplocase(a):
    b,c=0,0
    for i in a:
        if i.isupper():
            b=b+1
        elif i.islower():
            c=c+1
    return b,c
#c
def pal(a):
    a=a.lower()
    if a==a[::-1]:
        print("It is palindrome")
    else:
        print("It is not a palindrome")
#d
def pan(a):
    a=a.lower()
    b="abcdefghijklmnopqrstuvwxyz"
    for char in b:
        if char not in a:
            return "false"
    return "true"



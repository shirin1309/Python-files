from listmod.listop import uni as u
from listmod.listop import square as s

print("Enter list:")
x=[int(a) for a in input().split()]
print("a.....")
print("Unique list:",u(x))
print("b.....")
print("Square of list:",s(x))
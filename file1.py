try:
    f1=open("shirin.txt")
    f2=open("New.txt","w")
    a=f1.read()
    f2.write(a)
    f1.close()
    f2.close()
except IOError as io:
    print(io)
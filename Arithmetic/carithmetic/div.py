def div1(a,b):
    try:
        return a/b
    except ZeroDivisionError as zde:
        print(zde)
        
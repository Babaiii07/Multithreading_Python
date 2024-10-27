a = 5
b = 0
try :
    print("resource open")
    p = int(input("enter the number:-"))
    print(p)
    print(a/b)
except ValueError as e:
    print("invalid input")
except ZeroDivisionError as e:
    print("you cannot divide by zero")
except Exception as e :
    print("something went wrong")
finally :
    print("Resource closed")

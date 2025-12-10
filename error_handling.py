try:
    text = int("num")
    print(text)
except ValueError:
    print("invalid input")    
finally:
    print("finally done")   


try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Divide by zero is not allowed")
finally:
    print("finally done")    

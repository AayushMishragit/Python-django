add = square = lambda a,b:a + b
print(add(3,7))

square = lambda x:x ** 2
print(square(5))


numbers = [1,2,3,4]
doubled = list(map(lambda x:x*2,numbers))
print(doubled)
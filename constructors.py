class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        print(f"{name} object created")

p1 = Person("Alice",25)
p2 = Person("Bob",23)     
print(p1.name,p1.age)   
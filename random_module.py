import random

print(random.randint(1,10))
print(random.random())
print(random.choice(['red',"blue","green"]))
numbers = [1,2,3,4,5]
print(random.shuffle(numbers))
#correct syntax 
random.shuffle(numbers)
print(numbers)
print(random.sample(numbers,3))
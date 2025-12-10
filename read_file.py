file = open("sample.txt","r")
content = file.read()
print(content)
file.close()

with open("sample.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

       
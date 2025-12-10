import json
data = {"name":"Alice","age":25,"city":"NY"}
with open("data.json",'w') as file:
    json.dump(data,file)

with open("data.json",'r') as file:
    loaded = json.load(file)
    print(loaded)   
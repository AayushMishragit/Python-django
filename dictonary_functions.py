student = {"name":"Alice",
"Age":23,
"city":"New york"}
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"age":24})
print(student)
print("name " in student)
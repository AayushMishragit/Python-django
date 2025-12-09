age = 20
has_license = True
if age >= 18:
    print("Can Drive")
else:
    print("Need License")

#nested if else
age = 18
has_license = True
if age >= 18:
    if has_license:
        print("Can show")
    else:
        print("Need License")
else:
    print("Too Young")                
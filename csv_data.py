import csv
with open("output.csv",'w',newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age"])
    writer.writerow(["Alice",25])
    writer.writerow(["Bob",23])
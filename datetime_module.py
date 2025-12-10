from datetime import datetime,date,timedelta

print(datetime.now())
print(date.today())
today = date.today()
print(today.year,today.month,today.day)
future = today +timedelta(days=30)
print(future )
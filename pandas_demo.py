import pandas as pd

data = {
"Name":["Alice","bob","charlie"],
"Age":[23,24,25],
"City":['new York','la','chicago']
}
df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.describe())
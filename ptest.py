import pandas as pd


df = pd.DataFrame({"first_name":['tyler','amy','jake','james','tyler'], 
                   "last_name": ['chen', 'yu', 'hsiao', 'shen', 'liu'],
                   "age":[2,3,4,5,6],
                   "birthday": ["1997-02-03", "1998-09-06", "2000-03-02", "2003-05-03", "1992-03-04"],
                   "vaccined_date": ["2022-01-01", "2022-01-03", "2022-03-05", "2023-04-02", "2022-12-11"]})

print(df)

# Replace value in the age column, 1st time
df['age'] = df['age'].replace({2:20, 5:50})

print(df)

# Replace value in the age column, 2nd time
df[['age']] = df[['age']].replace({3:35})

print(type(df["age"].mean().max()))
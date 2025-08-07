import pandas as pd

data = {
    'Name' : ['Sivan','Babu','Sasi'],
    'Score': [90,95,92],
    'Passed': [False,True,True]
}

df = pd.DataFrame(data)
print(df)
print('\n')
# print(df['Name'])
print(df.loc[1])
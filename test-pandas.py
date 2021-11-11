import pandas as pd
df = pd.read_csv('dataframes/Pokemon.csv')

# print(df.iloc[2,1])

# for index, row in df.iterrows():
#     print(index, row['Name'])

# print(df.loc[df['Legendary'] == True])

# print(df.describe())


print(df.sort_values(['Type 1', 'Speed'], ascending=[0,1]))
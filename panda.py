import pandas as pd

data = {'name':  ['alice', 'bob', 'cahrlie'], 'score': [85,40,75]}
df = pd.DataFrame(data)

df['result'] = df['score'].apply(lambda x: 'paas' if x >= 50 else print(df))


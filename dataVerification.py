import pandas as pd
# Read train data
df = pd.read_csv('./data/sst_train.txt', sep='\t', header=None, names=['truth', 'text'])
df['truth'] = df['truth'].str.replace('__label__', '')
df['truth'] = df['truth'].astype(int).astype('category')
print(df.head())
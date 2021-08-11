from predict import predicts
import pandas as pd

df = pd.read_csv('data/test.csv', sep='\t', header=None)

print(df[1][500])

import pandas as pd

df = pd.read_csv('../symbolName1')
for index in df.index:
    s1 = df["Symbol"][index]
    s2 = df["Name"][index]
    print(s1 + ","+ s2)
import pandas as pd
df = pd.read_csv("fsv08.csv",sep=";")
df["VORNAME"] = df['NACHNAME'].str.split(',', expand=True)[1]
df["NACHNAME"] = df['NACHNAME'].str.split(',', expand=True)[0]
df.to_csv("fsv08cleaned.csv")
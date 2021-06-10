import pandas as pd

df1 = pd.read_csv("COVID19VaccDosesDelivered.csv")
df2 = pd.read_csv("COVID19VaccDosesAdministered.csv")

df1 = df1[['date', 'geoRegion', 'sumTotal']]
df2 = df2[['date', 'geoRegion', 'pop', 'sumTotal']]


df1 = df1.rename(columns={"sumTotal": "vax_delivered"})
df2 = df2.rename(columns={"sumTotal": "vax_administered"})

df = pd.merge(df1, df2, on=["date", "geoRegion"])

df["usage_rate"] = df.vax_administered/df.vax_delivered

print(df.head())
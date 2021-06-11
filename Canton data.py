import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")
import statistics
from Canton_Class import Canton

df1 = pd.read_csv("COVID19VaccDosesDelivered.csv")
df2 = pd.read_csv("COVID19VaccDosesAdministered.csv")

df1 = df1[['date', 'geoRegion', 'sumTotal']]
df2 = df2[['date', 'geoRegion', 'pop', 'sumTotal']]


df1 = df1.rename(columns={"sumTotal": "vax_delivered"})
df2 = df2.rename(columns={"sumTotal": "vax_administered"})

df = pd.merge(df1, df2, on=["date", "geoRegion"])

df=df.set_index('date')

df["usage_rate"] = df.vax_administered/df.vax_delivered

canton_names = df['geoRegion'].unique()

for i in range(len(canton_names)):
    temp_df = df[df['geoRegion'] == canton_names[i]]
    temp_df = temp_df[[ 'usage_rate']]
    temp_df = temp_df.loc[temp_df.index < '2021-03-01']
    temp_df.plot()
    plt.title(f' Usage rate in {canton_names[i]} ')
    plt.show()
    plt.close()
    print(canton_names[i], "mean:", statistics.mean(temp_df[ 'usage_rate']), "max:", max(temp_df[ 'usage_rate']), "standard deviavtion:", statistics.stdev(temp_df[ 'usage_rate']) )

cantons = []
for i in range(len(canton_names)):
    temp_df = df[df['geoRegion'] == canton_names[i]]
    temp_df = temp_df.loc[temp_df.index < '2021-03-01']
    cantons.append(Canton(canton_names[i], statistics.mean(temp_df['pop']), max(temp_df[ 'usage_rate']), temp_df['vax_delivered'].iloc[-1], temp_df['vax_administered'].iloc[-1] ))

for canton in cantons:
    print(canton)





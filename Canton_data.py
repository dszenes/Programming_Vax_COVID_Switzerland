import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")
import statistics
from Canton_Class import Canton
from Canton_Class import equi_distr, nat_doses

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



cantons = []
for i in range(len(canton_names)):
    temp_df = df[df['geoRegion'] == canton_names[i]]
    temp_df = temp_df.loc[temp_df.index < '2021-03-01']
    cantons.append(Canton(canton_names[i], statistics.mean(temp_df['pop']), max(temp_df[ 'usage_rate']), temp_df['vax_delivered'].iloc[-1], temp_df['vax_administered'].iloc[-1], statistics.stdev(temp_df[ 'usage_rate'])))

#we use tha max rather than the mean because we want to simulate the usage rate at the end of time period, where it will be higher than average

# we want to calculate how much vaccine usage improved in the period will simulate
#we first look at Switzerland and the total timespan
ch_end_df = df[df['geoRegion'] == 'CH']
ch_start_df = ch_end_df.loc[ch_end_df.index < '2021-03-01']
tot_improv = (((ch_end_df[ 'usage_rate'].iloc[-1])-max(ch_start_df[ 'usage_rate']))/(1-max(ch_start_df[ 'usage_rate'])))
print("Expected relative movemement toward usage = 1:",  tot_improv)

# we want to know by how much each canton should change every round in terms of non-quantity-dependent usage

per_round_change = tot_improv/12

for canton in cantons:
    print(canton)

equi_distr(cantons, 0)

print(ch_end_df[ 'usage_rate'].iloc[-1])








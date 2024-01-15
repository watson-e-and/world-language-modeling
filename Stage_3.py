import pandas as pd

df = pd.DataFrame()
df['Name'] =  ['India', 'Indonesia', 'Bangladesh', 'Mexico', 'Philippines', 'Egypt', 'South Africa', 'Kenya', 'Colombia', 'Sudan', 'Algeria', 'Morocco', 'Uzbekistan', 'Ecuador', 'Azerbaijan', 'UAE', 'Turkmenistan', 'Costa Rica', 'Lebanon', 'Panama', 'Jamaica', 'Botswana']
df['birth'] = [62972, 12085, 8152, 5062, 6877, 6703, 3088, 4160, 1925, 4327, 2380, 1726, 2006, 811, 324, 248, 352, 163, 193, 210, 87, 164]
df['deaths'] = [26097, 5836, 2552, 2396, 1850, 1701, 1429, 1083, 802, 865, 553, 615, 592, 249, 192, 44, 120, 80, 80, 66, 60, 52]
df['total_pop'] = [1435570900, 278740688, 173879223, 128951341, 118269586, 113633153, 60705532, 55675428, 52217945, 48764150, 45967423, 38038258, 35438713, 18289313, 10440041, 9556702, 6559980, 5230645, 5278981, 4499858, 2825291, 2698858]
df['population_proportion'] = (df['birth'] + df['deaths'])/df['total_pop']

print(df)


average_value_total_pop = df['population_proportion'].mean()

print("Average Stage 3", average_value_total_pop)
# births = [62972,]
# deaths = [26097,]
# total_pop = [1435570900,]
# data = { 'Name':, 
#         'Births/day': births, 
#         'Deaths/day': deaths, 
#         'Total Population': total_pop, 
#         'Population Proportion': }

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
city_data = {
"city_name": ["shiraz" , "karaj" , "tabriz","qom" , "ahvaz" , "kermanshah" , "oromie" , "rasht" , "zahedan" , "hamedan", "yazd" , "ardabil" , "bandar abbas" , "arak" , "qazvin" ],
"city_long": [52.5837 , 50.9391 , 46.2919 , 50.8764 , 48.6696 , 47.0798 , 45.0792 , 49.4418 , 60.8629 , 48.5164 , 54.3675 , 48.2961 , 56.2875 , 49.6892 , 50.0081],
"city_lat": [31.9822 , 35.8376 , 38.0666 , 34.6405 , 31.2700 , 34.2911 , 37.5000 , 38.4861 , 29.5450 , 34.7994 , 31.2150 , 38.4178 , 27.1833 , 34.1997 , 35.6897],
"city_pop": [1870000 , 1970000 , 1800000 , 1400000, 1300000 , 950000 , 740000 , 680000 , 600000 , 560000 , 530000 , 530000 , 530000 ,520000 , 400000],
"city_area": [240 , 162 , 324 , 115 , 375, 93 , 84 , 180 , 98 , 116 ,240 , 70 , 273 , 100 , 64]
}
df = pd.DataFrame.from_dict(city_data)
print(df)

# create new figure, axes instances.
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

# setup mercator map projection.
m = Basemap(llcrnrlon=44., llcrnrlat=25., urcrnrlon=63., urcrnrlat=40.,
            resolution='l', projection='merc')

m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgray')
x, y = m(df.city_long.values, df.city_lat.values)
# population scaling
sizes = [pop / 7000 for pop in df.city_pop]
m.scatter(x, y, s=sizes, c='red', marker='o', edgecolors='black')

plt.show()
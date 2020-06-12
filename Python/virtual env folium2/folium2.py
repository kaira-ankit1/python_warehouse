import folium
import pandas as pd

#print(dir(folium))

data = pd.read_csv('Volcanoes.txt')
#print(data.head())

#print(data.info())

lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
elev = list(data['ELEV'])

mymap = folium.Map()
fg = mymap.FeatureGroup(name = "my map")

for lt,ln,nm,el in zip(lat, lon, name, elev):
	fig.add_child(folium.Marker(location = [lt,ln], popup = str(n), icon = folium.Icon(color=func(el))   ))

mymap.add_child((fg))
mymap.save("project")

def func(n):
    if n<1000:
        return 'green'
    elif n>1000 and n<3000:
        return 'orange'
    else:
        return 'red'

print("Executed successfully")
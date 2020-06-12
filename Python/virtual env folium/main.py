import pandas as pd
import folium
print("it ran successfully")
# print(dir(folium))
#18°35'43.0"N 73°45'47.7"E
#18.595277, 73.763256
mymap = folium.Map(location = [18.595277, 73.763256])
mymap.save('myhome.html')

mymap2 = folium.Map(location=[18.595277, 73.763256])
m1 = folium.Marker(location = [18.595277, 73.763256], popup = 'MyHome-BlissSociety')
mymap2.add_child(m1)
mymap2.save('myhomecord.html')

#18°35'53.6"N 73°42'46.9"E
#18.598209, 73.713020
mymap3 = folium.Map(location = [18.595277, 73.763256])

fg = folium.FeatureGroup(name = 'something')

fg.add_child(folium.Marker(location = [18.595277, 73.763256], popup = 'MyHome-BlissSociety'))
fg.add_child(folium.Marker(location = [18.598209, 73.713020], popup = 'Office-Infosys'))

mymap3.add_child(fg)
mymap3.save('Home-office.html')

l = [[18.595277, 73.763256],[18.598209, 73.713020]]
mymap4 = folium.Map(location = [18.559528, 73.802055])

fg = folium.FeatureGroup(name = 'my map')
for cordinates in l:
    fg.add_child(folium.Marker(location=cordinates, popup="abc"))
mymap4.add_child(fg)

mymap4.save("mymap3.html")

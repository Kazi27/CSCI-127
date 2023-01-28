#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: November 1, 2021
#This program is a nyc map

import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)
folium.Marker([40.7420577, -74.0101494], popup="Little Island").add_to(mapCUNY)
mapCUNY.save(outfile='nycMap.html')

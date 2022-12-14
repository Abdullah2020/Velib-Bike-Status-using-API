# -*- coding: utf-8 -*-
"""Velib Status API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H9i5IbRcXhSqfSC-z_NxyrjoiC008iwQ

# **Real Time Velib status MAP**

**Project summary:**

The aim of this project is to explore Velib public bicycle sharing system in Paris by using the API concept to display real time statues of the bicycle in the entire Paris region.

### **Step 1: Implementation Step**

Get real time data from API
"""

import json
import requests
import pandas as pd
import urllib.request
import folium
from folium.plugins import MarkerCluster

"""**1- Get VELIB station list**"""

url = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"

velib_list = requests.get(url)
data_list = velib_list.json()

print(data_list)

"""**2- Get VELIB station status**"""

url_status = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"

velib_status = requests.get(url_status)
data_status = velib_status.json()
print(data_status)

"""### **Step 2: Construct display contain**

Tip: Use Python Folium library

Step 2.1: POI of each station: folium.CircleMarker
Each station contian: folium.Iframe

**Get an interactive map**
"""

world_map = folium.Map()
world_map

"""**Get an interactive map with a specific latitide and longtitude**"""

ISEP = folium.Map(location=[48.8231, 2.2741], control_scale=True)
ISEP

ISEP = [48.82471263032472, 2.2798535983081596]
boulder_coords = ISEP

my_map = folium.Map(Location = boulder_coords, zoom_start=19)

"""Define function to """

def set_html(name, bikes, ebikes, docks):
  html = f"""
  {name}</br>
  -------------------------------</br>
  Available Bike (Mechanical): {bikes}</br>
  Available Bike (Electrical): {ebikes}</br>
  Available Docking: {docks}</br>

  """
  return html

#create element for map

for n in data_list["data"]["stations"]:
  for m in data_status["data"]["stations"]:

    if n["stationCode"] == m["stationCode"]:
      html = set_html(n["name"], m["num_bikes_available_types"][0]["mechanical"], m["num_bikes_available_types"][1]["ebike"], m["num_docks_available"])
  
  iframe = folium.IFrame(html, width = 220, height=125)
  popup_content = folium.Popup(iframe, max_width=200)

  folium.CircleMarker(
      location = [n["lat"], n["lon"]],
      popup = popup_content,
      color = "red",
      radius = 12,
      fill_color = "red"
  ).add_to(my_map)

"""**Display the MAP**"""

my_map

"""**Conclusion:**


"""
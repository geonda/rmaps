import googlemaps
import pprint
import time
import geocoder
import numpy as np
from key import get_my_key
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import config

gmaps = googlemaps.Client(key=config.maps_token)
g = geocoder.ip('me')

try:
    places = gmaps.places_nearby(location='{lat}{lng}'.format(
        lat=g.latlng[0], lng=g.latlng[1]), radius=100, open_now=False, type='cafe')
except:
    places = gmaps.places_nearby(
        location=config.local, radius=5000, open_now=False, type='cafe')

df = pd.DataFrame.from_dict(places['results'])
df.to_pickle('places_db.pkl')
df = pd.read_pickle('places_db.pkl')

df['lat'] = [dict(df['geometry'])[i]['location']['lat']
             for i in range(len(dict(df['geometry'])))]
df['lng'] = [dict(df['geometry'])[i]['location']['lng']
             for i in range(len(dict(df['geometry'])))]
results = df[['name', 'rating', 'lat', 'lng']]


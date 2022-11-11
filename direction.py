import googlemaps
from datetime import datetime
import pandas as pd
import plotly.express as px
import time
import geocoder
import numpy as np
import plotly.graph_objects as go
from random import randrange
import config
class maps(object):
    """docstring for maps."""

    def __init__(self, fig):
        super(maps, self).__init__()


        direction_api = config.direction_token

        gmaps = googlemaps.Client(key=direction_api)
        # Geocoding an address
        df = pd.read_pickle('places_db.pkl')
        df['lat'] = [dict(df['geometry'])[i]['location']['lat'] for i in range(len(dict(df['geometry'])))]
        df['lng'] = [dict(df['geometry'])[i]['location']['lng'] for i in range(len(dict(df['geometry'])))]
        results = df[['name','rating','lat','lng'] ]

        g = geocoder.ip('me')
        print(g.latlng)
        # Request directions via public transit
        now = datetime.now()
        i = randrange(20)
        directions_result = gmaps.directions(g.latlng,
                                             [results.lat[i], results.lng[i]],
                                             mode="transit",
                                             departure_time=now)
        dircetctions_df = pd.DataFrame.from_dict(directions_result)
        dircetctions_df.to_pickle('{}_directions_db.pkl'.format(i))
        # with open('directions_db.pkl ')
        # dircetctions_df = pd.read_pickle('01_directions_db.pkl')
        # print(dircetctions_df['legs'][0][0]['steps'])
        lat=[]
        lng=[]
        time=[]
        import polyline

        for item in dircetctions_df['legs'][0][0]['steps']:
             tmp = polyline.decode(item['polyline']['points'])
             print(tmp)
             for items in tmp:
                 lat.append(items[0])
                 lng.append(items[1])


        fig.add_trace(go.Scattermapbox( lat=lat, lon=lng,

                             #center = dict(lat = g.center)
                               #mapbox_style="open-street-map"
                               ))
        token = 'pk.eyJ1IjoiZ2VvbmRhIiwiYSI6ImNsNzI3aG9zZDBoaXkzdW45aTNzOGtkcjEifQ.QmENCq9Nyg8b6Iq8uhMvFQ'


        fig.update_layout(
            title='',
            autosize=True,
            hovermode='closest',
            showlegend=False,
            mapbox=dict(
                accesstoken=token,
                center=dict(
                    lat=g.latlng[0],
                    lon=g.latlng[1]
                ),
                pitch=0,
                zoom=12,
                style='light'
            ),
        )
        fig.update_layout(
            margin=dict(l=1, r=1, t=1, b=1),
            )




# fig.show()
#     for label in item:
#         print('###'*10)
#         print(item[label])
#     #
    # print(item['start_address'])
    # print(item['end_address'])
    # print(dircetctions_df['legs'][0][item])

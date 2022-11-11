import googlemaps
import geocoder
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import config


class maps(object):
    """docstring for rmaps."""

    def __init__(self, fig):
        super(maps, self).__init__()
        gmaps = googlemaps.Client(
            key=config.maps_token)

        g = geocoder.ip('me')

        df = pd.read_pickle('places_db.pkl')

        df['lat'] = [dict(df['geometry'])[i]['location']['lat']
                     for i in range(len(dict(df['geometry'])))]
        df['lng'] = [dict(df['geometry'])[i]['location']['lng']
                     for i in range(len(dict(df['geometry'])))]
        results = df[['name', 'rating', 'lat', 'lng']]

        fig.add_trace(go.Scattermapbox(
            lat=[g.latlng[0]],
            lon=[g.latlng[1]],
            mode='markers',
            marker_size=10,
            marker_color='grey'
        ))

        location_name = list(results['name'])
        fig.add_trace(go.Scattermapbox(
            lat=results.lat,
            lon=results.lng,
            mode='text+markers',
            marker_color='blue',
            hoverinfo='text',
            marker_size=20,
            opacity=0.5,
            text=location_name,
        ))
        fig.update_layout(
            title='',
            autosize=True,
            hovermode='closest',
            showlegend=False,
            mapbox=dict(
                accesstoken=config.mapbox_token,
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
        self.fig=fig
        

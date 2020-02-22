import numpy as np
import pandas as pd
import googlemaps
from getpass import getpass

df = pd.read_csv("M357_students.csv")
df.head()

gmaps = googlemaps.Client(key=getpass("Type in your API key: "))

school_names = df['School'].tolist()

school_names = [i.strip() for i in school_names]

school_names = list(set(school_names))

school_names.remove('San Dimas High')

results = []

for school in school_names:
    result = gmaps.geocode(school)
    results.append(result)


latitudes = []
longitudes = []
for result in results:
    latitude = result[0]['geometry']['location']['lat']
    longitude = result[0]['geometry']['location']['lng']
    latitudes.append(latitude)
    longitudes.append(longitude)

result_df = pd.DataFrame.from_dict({'school_name': school_names, 'latitude': latitudes, 'longitude': longitudes})
result_df.to_csv("school_coordinates.csv", index=False)

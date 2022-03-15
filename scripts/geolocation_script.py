# from pip._internal import main
# main(['install','pandas'])
# from pip._internal import main
# main(['install','geopandas'])
from pip._internal import main
main(['install','geopy'])

#import pandas as pd
#import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim

from urllib.request import urlopen
from json import load


def geolocation_func(addr=''):
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    # for attr in data.keys():
    #     #will print the data line by line
    #     print(attr,' '*13+'\t->\t',data[attr])

    locator = Nominatim(user_agent="findmycoords")
    coordinates = data["loc"]
    location = locator.reverse(coordinates)
    location = location.address
    location = location[0:location.index(",")] + location[location.index(",")+1:]
    return location
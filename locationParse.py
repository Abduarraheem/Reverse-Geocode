'''
Juno Mayer, Alex Marozick and Abduarraheem Elfandi

'''
import os
import utm
import requests
import sys
import gpxpy
import gpxpy.gpx
import json
from configparser import ConfigParser
from simplify import giveCueSheet



def main(file=''):


    if file == '':
        print("No file given")
        return
    gpx_file = open(file, 'r')
    gpx = gpxpy.parse(gpx_file)

    return giveCueSheet(gpx)


# class MyTrack:
#     '''
#         Each track will contain a name and a list of locations that are in that track segment.
#     '''
#     listLocation = []
#     def __init__(self, trackName):
#         self.trackName = trackName



# class Location:
#     '''
#         A location is a part of a track which contains a latitude,
#         longitude, elevation, the time that location has been reached
#         and the street name of where that location is at.
        
#         Then a group of locations will all be put into a list of location for that specific track.

#     '''

#     def __init__(self, latitude: float, longitude: float, elevation: float, time: str, stName: str):
#         self.latitude = latitude
#         self.longitude =  longitude
#         self.elevation = elevation
#         self.time = time
#         self.stName = stName
    

# def getStName(lat: float, lng: float):
#     '''
#     Function that gets the street name given the latitude and longitude.
#     '''
#     payload  = {"apiKey" : api_key, "version" : "4.10", 
#                 "lat" : lat, "lon" : lng, "format" : "JSON"}

#     r = requests.get("http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/", params=payload)
#     # print(r.text)
#     result = json.loads(r.text)
    
#     return result["StreetAddresses"][0]["StreetAddress"]






if __name__ == "__main__":
    main()

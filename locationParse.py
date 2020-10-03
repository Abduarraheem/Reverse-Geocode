'''
Abduarraheem Elfandi and Juno Mayer.

'''
import os
import utm
import requests

import gpxpy
import gpxpy.gpx
import json

# TODO make sure the GPX file is taken from the user not a predefined file
print(os.getcwd())
gpx_file = open('Project 1/Reverse-Geocode/TestFiles/smallGPX.gpx', 'r')
gpx = gpxpy.parse(gpx_file)



trackList = [] # A list that will contain all the tracks

class MyTrack:
    listLocation = []
    def __init__(self, trackName):
        self.trackName = trackName


'''
    A location is a part of a track which contains a latitude,
    longitude, elevation, the time that location has been reached
    and the street name of where that location is at.
'''
class Location:
    def __init__(self, latitude: float, longitude: float, elevation: float, time: str, stName: str):
        self.latitude = latitude
        self.longitude =  longitude
        self.elevation = elevation
        self.time = time
        self.stName = stName
    

def getStName(lat: float, lng: float ):
    '''
    Function that gets the street name given the latitude and longitude.
    '''
    payload  = {"apiKey" : "58bd566df1854af4885c680dd2c42dc1", "version" : "4.10", 
                "lat" : lat, "lon" : lng, "format" : "JSON"}

    r = requests.get("http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/", params=payload)
    # print(r.text)

    result = json.loads(r.text)

    return result["StreetAddresses"][0]["StreetAddress"]



for track in gpx.tracks:
    myTrack = MyTrack(track.name)
    trackList.append(myTrack)
    for segment in track.segments:
        for point in segment.points:
            myTrack.listLocation.append(Location(point.latitude, point.longitude, point.elevation, point.time, getStName(point.latitude, point.longitude)))


# for i in range(len(trackList)):
#     listLoc = trackList[i].listLocation
#     print(f'Track Number: {i}')
#     for j in range(len(listLoc)):
#         print(f'Entry {j}: latitude {listLoc[j].latitude}, longitude {listLoc[j].longitude},\ 
#         elevation {listLoc[j].elevation}, time {listLoc[j].time}, street {listLoc[j].stName}')

#     print(f'Track Name: {trackList[i].trackName} Track Number: {i}')
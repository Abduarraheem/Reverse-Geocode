import os
import utm
import requests
import sys
import gpxpy
import gpxpy.gpx

import anm_api_test

# TODO make sure the GPX file is taken from the user not a predefined file
class MyTrack:
    listLocation = []
    def __init__(self, trackName):
        self.trackName = trackName

'''
    A location is a part of a track which contains a latitude,
    longitude, elevation and the time that location has been reached.
    TODO get the street names which will also be a part of the location 
'''
class Location:
    def __init__(self, latitude: float, longitude: float, elevation: float, time: str, stName: str):
        self.latitude = latitude
        self.longitude =  longitude
        self.elevation = elevation
        self.time = time
        self.stName = stName
    

def getStName(lat: float, lng: float ):



    payload  = {"apiKey" : "58bd566df1854af4885c680dd2c42dc1", "version" : "4.10", 
                "lat" : lat, "lon" : lng, "format" : "JSON"}

    r = requests.get("http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/", params=payload)
    print(r.text)

    result = json.loads(r.text)
    return result["StreetAddresses"][0]["StreetAddress"]


def main():

    

    gpx_file = open(sys.argv[1], 'r')
    gpx = gpxpy.parse(gpx_file)



    trackList = [] # A list that will contain all the tracks



    for track in gpx.tracks:
        myTrack = MyTrack(track.name)
        trackList.append(myTrack)
        for segment in track.segments:
            for point in segment.points:
                myTrack.listLocation.append(Location(point.latitude, point.longitude, point.elevation, point.time, getStName(point.latitude, point.longitude)))


    for i in range(len(trackList)):
        listLoc = trackList[i].listLocation
        print(f'Track Number: {i}')
        for j in range(len(listLoc)):
            print('Entry {0}: latitude {1}, longitude {2}, elevation {3}, time {4}, street {5}'
            .format(j, listLoc[j].latitude, listLoc[j].longitude, listLoc[j].elevation, listLoc[j].time, listLoc[j].stName))
        print(f'Track Name: {trackList[i].trackName} Track Number: {i}')

if __name__ == "__main__":
    main()
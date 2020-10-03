import os
import utm
import requests

import gpxpy
import gpxpy.gpx

# TODO make sure the GPX file is taken from the user not a predefined file
gpx_file = open('Prototype/testGPX.gpx', 'r')
gpx = gpxpy.parse(gpx_file)



trackList = [] # A list that will contain all the tracks

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
    def __init__(self, latitude: float, longitude: float, elevation: float, time: str):
        self.latitude = latitude
        self.longitude =  longitude
        self.elevation = elevation
        self.time = time
        # self.stName = stName
    



for track in gpx.tracks:
    myTrack = MyTrack(track.name)
    trackList.append(myTrack)
    for segment in track.segments:
        for point in segment.points:
            myTrack.listLocation.append(Location(point.latitude, point.longitude, point.elevation, point.time))

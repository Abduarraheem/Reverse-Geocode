'''
Abduarraheem Elfandi and Juno Mayer.

'''
import os
import utm
import requests
import sys
import gpxpy
import gpxpy.gpx
import json

# TODO make sure the GPX file is taken from the user not a predefined file
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
    

def getStName(lat: float, lng: float):
    '''
    Function that gets the street name given the latitude and longitude.
    '''
    payload  = {"apiKey" : "58bd566df1854af4885c680dd2c42dc1", "version" : "4.10", 
                "lat" : lat, "lon" : lng, "format" : "JSON"}

    r = requests.get("http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/", params=payload)
    # print(r.text)

    result = json.loads(r.text)
    return result["StreetAddresses"][0]["StreetAddress"]


def main():

    # TODO need to change it so that we get the file from the website
    gpx_file = open(sys.argv[1], 'r')
    gpx = gpxpy.parse(gpx_file)



    trackList = [] # A list that will contain all the tracks

    for track in gpx.tracks:
        myTrack = MyTrack(track.name)
        trackList.append(myTrack)
        for segment in track.segments:
            for point in segment.points:
                myTrack.listLocation.append(Location(point.latitude, point.longitude, point.elevation, point.time, getStName(point.latitude, point.longitude)))


    # TODO need to make the output to the file a little more cleaner
    output = open("output.txt", "w+")
    for i in range(len(trackList)):
        listLoc = trackList[i].listLocation
        output.write(f'Track Number: {i}')
        for j in range(len(listLoc)):
            output.write(f'Entry {j}: latitude {listLoc[j].latitude}, longitude {listLoc[j].longitude}, ')
            output.write(f'elevation {listLoc[j].elevation}, time {listLoc[j].time}, street {listLoc[j].stName} \n')
            
        output.write(f'Track Name: {trackList[i].trackName} Track Number: {i}\n')
    output.close()
if __name__ == "__main__":
    main()

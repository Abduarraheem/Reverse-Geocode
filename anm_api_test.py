"""
Juno Mayer 

A test call to request from the Texas AnM Reverse Geocoding API 
using the python requests module 
"""
import requests
import json

def main():

    myLat = 30.610487
    myLon = -96.327766

    payload  = {"apiKey" : "58bd566df1854af4885c680dd2c42dc1", "version" : "4.10", 
                "lat" : myLat, "lon" : myLon, "format" : "JSON"}

    r = requests.get("http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/", params=payload)
    print(r.text)

    result = json.loads(r.text)
    print(result["StreetAddresses"][0]["StreetAddress"])


# https://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest
# /?lat=30.610487&lon=-96.327766&state=tx&apikey=58bd566df1854af4885c680dd2c42dc1&format=json&notStore=false&version=4.10

if __name__ == "__main__":
    main()
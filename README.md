# Reverse-Geocode

Contributors:
    Alex Marozick, Juno Mayer, Abduarraheem Elfandi
                                            
                                        Project Overview
Hikers, runners, and cyclists often record their activites using a phone, fitness watch, or dedicated GPS device. They may upload data from their devices to a system like Strava, MapMyRun, or RideWithGPS, which typically provide analysis, map display, and optional social media sharing. Existing services like Strava provide a variety of analyses and record keeping, but they typically do not provide a fully automated way to extract turn-by-turn directions from a recorded activity. For hikers and runners and some cyclists who travel off-road, this might be very difficult … there may be no suitable database from which to extract suitable cues. For road cyclists, however, it should be possible to extract turn-by-turn directions (a “cue sheet”) from a recording.
That is what our system does. The input will be a gpx or xml file which are records consisting of a sequence of (latitude, longitude) pairs, possibly with other information. The output is be a list of turn-by-turn directions.
            
Geocoding means translating place names or descriptions into geographic coordinates, usually latitude and longitude. If you have used a web mapping service, you have probably used geocoding to find a destination or place of interest.

Reverse geocoding, as you might guess, translates coordinates to addresses. This involves some very cool data structures and algorithms called spatial indexes, but you don’t need to understand spatial indexes to use a reverse geocoding service.

Cited by Prof. Michal's repo at https://uo-cis422.github.io/chapters/projects/reverse/reverse.html 




Developer log, further documentation for end users and for developers looking to further the project will be available on our wiki on our github at https://github.com/Abduarraheem/Reverse-Geocode/wiki
    

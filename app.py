'''
Juno Mayer, Alex Marozick and Abduarraheem Elfandi

'''

from flask import Flask, render_template, url_for, request, redirect, abort, flash, jsonify, session
import os
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException, default_exceptions, Aborter
import pprint
import locationParse
import requests
import json
import config


class FileTypeException(HTTPException):   # this error is thrown when the file type is incorrect
    code = 400
    description = 'Error: File Type Incorrect!'

default_exceptions[400] = FileTypeException
abort = Aborter()

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'TestFiles'
app.config['UPLOAD_EXTENSIONS'] = ['.gpx', '.xml'] # can add other file types in the list
secret_key = os.urandom(24)
app.secret_key = secret_key

mapbox_key = config.get('mapbox_key')

@app.route('/', methods=['GET', 'POST'])
def index():
    session['coords_list'] = [] # set the coords list to be empty at first

    
    if request.method == 'POST':
        uploaded_file = request.files["gpx_file"] # the file name is listed as gpx_file in index.html
        fileName = secure_filename(uploaded_file.filename)
        if fileName != "":

            # next 3 lines validate the file type
            file_ext = os.path.splitext(fileName)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)

            #save the file in the given directory
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], fileName))

            #calls main in location parse with the file in the upload path            
            cuesheet = locationParse.main('TestFiles/' + uploaded_file.filename) # run the parsing which will generate an output.
            #cuesheet contains the JSON object and instructions is a list of the values for instructions within the JSON object
            # pprint.pprint(cuesheet)
            if cuesheet is None:
                return flash("NO API KEY GIVEN")

            instructions = []
            coordinates = []

            for cue in cuesheet['cuesheet']:
                if cue['distance'] >= 1000:
                    cue['distance'] = float(cue['distance'])/1000
                    unit = "km"
                else:
                    unit = "m"
                instructions.append((cue['maneuver'], cue['distance'], unit))
                coordinates.append(cue['coordinate'])
            coords_list = coordinates
            session['coords_list'] = coords_list # save the coordinates 
        return render_template("index.html", instructions = instructions)

    return render_template("index.html"), 200

@app.route('/give_coords')
def give_coords(): 
    #also give tehe mapbox key 
    if 'coords_list' in session:
        coords_list = session['coords_list']
        print(coords_list)
        zoom_value = 7
    else:
        coords_list = []
        zoom_value = 1        
    return jsonify({'key' : mapbox_key, 'coords': coords_list, 'zoom' : zoom_value})





@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def page_forbidden(e):
    return render_template("403.html"), 403



if __name__ == "__main__":
    app.run(debug=True)
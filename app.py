from flask import Flask, render_template, url_for, request, redirect

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField
import locationParse

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        uploaded_file = request.files["gpx_file"] # the file name is listed as gpx_file in index.html
        fileName = uploaded_file.filename
        if fileName != "":
            uploaded_file.save(uploaded_file.filename) # saves the file to the directory.
            locationParse.main(uploaded_file.filename) # run the parsing which will generate an output.
        return redirect(url_for("index"))

    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def page_forbidden(e):
    return render_template("403.html"), 403




if __name__ == "__main__":
    app.run(debug=True)
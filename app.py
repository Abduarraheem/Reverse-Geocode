from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        uploaded_file = request.files["gpx_file"]
        if uploaded_file.filename != "":
            uploaded_file.save(uploaded_file.filename)
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
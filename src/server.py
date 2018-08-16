from flask import Flask, render_template, send_from_directory

app = Flask("StreamSpeed!")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/video/<string:filename>")
def stream(filename: str):
    dir = "../video"
    return send_from_directory(directory=dir, filename=filename)

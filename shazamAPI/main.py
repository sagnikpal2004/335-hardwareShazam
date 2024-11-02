import flask

app = flask.Flask("shazamAPI")

@app.route("/", methods=["GET"])
def home():
    return "OK", 200

@app.route("/", methods=["POST"])
def recognize_song():
    return "Not implemented", 501

app.run()
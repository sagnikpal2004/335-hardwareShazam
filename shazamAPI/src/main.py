import flask
import shazamio

app = flask.Flask("shazamAPI")
shazam = shazamio.Shazam()

@app.get("/")
def home():
    return "OK", 200

@app.post("/")
async def recognize_song():
    file = flask.request.files["file"]
    if not file:
        return "No file provided", 400
    filebytes = file.read()

    result = await shazam.recognize(filebytes)
    return flask.jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")
from flask import Flask, request
from flask_cors import cross_origin
from gevent import pywsgi
from flask import Response


app = Flask(__name__)
app.config.update(DEBUG=True)

folder = './audios/output/audio/und/mp4a.40.2/'


@app.route('/mp3/<file_key>')
@cross_origin()
def stream_mp3(file_key):
    def generate():
        path = folder + file_key
        with open(path, 'rb') as video:
            data = video.read(1024)
            while data:
                yield data
                data = video.read(1024)
    return Response(generate(), mimetype="audio")



if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8008), app)
    server.serve_forever()

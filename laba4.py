from flask import Flask
from waitress import serve
app = Flask(__name__)


@app.route('/api/v1/hello-world-<numb>')
def myendpoint(numb):
    return f'Hello World {numb}'


serve(app)#, host='0.0.0.0', port=8080)  # WAITRESS!


# http://192.168.0.105:8080/api/v1/hello-world-11

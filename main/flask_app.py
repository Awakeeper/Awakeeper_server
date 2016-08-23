
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import csv
import json

app = Flask(__name__)

@app.route('/')
def data_throw():
    f = open('./main/dummy_log/scenario.log.csv')
    reader = csv.DictReader(f, fieldnames = ('time', 'carId', 'gpsX', 'gpsY',
                        'velocity', 'angle', 'roadType', 'heartBeat', 'iris',
                        'CO', 'windowOffset', 'RPM', 'aircondition'))
    out = json.dumps([row for row in reader])
    return out
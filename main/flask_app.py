
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import csv
import sys
import json

app = Flask(__name__)

@app.route('/')
def data_throw():
    f = open('./main/dummy_log/dummy.log.csv')
    reader = csv.DictReader(f, fieldnames = ('time', 'ID', 'x', 'y', 'speed'))
    out = json.dumps([row for row in reader])
    return out
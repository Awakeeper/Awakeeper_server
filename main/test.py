import csv
import sys
import json

f = open('./main/dummy_log/dummy.log.csv')
reader = csv.DictReader(f, fieldnames = ('time', 'ID', 'x', 'y', 'speed'))
out = json.dumps([row for row in reader])
f = open('./main/parsed_log/parsed.json', 'w')
f.write(out)
print(out)
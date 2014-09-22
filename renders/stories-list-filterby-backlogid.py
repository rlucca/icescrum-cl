#!/usr/bin/python

import json
from sys import stdin, argv

data = json.load(stdin)

interested_backlogs = []

for number in argv[1:]:
  try:
    interested_backlogs.append(int(number))
  except:
    pass

def existsData(value, defValue):
  if value is None:
    return defValue
  return value

if len(interested_backlogs) != 0:
  filterOn = 1
else:
  filterOn = 0

data_filtered = []
for x in data:
  try:
    if filterOn == 1:
      if existsData(x["parentSprint"], {"id", -1})["id"] in interested_backlogs:
        data_filtered.insert(0, "%d - %s - Tasks: %d" % (x['id'], x['name'], len(x['tasks'])))
    else:
      data_filtered.insert(0, "%d - %s - Tasks: %d" % (x['id'], x['name'], len(x['tasks'])))
  except TypeError:
    continue

for line in data_filtered:
  print line
#print len(data_filtered)

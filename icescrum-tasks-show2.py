#!/usr/bin/python

import json
from sys import stdin, argv

data = json.load(stdin)

task_state = { 0: "To be done",
               1: "In progress",
               2: "Done" };

def existsData(value, defValue):
  if value is None:
    return "-"
  return value

def convertDataToInt(value, defValue):
  try:
    return int(value)
  except:
    return defValue

print "%d (Commit Use Only: %d) - %s" % (data['id'], data['uid'], data['name'])

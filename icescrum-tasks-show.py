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

print "ID: %d (Commit Use Only: %d)" % (data['id'], data['uid'])
print "Name: %s" % data['name']
print "State: %s" % task_state[data['state']]
print "DoneDate: %s" % existsData(data['doneDate'], "-")
print "Estimation: %d" % convertDataToInt(data['estimation'], -1)
try:
  print "Story: %d" % data['parentStory']['id']
except:
  print "Story: -"
try:
  print "Backlog: %d" % data['backlog']['id']
except:
  print "Backlog: -"
print "Description: %s" % existsData(data['description'], "-")

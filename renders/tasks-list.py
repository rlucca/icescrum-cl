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

interested_states = []

for number in argv[1:]:
  try:
    interested_states.append(int(number))
  except:
    pass

FREE_TASK=0

if len(interested_states) == 0:
  interested_states.append(FREE_TASK)

for task in data:
  if task['state'] in interested_states:
    print "%d - %s - %s - %d" % (task['id'], task['name'], task_state[task['state']], convertDataToInt(task['estimation'], -1))

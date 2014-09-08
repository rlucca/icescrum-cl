#!/usr/bin/python

import json
from sys import stdin, argv
from os import system

data = json.load(stdin)

SUGERIDA = 1
ACEITA = 2
ESTIMADA = 3
PLANEJADA = 4
EM_ANDAMENTO = 5
TERMINADA = 7
story_state = { 1: "Suggested",
                2: "Accepted",
                3: "Estimated",
                4: "Planned",
                5: "In progress",
                7: "Done" };

def existsData(value, defValue):
  if value is None:
    return "-"
  return value

print "ID: %d" % data['id']
print "Name: %s" % data['name']
print "State: %s" % story_state[data['state']]
print "PlannedDate: %s" % existsData(data['plannedDate'], "-")
print "DoneDate: %s" % existsData(data['doneDate'], "-")
print "Description: %s" % existsData(data['description'], "-")

ntasks = len(data['tasks'])
if ntasks > 0:
  tasklist = [str(task['id']) for task in data['tasks']]
  print "Tasks (%d):" % ntasks
  for task in tasklist:
    system("icescrum task -S %s" % task)


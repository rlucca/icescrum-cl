#!/usr/bin/python

import json
from sys import stdin, argv

data = json.load(stdin)

story_state = { 1: "Suggested",
                2: "Accepted",
                3: "Estimated",
                4: "Planned",
                5: "In progress",
                7: "Done" };

interested_states = []

for number in argv[1:]:
  try:
    interested_states.append(int(number))
  except:
    pass

EM_ANDAMENTO=5

if len(interested_states) == 0:
  interested_states.append(EM_ANDAMENTO)

data_filtered = []
for x in data:
  try:
    if x['state'] in interested_states:
      data_filtered.insert(0, "%d - %s - Tasks: %d" % (x['id'], x['name'], len(x['tasks'])))
    #else:
    #  data_filtered.append("%d - %s - State: %s" % (x['id'], x['name'], story_state[x['state']]))

  except TypeError:
    continue

for line in data_filtered:
  print line
#print len(data_filtered)

#!/bin/bash

. icescrum-setup.sh

TASK_ID=$1

[ -z $SHOW ] && SHOW=icescrum-tasks-show.py

curl -s -b /tmp/cookie.jar -c /tmp/cookie.jar "${URL}/p/${PROJECT_ID}/task/${TASK_ID}" -H "Referer: ${URL}/p/${PROJECT_NAME}" -H "X-Requested-With: XMLHttpRequest" --get -H "Content-Type: application/json" | $SHOW


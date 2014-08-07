#!/bin/bash

. icescrum-setup.sh

STORY_ID=$1

curl -s -b /tmp/cookie.jar -c /tmp/cookie.jar "${URL}/p/${PROJECT_ID}/story/${STORY_ID}" -H "Referer: ${URL}/p/${PROJECT_NAME}" -H "X-Requested-With: XMLHttpRequest" --get -H "Content-Type: application/json" | icescrum-stories-show.py


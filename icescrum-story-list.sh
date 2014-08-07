#!/bin/bash

. icescrum-setup.sh

curl -s -b /tmp/cookie.jar -c /tmp/cookie.jar "${URL}/p/${PROJECT_ID}/story/list" -H "Referer: ${URL}/p/${PROJECT_NAME}" -H "X-Requested-With: XMLHttpRequest" --get -H "Content-Type: application/json" | icescrum-stories-list.py $*


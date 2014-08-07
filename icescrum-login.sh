#!/bin/bash

. icescrum-setup.sh

curl -c /tmp/cookie.jar $URL/j_spring_security_check -d "j_username=$USER&j_password=$PASS" -X POST

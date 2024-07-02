#!/bin/bash
# This is a Bash script that displays all the allowed methods on a web server
curl -si "$1"|sed -n 's/Allow: //1 p'

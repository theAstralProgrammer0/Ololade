#!/bin/bash
# A Bash script that displays the size of the body of a response
curl -sI "$1"|grep Content-Length|awk '{print $2}'

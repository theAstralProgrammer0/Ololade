#!/bin/bash
# This bash script displays only the status of a request made to a url
curl -so /dev/null -w "%{http_code}" "$1"

#!/bin/bash
# This script makes a POST request of the contents of a json file to a url using curl
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"

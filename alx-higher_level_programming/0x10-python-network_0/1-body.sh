#!/bin/bash
# This is a Bash script that takes in a URL, sends a GET request to the URL (including redirects), and displays the body of the response
curl -sL "$1"

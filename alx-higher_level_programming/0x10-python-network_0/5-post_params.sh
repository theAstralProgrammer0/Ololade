#!/bin/bash
# This script sends a POST request (with some params) to the url passed to it
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"

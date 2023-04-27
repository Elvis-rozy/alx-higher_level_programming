#!/bin/bash
# send JSON POST request to URL passed as first argument and displays the response
curl -s -H "Content-Type: application/json" -d @"$2" "$1"

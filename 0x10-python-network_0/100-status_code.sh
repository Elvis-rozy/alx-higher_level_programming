#!/bin/bash
# sends a rquest to URL passed as an argument and displays the status code only
curl -s -o /dev/null -w "%{http_code}" "$1"

#!/bin/bash
# takes a a URL, send a POST request and displays the response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I am an alx student"

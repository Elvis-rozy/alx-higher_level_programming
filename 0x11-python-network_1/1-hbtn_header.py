#!/usr/bin/python3
"""
Script that takes in a URL
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
- You must use the packages urllib and sys
- You are not allow to import packages other than urllib and sys
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a with statement
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    reqest = urllib.request.Request(url)
    with urllib.reqest.urlopen(reqest) as response:
        print(dict(response.headers).get("X-Request-Id"))

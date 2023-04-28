#!/usr/bin/python3
"""
    The email must be sent in the email variable, You must use the packages urllib and sys, You are not allowed to import packages other than urllib and sys, You don’t need to check arguments passed to the script (number or type), You must use the with statement
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))

#!/usr/bin/python3
"""
    The email must be sent in the email variable, You must use the packages urllib and sys, You are not allowed to import packages other than urllib and sys, You don’t need to check arguments passed to the script (number or type), You must use the with statement
"""
import urllib.request
from sys import argv


def main(argv):
    """
    script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))

if __name__ == "__main__":
    main(argv)

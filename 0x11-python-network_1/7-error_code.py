#!/usr/bin/python3
"""Script that takes in a URL
- sends a request to the given URL
- and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    reque = requests.get(url)
    if reque.status_code >= 400:
        print("Error code: {}".format(reque.status_code))
    else:
        print(reque.text)

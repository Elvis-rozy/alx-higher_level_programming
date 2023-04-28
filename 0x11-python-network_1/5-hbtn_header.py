#!/usr/bin/python3
"""Script that takes in a URL, sends a request, displays the value of X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    reque = requests.get(url)
    print(reque.headers.get("X-Request-Id"))

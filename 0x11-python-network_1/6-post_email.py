#!/usr/bin/python3
"""Script sends a POST request to given URL
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    content = {"email": sys.argv[2]}

    reque = requests.post(url, data=content)
    print(reque.text)

#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    reque = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(reque.text)))
    print("\t- content: {}".format(reque.text))

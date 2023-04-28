#!/usr/bin/python3
"""Script that:
- takes a letter
- POST to http://0.0.0.0:5000/search_user
- with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    lettr = "" if len(sys.argv) == 1 else sys.argv[1]
    payload_taken = {"q": lettr}

    reque = requests.post("http://0.0.0.0:5000/search_user", data=payload_taken)
    try:
        response = reque.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

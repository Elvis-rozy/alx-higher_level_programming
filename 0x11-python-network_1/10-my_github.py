#!/usr/bin/python3
"""Script that:
- takes your GitHub credentials 
- (username and password)
- and uses the GitHub API to 
- display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    user = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(user, password))
    try:
        profile_information = response.json()
        print(profile_information['id'])
    except:
        print('None')

if __name__ == "__main__":
    main(argv)

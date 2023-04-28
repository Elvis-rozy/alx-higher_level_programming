#!/usr/bin/python3
"""
    You must use the package urllib, You are not allowed to import any packages other than urllib, You must use a with statement
"""
import urllib.request


def main():
    """
    Python script that fetches https://alx-intranet.hbtn.io/status and prints the response
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))

if __name__ == "__main__":
    main()

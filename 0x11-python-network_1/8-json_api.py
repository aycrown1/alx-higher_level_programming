#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
"""

import sys
import requests

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

url = 'http://0.0.0.0:5000/search_user'
params = {'q': letter}

if __name__ == "__main__":
    try:
        response = requests.post(url, data=params)
        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get('id'), data.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Request error: {}".format(e))

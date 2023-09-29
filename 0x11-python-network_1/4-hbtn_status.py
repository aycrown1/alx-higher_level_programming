#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    url = requests.get("https://alx-intranet.hbtn.io/status")
    try:
        print("Body response:")
        print("\t- type: {}".format(type(url.text)))
        print("\t- content: {}".format(url.text))
    except requests.exceptions.RequestException as e:
        print("Request error: {}".format(e))

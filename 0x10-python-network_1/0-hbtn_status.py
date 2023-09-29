#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    url = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode("utf-8")))
    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e}")
#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
"""
import sys
import urllib.request


if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)
url = sys.argv[1]


if __name__ == "__main__":
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            if 'X-Request-Id' in response.headers:
                print(dict(response.headers).get("X-Request-Id"))
    except urllib.error.URLError as e:
        print(f"Error fetching the URL: {e}")

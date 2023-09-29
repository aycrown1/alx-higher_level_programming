#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
"""

import sys
import urllib.parse
import urllib.request


if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

if __name__ == "__main__":
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data)

    try:
        with urllib.request.urlopen(request) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except urllib.error.URLError as e:
        print(f"Error sending POST request: {e}")

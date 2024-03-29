#!/usr/bin/python3
"""fetches the X-Request-Id variable in the response header"""
from requests import get
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = get(url).headers
    print("{}".format(response.get('X-Request-Id')))

#!/usr/bin/python3
# displays the body of the response or error code if URLError
from urllib import request, error
import sys

if len(sys.argv) != 2:
    print("Usage: ./3-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]


if __name__ == "__main__":
    try:
        with request.urlopen(url) as response:
            content = response.read()
            print("{}".format(content.decode('utf-8')))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except error.URLError as e:
        print("Error fetching the URL: {}".format(e))

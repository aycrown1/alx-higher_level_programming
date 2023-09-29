#!/usr/bin/python3
# takes in github credentials and displays the id
from requests import get
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)
    response = get(url, auth=auth)
    user_id = response.json().get('id')
    print(user_id)

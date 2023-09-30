#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""

import requests
import sys

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'


if __name__ == "__main__":
    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print("{}: {}".format(sha, author_name))
    except requests.exceptions.RequestException as e:
        print("Request error: {}".format(e))
    except ValueError:
        print("Not a valid JSON response")

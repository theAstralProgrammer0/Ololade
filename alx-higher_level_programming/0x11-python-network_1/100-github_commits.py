#!/usr/bin/python3
"""This module lists the top 10 commits on GitHub repo based on recency.
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2],
                                                              argv[1]
                                                              )

    req = get(url)
    print(req)
    commits = req.json()
    print(commits)
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),
                                  commits[i].get("commit")
                                  .get("author")
                                  .get("name")
                                  ))
    except Exception:
        pass

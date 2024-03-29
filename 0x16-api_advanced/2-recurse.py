#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should
return None.
"""i

import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles or None"""
    if type(subreddit) is list:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        return (None)
    req = req.json()
    if "data" in req:
        data = req.get("data")
        if not data.get("children"):
            return (hot_list)
        for post in data.get("children"):
            hot_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (hot_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)
    else:
        return (None)

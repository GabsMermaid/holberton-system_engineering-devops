#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given, the function should return 0."""

import requests

def number_of_subscribers(subreddit):
    """ Returns number of subs """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    header = {'User-Agent': 'CustomClient/1.0'}
    req = requests.get(url, headers=header, allow_redirects=False)

    if req.status_code != 200:
        return (0)
    req = req.json()

    if "data" in req:
        return (req.get("data").get("subscribers"))
    else:
        return (0)




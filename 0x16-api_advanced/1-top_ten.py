#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """return number of subcribers"""
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit),
                     headers={'User-agent': 'my-integration/1, 2, 3'},
                     allow_redirects=False)
    print(r.json()['kind'])
    try:
        val = r.json()['data']['subscribers']
    except:
        val = 0
    print(val)
    return val

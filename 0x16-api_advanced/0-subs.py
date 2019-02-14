#!/usr/bin/python3
"""Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """return number of subcribers"""
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit),
                     headers={'User-agent': 'my-integration/1'},
                     allow_redirects=False)
    val = r.json()['data']['subscribers']
    return val

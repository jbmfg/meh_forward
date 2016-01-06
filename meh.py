#!/usr/bin/python
__author__ = 'Benny'
import urllib.request
import ssl
import json


def meh():
    resp = urllib.request.urlopen('https://api.meh.com/1/current.json?apikey=') # Enter your api_key here
    data = resp.read().decode('utf-8')
    obj = json.loads(data)
    item = obj['deal']['title']
    item_url = obj['deal']['topic']['url']
    return item, item_url


def push(item, item_url):
    token = '' # Enter your api_key here
    user_key = 'XXXXXXXXXX'
    message = item+'\n'+item_url
    post_data = 'token='+token+'&user='+user_key+'&message='+message
    post_data = str.encode(post_data)
    push_url = 'https://api.pushover.net/1/messages.json'
    pushover = urllib.request.urlopen(push_url, data=post_data)
    return pushover


def main():
    meh_response = meh()
    item = meh_response[0]
    item_url = meh_response[1]
    push(item, item_url)

if __name__ == '__main__':
    main()

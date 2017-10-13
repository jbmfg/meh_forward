#!/usr/bin/python
__author__ = 'Benny'
import urllib.request
import ssl
import json


def getConfigs():
    with open("config.json", "r") as f:
        params = json.load(f)
    f.close()
    return params

def meh(params):
    meh_api = params["meh_api"]
    resp = urllib.request.urlopen('https://api.meh.com/1/current.json?apikey=' + meh_api) # Enter your api_key here
    data = resp.read().decode('utf-8')
    obj = json.loads(data)
    item = obj['deal']['title']
    item_url = obj['deal']['topic']['url']
    return item, item_url


def push(item, item_url, params):
    token = params["pushover_api"]
    user_key = params["pushover_user"]
    message = item+'\n'+item_url
    post_data = 'token='+token+'&user='+user_key+'&message='+message
    post_data = str.encode(post_data)
    push_url = 'https://api.pushover.net/1/messages.json'
    pushover = urllib.request.urlopen(push_url, data=post_data)
    return pushover


def main():
    params = getConfigs()
    meh_response = meh(params)
    item = meh_response[0]
    item_url = meh_response[1]
    push(item, item_url, params)

if __name__ == '__main__':
    main()

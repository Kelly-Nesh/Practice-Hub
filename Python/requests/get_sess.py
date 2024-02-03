#!/usr/bin/python3
"""Get request with session"""
import requests
sess = requests.Session()

sess.auth = ('user', 'pass')

sess.headers.update({'X-Sent-By': 'Nesh'})

res = sess.get("https://httpbin.org/cookies/set/sessioncookie/123456789")
print(res.text)

res1 = sess.get('https://httpbin.org/headers', headers=({"X-sending": 'nesh'}))
#session gets reused
print(res1.text)


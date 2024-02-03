#!/usr/bin/python3
"""Get request with requests module"""
import requests

r = requests.get("https://api.github.com/users")

print("url: {}\headers: {}\nstatus_code: {}\nencoding: {}\n\
      elapsed: {}\nreason: {}".format(r.url, r.headers,
        r.status_code, r.encoding, r.elapsed, r.reason))

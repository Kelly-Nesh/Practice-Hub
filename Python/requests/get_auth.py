#!/usr/bin/python3
"""Get request with authentication"""
import requests
from requests.auth import HTTPBasicAuth

res = requests.get("https://api.github.com/user",auth=HTTPBasicAuth('user', 'pass'))
print(res.status_code, res.request.headers)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " city")
    exit(1)

api_url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = 'XXXXXXXXXXX'
r = requests.get(url=api_url, params=dict(q=sys.argv[1], APPID=api_key, units='metric'))

weather = r.content.strip()
data = json.loads(weather)

temp = str(data['main']['temp'])
print(temp + " " + u"\u2103")


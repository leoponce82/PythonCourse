# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:25:00 2019

@author: CEC
"""

import urllib.parse
import requests

main_api= "https://www.mapquestapi.com/directions/v2/route?"
orig="Quito"
dest="Piñas, El Oro"
key="ZpPbqgNsqD1epitsjSai9d0zFtPzziIE"
url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})

json_data=requests.get(url).json()
print(json_data)

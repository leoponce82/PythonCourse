# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:50:24 2019

@author: CEC
"""

import urllib.parse
import requests

main_api= "https://www.mapquestapi.com/directions/v2/route?"
#orig="Quito"
#dest="Piñas, El Oro"
key="ZpPbqgNsqD1epitsjSai9d0zFtPzziIE"
#url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
while True:
    orig=input("Origen: ")
    dest=input("Destino: ")
    url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})


    json_data=requests.get(url).json()
    print("URL: "+(url))
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]
    
    if json_status==0:
        print("API Status: " +str(json_status)+"= A successful route call.\n")
        


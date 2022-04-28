#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='This is Braydens JSON Script, just enter an ip')

parser.add_argument('-ipaddress', '--', dest='ip', type=str, required=True, help='Enter an IP Address')

args = parser.parse_args()
#print(ip)

import sys
import requests
import json

url = f"http://ipinfo.io/{args.ip}/json"

myJson= requests.get(url)

myDict = json.loads(myJson.text)
#print(type(myDict))
for key in myDict.keys():
    print(f"{key: <8}:{myDict[key]: <8}")

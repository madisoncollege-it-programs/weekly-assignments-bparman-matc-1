#!/usr/bin/env python3
#Brayden Parman's Script: Working with dictionaries

myIpDict = {"server1.testlab.com" : "192.168.1.10", "server2.testlab.com" : "192.168.1.11", "server3.testlab.com" : "192.168.1.12", "server4.testlab.com" : "192.168.1.13", "server5.testlab.com" : "192.168.1.14", "server6.testlab.com" : "192.168.1.15"}

print(myIpDict.keys())

print(myIpDict.values())

print(myIpDict.items())

myIpDict['server7.testlab.com'] = '192.168.1.16'
myIpDict['server8.testlab.com'] = '192.168.1.17'

print("server2.testlab.com" in myIpDict.keys())
print("server10.testlab.com" in myIpDict.keys())


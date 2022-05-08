#!/usr/bin/env python3

import argparse
import sys
import requests, bs4
import json
import socket

parser = argparse.ArgumentParser(description='Enter an IP Address and Function number 1-5')

parser.add_argument('-i', '--ipaddress', dest='ip', type=str, required=True, help='Enter an IP Address')
parser.add_argument('-f', '--function', dest='func_numb', type=int, required=True, help='Enter the number corresponding to the function you want, 1-5')

args = parser.parse_args()

URL = f"http://{args.ip}/q{args.func_numb}"
IP = args.ip
#response = requests.get(URL)
#print(response.text)

print("Name: Brayden Parman")
print(f"{URL}")
#print(f"{IP}")
def get_response(URL):
    #print("this is my get response function")
    response = requests.get(URL)
    print(f"ANSWER: {response.text}")

def parse_string(URL):
    response = requests.get(URL)
    myHTML = bs4.BeautifulSoup(response.text,features="html.parser")
    #print(type(myHTML.h3.text))
    #print(myHTML.h3.text)
    myString = myHTML.h3.text
    print(f"ANSWER: {myString[4::2]} Brayden")
    #print(f"{response.text}")

def parse_header(URL):
    response = requests.get(URL)
    print(f"ANSWER: {response.headers['MATC-HEADER']}")
    #print(f"{response.text}")

def parse_json(URL):
    response = requests.get(URL)
    #print(response.headers)
    #print(type(json.loads(response.text)))
    #print(json.loads(response.text))
    myDict = json.loads(response.text)
    #print(json.dumps(myDict,indent=4))
    #print(myDict)
    myDict2 = myDict['Music And Books'][3]['publish_info']
    #myDict2 = myDict['Music And Books']
    #print(myDict2)
    print(f"ANSWER: {myDict2.get('publisher')}")
    #for x in myDict2.values():
        #print(x)

def socket_client(IP):
    #RHOST = URL
    RHOST = IP
    #RHOST = '172.31.29.253'
    RPORTS = range(5000,6000)
    SND_DATA = 'secret'
    myTimeout = 2

    #print(f"{RHOST}")
    for RPORT in RPORTS:
        C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        C_SOCK.settimeout(myTimeout)
        try:
            C_SOCK.connect((RHOST,RPORT))
            #print(f"Connection State: {RPORT}::Port Open")
            C_SOCK.send(bytearray(SND_DATA, 'utf8'))

            RCV_DATA = C_SOCK.recv(1024)
            print(f"ANSWER: {RCV_DATA.decode('utf-8')}")
            C_SOCK.close()
        except socket.error as e:
            #print(f"Connection State: {RPORT}::{e}")
            C_SOCK.close()

if args.func_numb == int("1"):
    get_response(URL)
elif args.func_numb == int("2"):
    parse_string(URL)
elif args.func_numb == int("3"):
    parse_header(URL)
elif args.func_numb == int("4"):
    parse_json(URL)
elif args.func_numb == int("5"):
    socket_client(IP)
else:
    print("Wrong Answer")

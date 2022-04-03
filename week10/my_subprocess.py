#!/usr/bin/env python3

import subprocess

myProc = subprocess.run(['ps', '-a', '-x', '-c', '-o', 'command'],stdout=subprocess.PIPE)

myProcString = myProc.stdout.decode()
#print(myProcString)
myProcList = myProc.stdout.decode().split('\n')
#print(myProcString)

for x in myProcList:
    print(x)

print(len(myProcList[1::]))


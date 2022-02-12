#!/usr/bin/env python3

varString = "Here is a nice string to slice"
varList = [ "Here", "is", "a", "nice", "list", "to", "slice"]

print(varString[3::])
print(varString[0:3:1])
print(varString[3:12:1])
print(varString[0::2])
print(varString[::-1])

print(varList[::-1])
print(varList[2::-1])
print(varList[::3])
print(varList[1::])

for element in varString:
    print(element)
for element in varList:
    print(element)

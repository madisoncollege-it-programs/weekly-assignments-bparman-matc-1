#!/usr/bin/env python3

#Brayden Parman's File Data Interactions Script

#Q1
hFile = open("/etc/passwd",'r')
strPasswd = hFile.read()
print(len(strPasswd))
print("The len() function counted the number of characters in this file")
print("You would use the read() function when you want the file read in a single string")
hFile.close()

#Q2
hFile = open("/etc/passwd",'r')
lstPasswd = hFile.readlines()
print(len(lstPasswd))
print("The len() function counted the number of lines in this file")
print("You would use readlines() when you want read all lines of a file and store it in a list")
hFile.close()

#Q3
hFile = open("/etc/passwd",'r')
count = 0
for line in hFile:
    #print(f"{hFile.readline()}", end='')
    count += len(line)
print(f"The lenght of this file is: {count}")
print("The readline and loop technique would really only be used to find the length of a really large file or data set")
hFile.close()

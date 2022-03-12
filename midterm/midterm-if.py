#!/usr/bin/env python3

print("Name: Brayden Parman")

Counter = 1
Total = 0
with open("Midterm-if.txt","r") as hFile:
    for line in hFile:
        if "gmeach18@ed.gov" in line:
            print(f"{Counter}")
            Total += int(Counter)
            #print(f"The Total is: {Total}")
        elif "248.253.63.149" in line:
            print(f"{Counter}")
            Total += int(Counter)
            #print(f"The Total is: {Total}")
        #Counter += 1
        elif "Whiteland" in line:
            print(f"{Counter}")
            Total += int(Counter)
        elif "80.222.19.190"in line:
            print(f"{Counter}")
            Total += int(Counter)
        elif "Kayley" in line:
            print(f"{Counter}")
            Total += int(Counter)
        elif "dcassyqw@microsoft.com" in line:
            print(f"{Counter}")
            Total += int(Counter)
            print(f"The Total is: {Total}")
        Counter += 1

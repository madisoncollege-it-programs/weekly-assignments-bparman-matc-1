#!/usr/bin/env python3
print("Name: Brayden Parman")

#opens file in read mode as hFile
with open ("slicing-file.txt","r") as hFile:
    #readlines() reads file into a list named list_slicing_file
    list_slicing_file=hFile.readlines()
    print(list_slicing_file)
    print(len(list_slicing_file))
    #creating variable A for question 4a
    A = list_slicing_file[24]
    print(f"{A}")
    #creating variable B for question 4b
    B = list_slicing_file[2:5:1]
    print(f"{B}")
    #creating variable C for question 4c
    C = list_slicing_file[-10::2]
    print(f"{C}")
    #creating variable D for question 4d
    D = list_slicing_file[10:13:]
    print(f"{D}")
    #creating variable E for question 4e
    E = list_slicing_file[8:5:-1]
    print(f"{E}")
    #putting lists into string
    #myString = ""
    #myString = myString.join(A)
#for x in B:
    #myString = ','.join(B)
    #for z in C:
        #myString = ','.join(C)
    #myString = myString.join(A)
    #myString = myString.join(B)
    #myString = myString.join(C)
    #myString = myString.join(D)
    #myString = myString.join(E)
    print(myString)

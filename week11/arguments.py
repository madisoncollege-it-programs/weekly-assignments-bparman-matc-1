#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='This is a Brayden Parman script')

parser.add_argument('-m', dest='BASIC', help='Enter some text')
parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]', type=int, required=True, help='<required> Enter a simple Integer')
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', type=float, required=False, help='Enter a simple Float')
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', type=str, required=False, help='Enter a simple String')
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true', required=False, help='Toggle from default False to True')
parser.add_argument('-f', '--set-false', dest='bool_f', default=True, action='store_false', required=False, help='Toggle from default True to False')
parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')

input_results = parser.parse_args()
print(input_results)

args = parser.parse_args()

print("The value of your '-i'  arg is: " + str(args.varInteger))
print("The value of your '-d' arg is: " + str(args.varFloat))
print("The value of your '-s' arg is: " + str(args.varString))

print("=== Here is the List ===")
print(args.varList)
for arg in args.varList:
    print(arg)



#!/bin/python3

import sys

input = sys.stdin.readline
S = input().strip()
try:
    S = int(S)
except:
    S = "Bad String"
print(S)

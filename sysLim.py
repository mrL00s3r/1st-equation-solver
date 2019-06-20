#!/bin/bash/env python
#   program to calculate linear systems
#   platos 06/04/19

term = input("Write the number of terms: \n")
unk = input("Write the number of unknowns: \n")
indepentent = input("Write the independent terms devided by ',': \n")
t = int(term)
u = int(unk)
token = [t * u] #determine the size of 'token'
token = indepentent.split(",")
m = [t],[u]
if len(token) == len(m):
    try:    #xgh
        for i in range(0, t):
            for j in range(0, u):
                m = list(input())

        for i in range(0, t):
            for j in range(0, u):
                print(list(m))
    except:
        print("FUDEU")
else:
    print("ERROR")

# TODO: make functions to determine if the system 
# impossible, possible, ideterminant.


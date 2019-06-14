#!/bin/bash/env python
#   program to calculate linear systems
#   CRAMER
#   platos 06/04/19

t = input("Write the number of therms:\n")
token = [2]
token = t.split("x")
matrix = [[int(token[0])],[int(token[1])]]

print("the number of unknowns is: "+token[1])
print("the number of lines is: "+token[0])
print("Write the numbers: \n")
for j in range(0, int(token[0])):
    b = input()


print("Write the independent terms")
for i in range(0, int(token[0])):
    a = input()
# 0 = unsolved, 1 = solved.
# TODO: make functions to determine if the system is impossible, possible, ideterminant. '0'
#

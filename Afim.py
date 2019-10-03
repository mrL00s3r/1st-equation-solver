# under MIT license
# program to solve 1st eqations
# Made by mr_L00s3r at: 10/03/2019
#TODO: make a better code, do not use all of this 'IF's'

import re

x = 0
angularCoefficient = 0
linearCoefficient = 0 
variableValues = [2]
variables = input('Write the value of the variables (divided by comma): ')
operation = input('Write the arithmetic operator between them: ')
variableValues = str(variables).split(', ')
if 'x' in str(variableValues[0]):
    angularCoefficient = int(re.search(r'\d+', variableValues[0]).group())
    linearCoefficient = int(re.search(r'\d+', variableValues[1]).group())
elif 'x' in str(variableValues[1]):
    angularCoefficient = int(re.search(r'\d+', variableValues[1]).group())
    linearCoefficient = int(re.search(r'\d+', variableValues[0]).group())
if str(operation) == '*':
    x = angularCoefficient * linearCoefficient
    print(x)
if 'x' in str(variableValues[1]) and operation == '-':
    x = -linearCoefficient/angularCoefficient
    print(x)
if 'x' in str(variableValues[0]) and operation == '-':
    x = linearCoefficient/angularCoefficient
    print(x)
interval = input('write the interval that you want (divided by comma): ')
token = [2]
token = str(interval).split(', ')
for i in range(int(token[0]), int(token[1])+1):
    print(x * i)

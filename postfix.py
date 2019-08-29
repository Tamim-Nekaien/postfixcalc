
"""
import sys
#input = sys.stdin.read()

tokens = input("Enter numbers, loser: ")
#if user_input.isdigit() == True
stack = []
operators = {'+': lambda x,y: x+y,\
            '-': lambda x,y: x-y,\
            '*': lambda x,y: x*y,\
            '/': lambda x,y: x//y,}
for s in tokens:
    if s in operators:
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        stack.append(operators[s](op1, op2))

    else:
        exit(0)
"""


import sys

input = sys.stdin.read()

#input = input("Enter: ")

stack = input.split()
new_stack = []

for i in stack:

    if i.lstrip('-+').isdigit() == True:

        new_stack.append(int(i))

    if i == '+':

        x = new_stack.pop()
        y = new_stack.pop()
        new_stack.append(x + y)

    if i == '-':
        x = new_stack.pop()
        y = new_stack.pop()
        new_stack.append(y-x)

    if i == '*':
        x = new_stack.pop()
        y = new_stack.pop()
        new_stack.append(x*y)

    if i == '/':
        x = new_stack.pop()
        y = new_stack.pop()
        new_stack.append(y // x)

print (new_stack.pop())

"""
input = input("Enter numbers")
stack = []
stack = input.split()
operands = {'+', '-', '*', '/'}
if operands = '+':
    stack.pop()
"""

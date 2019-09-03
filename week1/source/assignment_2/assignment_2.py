#!/usr/bin/python3

"""
Assignment 2
Write a program that uses a while loop that runs 10 times. The program should
have a variable loop = 10 and a variable index = 0.
Every time the index is even the program should output the number. The operand to find out if a number is even called modulo and is represented by the % symbol. Use google to find out how to use the module operator.
The output of the function should be:
0 2 4 6 8
"""

loop = 10
index = 0

while index<10:
    if index%2 == 0:
        print(index)
    index += 1





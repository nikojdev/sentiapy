#!/usr/bin/python3

"""
Assignment 3
Write three functions:
sum, with two parameters (a and b), which returns the sum of a and b.
div, with two parameters (a and b), which returns the result of a divided by b.
times_three, with one parameter (a), which returns a multiplied by 3.
Then write a program that contains three variables: x = 3, y = 5, z = 2. Then it should use the sum function with parameters x and y. Store the result in a variable. Then run the div function with that variable and z. Store the result in another variable.
Then run times_three on that variable and print the result. The output should be:
12.0
"""

def sum1(a,b):
    result = a+b
    return result


def div(a,b):
    result = a/b
    return result


def times_three(a):
    result = a*3
    return result


x = 3
y = 5
z = 2

result_sum = sum1(x,y)
result_div = div(result_sum,z)
result_final = times_three(result_div)

print(result_final)



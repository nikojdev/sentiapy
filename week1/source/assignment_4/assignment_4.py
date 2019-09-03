#!/usr/bin/python3

"""
Assignment 4

Initialize a list with 20 numbers like so: my_list = list(range(0, 20)) Then reverse the list and store the result in a new variable. Make sure the original my_list variable remains unchanged.
Then take the first 5 numbers and the last 5 numbers of the reversed list and store them in a new variable. Print that variable. The result should be:
[19, 18, 17, 16, 15, 4, 3, 2, 1, 0]
Hint: you can concatenate two lists with the + operator. For example:
print([1, 2] + [3, 4]) # outputs [1, 2, 3, 4]
"""

my_list = list(range(0, 20))
reversed_list = my_list[::-1] # reversing the list
result_list = reversed_list[0:5] + reversed_list[-5:] # concatenate the lists

print(result_list)

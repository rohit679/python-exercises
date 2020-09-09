"""
Q. Write a Python program to take an odd integer as an input.
Print the following pattern, where input integer will be the number
of rows of the pattern.

Input:
9

Output:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

Sloution:-
"""
number = int(input())
for row_index in range(number + 1):
    if row_index <= (number // 2 + 1) :
        for col_index in range(row_index):
            print ('* ', end="")
    else:
        for col_index in range(number - row_index + 1):
            print('* ', end="")
    print('')

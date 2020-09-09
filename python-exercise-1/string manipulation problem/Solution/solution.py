"""
Q. Write a python program to take a string as an input.
Check the following into the string -
    - Print True If all charaters are in uppercase or False
    - Print True If all charaters are in lowercase or False
    - Convert all characters of the string uppercase & Print it
    - Convert all characters of the string lowercase & Print it
    - Concatinate uppercase & lowercase string with "*" & print it

Input:
India is Great

Output:
False
False
INDIA IS GREAT
india is great
INDIA IS GREAT * india is great
"""

sample_string = input()
print(sample_string.isupper())
print(sample_string.islower())
upper = sample_string.upper()
lower = sample_string.lower()
print(upper)
print(lower)
print(upper+" * "+lower)

"""
Q. Write a Python program to take any number of input elements into a list at runtime by user.
Create a dictionary to show the count of each & every unique element in the list. Print
the maximum key & maximum value in the dictionary.

Input:
11 45 8 11 23 45 23 45 89 30 89 23 89

Output:
Printing maximum key in the dictionary: 89
Printing maximum value in the dictionary: 3

Solution:-
"""

sampleList = [int(element) for element in input().split(' ')]
print("Original list ", sampleList)

result = dict()
unique_list = set(sampleList)
for item in unique_list:
    result[item] = sampleList.count(item)

print("Printing maximum key in the dictionary:",max(result.keys()))
print("Printing maximum value in the dictionary:",max(result.values()))
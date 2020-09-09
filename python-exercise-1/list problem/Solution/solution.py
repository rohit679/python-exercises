"""
Q. A list is given. Write a Python program to replace every even occurance of 0 by 10 into the list.
But if you get any 10 in list after that you will not make any change into the list.
sample_list = [0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12]

Output:
[0, 2, 10, 4, 0, 6, 10, 8, 0, 10, 0, 12]

Solution:-
"""

sample_list = [0, 2, 0, 4, 0, 6, 0, 8, 0, 10, 0, 12]
flag = False
for index in range(len(sample_list)):
    if sample_list[index] == 0:
        if flag:
            sample_list[index] = 10
            flag = False
        else:
            flag = True
    elif sample_list[index] == 10:
        break
print("Resultant list:", sample_list)
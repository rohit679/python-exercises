"""
Q. Write a python program to roll a dice & if it will generate 1 then game over,
otherwise add the generated number into a count variable. Repeat the game while
game over. After game over, print the score.

Solution:-
"""

import random
score = 0
dice = [1, 2, 3, 4, 5, 6]
while(1):
    number = random.choice(dice)
    print("generated number",number)
    if number==1:
        break
    score += number
print("GAME OVER:(")
print("Your score is:{}".format(score))
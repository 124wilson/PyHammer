# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:53:42 2022

@author: Mikuś
"""
from random import randint

def roll_dice(dice):
    for die in dice:
        yield(randint(1, die))

'''
#to remember how to use dice roll function
z = [6, 8, 9]
roll = roll_dice(z)
print(*list(roll))
'''

def atr_roll(atribute, dice=100):
    roll = (roll_dice([dice]))
    if(atribute>=next(roll)):
        print('sucess')
    else:
        print('fail')

    
        
    
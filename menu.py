# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:56:08 2017

@author: Brian Bentley
"""


# Start of the Gloriana Project

import sys
sys.path.append("D:/Projects/Workspace/Gloriana")

inputCheck = False

# Prints out the menu.
print("Welcome to Gloriana. Choose something from the menu:")
print("(C)reate Character: ")
print("(L)oad Character: ")
print("(R)oll Dice: ")
print("(Q)uit Gloriana: ")
#print(dice_roller.rollDie10)

# Allows user input and checks if it is valid.
while inputCheck == False:
    menuInput = input("Welcome to Gloriana. Choose something from the menu: ")
    if menuInput == 'c' or menuInput == 'C':
        inputCheck = True
    elif menuInput == 'l' or menuInput == 'L':
        inputCheck = True
    elif menuInput == 'r' or menuInput == 'R':
        inputCheck = True
    elif menuInput == 'q' or menuInput == 'Q':
        inputCheck = True
    else:
        print("You have entered an incorrect menu option. Please enter the ") 
        print ("first letter of your menu option. ")
        
    
    

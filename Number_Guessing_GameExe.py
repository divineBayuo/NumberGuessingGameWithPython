# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:52:42 2021

@author: Divine
"""

#putting both programs together
#importing required libs
 
import tkinter as tk 
import random 
import math 

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

#making the game code a function
def NumberGuessingGame ():
    #take the inputs from the user
    lowerBound = int(input("Enter lower bound:- ")) #lower bound 
    upperBound = int(input("Enter upper bound:- ")) #upper bound 

    #generating random figure between the lower and upper bound 
    x = random.randint(lowerBound,upperBound)
    print("\n\tYou have only chances ",
          round(math.log(upperBound-lowerBound+1,2)),
          "to guess the integer!\n")
 
    #initializing the number of guesses
    count = 0
    #min number of guesses depends on the range given
    while count <= round(math.log(upperBound-lowerBound+1,2)):
        count = count + 1
    
        #taking the player's guess
        guess = int(input("Guess the number:- "))
    
        #test a condition 
        if x == guess:
            print("\nCongratulations! You did it in ",count," tries.")
            #once the guess is correct, the loop will break
            break 
        elif x > guess: 
            print("\nGuessed too small!")
        elif x < guess:
            print("\nGuessed too high!")

    #if guessing is more than the required guesses, give the following 
    if count > round(math.log(upperBound-lowerBound+1,2)):
        print("\nThe number is %d" %x)
        print("\tBetter luck next time!")
        
button1 = tk.Button(text='Start!',command = NumberGuessingGame, bg='green', fg='white')
canvas1.create_window(150,150,window=button1)

#button2 = tk.Button(text='Play Again',command = NumberGuessingGame, bg='green', fg='white')
#canvas1.create_window(150,150,window=button2)
        
root.mainloop()
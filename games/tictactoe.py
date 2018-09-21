import os
import time
import random

#Define the board
board = [" ", " ", " "," ", " ", " ", " ", " ", " ", " "]

#print header
def print_header():
    print """
 _____ _ ____    _____ ____ ____    _____ ____ _____
/__ __/ /   _\  /__ __/  _ /   _\  /__ __/  _ /  __/
  / \ | |  / _____/ \ | / \|  / _____/ \ | / \|  \  
  | | | |  \_\____| | | |-||  \_\____| | | \_/|  /_ 
  \_/ \_\____/    \_/ \_/ \\____/    \_/ \____\____/
                                                    
"""

#define board 
def print_board():
    print "   |   |   "
    print " "+board[1]+" | "+board[2]+" | "+board[3]+" "
    print "   |   |   "
    print "---|---|---"
    print " "+board[4]+" | "+board[5]+" | "+board[6]+" "
    print "   |   |   "
    print "---|---|---"
    print "   |   |   "
    print " "+board[7]+" | "+board[8]+" | "+board[9]+" "
    print "   |   |   "

while True:
    os.system("clear")
    print_header()
    print_board()

    
    choice=raw_input("Please choose an empty space for X, ")
    choice=int(choice)

    if board[choice] == " ":
        board[choice] = "X"
    else:
        print "Sorry the space is not empty"
    time.sleep(1)         
                                                    
                                                    



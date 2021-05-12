import getpass
import sys
import colorama
from colorama import Fore, Style, Back
#'abhinav-gupta' is the password

password = getpass.getpass(prompt = "Enter the password:")

if password == 'abhinav-gupta':
    print(Back.WHITE + Fore.GREEN + Style.BRIGHT + 'Password Accepted' + Style.RESET_ALL + "\n")
else:
    print(Back.WHITE + Fore.RED + Style.BRIGHT + 'Incorrect Password' + Style.RESET_ALL + "\n")
    sys.exit()

def display_board(board):
    print('-------')
    print('|'+board[7]+'|'+board[8]+'|'+board[9]+'|')
    print('|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
    print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|')
    print('-------')
    
test2_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def player_input():
    check = 'NONE'
    ch = False    
        
    while check not in ['1','2','3','4','5','6','7','8','9'] and ch == False:
        check = input('Enter an index (1-9): ')
        if check.isdigit() == False:
            print('Invalid Input!')
            continue            
        if check.isdigit() == True and check in ['1','2','3','4','5','6','7','8','9']:
            ch = True
        else:
            print("Enter a number only between 1 and 9!")
            
    return int(check)
    
def place_marker(board, marker, position):
    board[position] = marker
    return board
    
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False
        
import random

def choose_first():
    
    x = random.randint(1,2)
    return x
    
    
def space_check(board, position):
    if 'X' == board[position] or 'O' == board[position]:
        return 'OCCUPIED'
    else:
        return 'AVAILABLE'
        
def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True
        
def replay():
    flag = False
    check = 0
    while flag == False:
        ans = input('Do you wish to play again? (Yes or No)')
        ans = ans.upper()
        if ans == 'NO':
            flag = True
            check = 1
        elif ans == 'YES':
            print('\n')
            flag = True
        else:
            print('Invalid Input! Enter Yes or No only.\n')
    return check
    
c = False
game_on = True
wincheck = None
mark1 = ' '
mark2 = ' '
while c == False:
    print('Welcome to Tic Tac Toe!\n')
    choice = choose_first()
    if choice%2 == 0:
        mark1 = 'X'
    else:
        mark1 = 'O'
    print('1st player will play with {}'.format(mark1))
    if mark1 == 'O':
        mark2 = 'X'
        print('2nd player will play with X')
    else:
        mark2 = 'O'
        print('2nd player will play with O')
    print('\n')
    display_board(test2_board)
    while game_on == True:
        
        print("\nPlayer 1's Turn\n") #Player 1
        pos = player_input()
        avai = space_check(test2_board,pos)
        print(avai)
        if avai == 'OCCUPIED':
            print("Enter Again!\n")
            continue
        else:
            pass
        test2_board = place_marker(test2_board,mark1,pos)
        display_board(test2_board)
        wincheck = win_check(test2_board,mark1)
        if wincheck == True:
            print('Congratulations! Player 1 has won the game.')
            break
        if full_board_check(test2_board) == True:
            print('Board is Full!\n')
            break
            
        
        print("\nPlayer 2's Turn\n") #Player 2
        pos = player_input()
        avai = space_check(test2_board,pos)
        print(avai)
        if avai == 'OCCUPIED':
            print("Enter Again!\n")
            continue
        else:
            pass
        test2_board = place_marker(test2_board,mark2,pos)
        display_board(test2_board)
        wincheck = win_check(test2_board,mark2)
        if wincheck == True:
            print('Congratulations! Player 2 has won the game.')
            break
        if full_board_check(test2_board) == True:
            print('Board is Full!\n')
            break
            
            
    cc = replay()
    if cc == 1:
        c = True        
    else:
        test2_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

from math import dist
import random


def display(board):
    print("_  0  1  2")
    for i in range(3):
        print(i,end="  ")
        for j in range(3):
            print(board[i][j],end="  ")
        print("")

def check_full(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]==''):return False
    return True


def check_won(board):
    #row:
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2]!=''):return True
        if(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i]!=''):return True
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]!=''):return True
    if(board[0][2]==board[1][1]and board[1][1]==board[2][0] and board[2][0]!=''):return True
    return False



def main():
    board=[['','',''],['','',''],['','','']]
    print("You are X and computer is O")
    display(board)

 

    for i in range(9):
        if(check_full(board)):
            print("Tie!")
            exit()
        if(i%2==0):
            row=int(input("Enter row:"))
            col=int(input("Enter col:"))
            while(board[row][col]!=''):
                print("Invalid ..enter again:")
                row=int(input("Enter row:"))
                col=int(input("Enter col:"))
            board[row][col]='X'
            display(board)
            if(check_won(board)):
                print("You WON!!!")
                exit()
        else:
            row=random.randint(0,2)
            col=random.randint(0,2)
            while(board[row][col]!=''):
                row=random.randint(0,2)
                col=random.randint(0,2)
            board[row][col]='O'
            display(board)
            if(check_won(board)):
                print("You lost!")
                exit()
main()
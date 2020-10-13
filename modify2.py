import numpy as np
import pygame
import sys
import math
import time
from pygame import mixer
mixer.init()


BLUE = (0,0,255)
BLACK = (0,0,0)
RED =(255,0,0)
YELLOW =(255,255,0)
GREY =(169, 169, 169)

ROW_COUNT = 6
COL_COUNT = 7

mixer.music.load('C:\\Users\\Dipak Acharya\\Downloads\\sound.mp3')
mixer.music.play(3)

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, col, row, piece):
    board[row][col] = piece
  
def is_valid_location(board, col):
    return board[5][col] == 0
    pass
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)

def winning_move(board, piece):
    #checking horizental palaces for win
    for c in range (COL_COUNT-3):
        for r in range (ROW_COUNT):
            if board[r][c] ==piece and board[r][c+1] ==piece and board[r][c+2] ==piece and board[r][c+3] ==piece:
                return True
#checking for vertical location if win
    for c in range (COL_COUNT):
        for r in range (ROW_COUNT-3):
            if board[r][c] ==piece and board[r+1][c] ==piece and board[r+2][c] ==piece and board[r+3][c] ==piece:
                return True


#checking posative diagonals for win
    for c in range (COL_COUNT-3):
        for r in range (ROW_COUNT-3):
            if board[r][c] ==piece and board[r+1][c+1] ==piece and board[r+2][c+2] ==piece and board[r+3][c+3] ==piece:
                return True

#Checking for negative diagonal win
    for c in range (COL_COUNT-3):
        for r in range (3,ROW_COUNT):
            if board[r][c] ==piece and board[r-1][c+1] ==piece and board[r-2][c+2] ==piece and board[r-3][c+3] ==piece:
                return True


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
                
            pygame.draw.circle(screen, BLACK,(int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)),RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED,(int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)),RADIUS)

            elif board[r][c] == 2:
                
                pygame.draw.circle(screen, YELLOW,(int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)),RADIUS)

            pygame.display.update()




def reset_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.circle(screen, BLACK,(int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)),RADIUS)
            board[r][c]=0
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK,(int(c*SQUARE_SIZE+SQUARE_SIZE/2), height-int(r*SQUARE_SIZE+SQUARE_SIZE/2)),RADIUS)

      


dis_width = 1000
dis_height = 1000

dis = pygame.display.set_mode((dis_width, dis_height))


pygame.init()
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2-5)
width = COL_COUNT * SQUARE_SIZE
height = ROW_COUNT * SQUARE_SIZE
size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


myfont = pygame.font.SysFont("monospace" ,75)
myfont1 = pygame.font.SysFont("monospace" ,25)
def loop():
    game_over = False
    game_close = False
    turn = 0
    SQUARE_SIZE = 100
    RADIUS = int(SQUARE_SIZE/2-5)
    width = COL_COUNT * SQUARE_SIZE
    height = ROW_COUNT * SQUARE_SIZE
    size = (width, height)
    reset_board(board)
    
    while not game_over:
        while game_close == True:
            
        
        #holding display to show a winner for instant
            pygame.time.delay(900)    
            


#Creating a wating display            
            dis.fill(GREY)
            #displaying a message 
            label= myfont1.render("Game Over! Press C-Play Again or Q-Quit", 1 ,BLACK)
            screen.blit(label, (35,300))
            pygame.display.update()
                        
                    
                
            
            
            
            
            
            
            
            
 #pygame keyevents: type keydown
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
#Event to quit game if q button pressed
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
#Event to continue game if c botton pressed
                    if event.key == pygame.K_c:
                        draw_board(board)
#Resetting the board
                        reset_board(board)
#Running the loop if c is pressed
                        loop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
#Mouse hover event ball moving type 
            if event.type == pygame.MOUSEMOTION:

#Top black board display 
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))
                posx = event.pos[0]

#Player 1 turn displaying a RED ball moving animation type at top
                if turn ==0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE/2)), RADIUS)
#Player 2 turn displaying a YELLOW ball moving animation type at top
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), RADIUS)

                pygame.display.update()
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0,0, width, SQUARE_SIZE))


                
                #print(event.pos)
                #Ask for player 1 input
                    if turn ==0:
                        
                        posx= event.pos[0]
                        col = int(math.floor(posx/SQUARE_SIZE))
                        while col not in [0, 1, 2, 3, 4, 5, 6]:

                            #warning pop out 
                            col = int(input ("Invalid Entry ! Choose a position from 0-6:  "))

                   
                        if is_valid_location(board, col):
                            row = get_next_open_row (board, col)
                            drop_piece(board, col, row, 1)

                            if winning_move(board,1):

#Displaying the winner 
                                    label= myfont.render("Player 1 wins!!", 1 ,RED)
                                    screen.blit(label, (40,20))
                                    pygame.time.delay(900)

                                    game_close =True

                        
                #player 2 input session 
                    else:
                        posx= event.pos[0]
                        col = int(math.floor(posx/SQUARE_SIZE))
                        
                        
                            

                           
                        while col not in [0, 1, 2, 3, 4, 5, 6]:
                            col = int(input ("Invalid Entry ! Choose a position from 0-6:  "))
                            

                     
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, col, row, 2)

                            if winning_move(board,2):
                                label= myfont.render("Player 2 wins!!", 1 ,YELLOW)
                                screen.blit(label, (40,20))
                                pygame.time.delay(900)
                                game_close =True

                    print_board(board)
                    draw_board(board)
                    turn += 1
                    turn=turn%2
    pygame.quit()
    quit()


loop()
        
        
        
    


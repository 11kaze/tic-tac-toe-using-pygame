import pygame as pg,sys
from pygame.locals import *
import time
import random
from pygame import mixer

# These variables will be used globaly("means in more than one functions")
X_and_O = 'x'
winner = None
match_draw = False
width = 400
height = 400
score = {'x':0,'o':0}
game_counter = 0
white = (255, 255, 255)
line_color = (10,10,10)
# TicTacToe 3x3 table
Tic_Tac_Toe_table = [[None]*3,[None]*3,[None]*3]

# initialising the first window 
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic-Tac-Toe-game")

#loading the images of first screen, X and O.
opening = pg.image.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\img\opening_image.jpg')
img_of_X = pg.image.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\img\x_img.png')
img_of_O = pg.image.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\img\o_img.png')
winner_x = pg.image.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\img\winner_x.png')
winner_o = pg.image.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\img\winner_o.png')
#resizing of the loaded images
img_of_X = pg.transform.scale(img_of_X, (80,80))
img_of_O = pg.transform.scale(img_of_O, (80,80))
winner_x = pg.transform.scale(winner_x,(width,height+100))
winner_o = pg.transform.scale(winner_o,(width,height+100))
opening = pg.transform.scale(opening, (width, height+100))

def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    
    # Drawing vertical lines on board
    pg.draw.line(screen,line_color,(width/3,0),(width/3, height),9)
    pg.draw.line(screen,line_color,((2*width)/3,0),((2*width)/3, height),9)
    
    # Drawing horizontal lines on board
    pg.draw.line(screen,line_color,(0,height/3),(width, height/3),9)
    pg.draw.line(screen,line_color,(0,(2*height)/3),(width, (2*height)/3),7)
    draw_status()

def draw_status():
    global match_draw
    if winner is None:
        message = X_and_O.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
        mixer.music.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\sounds\winning.mp3')
        mixer.music.play()
    if match_draw:
        message = 'Game Draw!'
        mixer.music.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\sounds\match_draw.mp3')
        mixer.music.play()

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    text_score_x = font.render("X Wins: {}".format(score['x']), 1, (255, 255, 255))
    text_score_o = font.render("O Wins: {}".format(score['o']), 1, (255, 255, 255))
    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 400, 500))
    text_rect = text.get_rect(center=(width/2, 500-50))
    text_score_x_rect = text_score_x.get_rect(center=(70, 500-50))
    text_score_o_rect = text_score_o.get_rect(center=(70, 500-30))
    screen.blit(text_score_o, text_score_o_rect)
    screen.blit(text_score_x, text_score_x_rect)
    screen.blit(text, text_rect)
    if winner=='x':
        screen.blit(winner_x,(0,0))
        score['x'] += 1
    elif winner=='o':
        screen.blit(winner_o,(0,0))
        score['o'] += 1    
    pg.display.update()

def check_win():
    global Tic_Tac_Toe_table, winner,match_draw
    # check for winning rows
    for row in range (0,3):
        if ((Tic_Tac_Toe_table [row][0] == Tic_Tac_Toe_table[row][1] == Tic_Tac_Toe_table[row][2]) and(Tic_Tac_Toe_table [row][0] is not None)):
            # this row won
            winner = Tic_Tac_Toe_table[row][0]
            pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\
                              (width, (row + 1)*height/3 - height/6 ), 4)
            break
    # check for winning columns
    for col in range (0, 3):
        if (Tic_Tac_Toe_table[0][col] == Tic_Tac_Toe_table[1][col] == Tic_Tac_Toe_table[2][col]) and (Tic_Tac_Toe_table[0][col] is not None):
            # this column won
            winner = Tic_Tac_Toe_table[0][col]
            #draw winning line
            pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),((col + 1)* width/3 - width/6, height), 4)
            break
    # check for diagonal winners
    if (Tic_Tac_Toe_table[0][0] == Tic_Tac_Toe_table[1][1] == Tic_Tac_Toe_table[2][2]) and (Tic_Tac_Toe_table[0][0] is not None):
        # game won diagonally left to right
        winner = Tic_Tac_Toe_table[0][0]
        pg.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
    if (Tic_Tac_Toe_table[0][2] == Tic_Tac_Toe_table[1][1] == Tic_Tac_Toe_table[2][0]) and (Tic_Tac_Toe_table[0][2] is not None):
        # game won diagonally right to left
        winner = Tic_Tac_Toe_table[0][2]
        pg.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)
    if(all([all(row) for row in Tic_Tac_Toe_table]) and winner is None ):
        match_draw = True
    draw_status()

def drawXO(row,col):
    global Tic_Tac_Toe_table,X_and_O
    
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30
    if col==1:
        posy = 30
    if col==2:
        posy = height/3 + 30
    if col==3:
        posy = height/3*2 + 30
    Tic_Tac_Toe_table[row-1][col-1] = X_and_O
    if(X_and_O == 'x'):
        screen.blit(img_of_X,(posy,posx))
        mixer.music.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\sounds\x_sound.mp3')
        X_and_O= 'o'
    else:
        screen.blit(img_of_O,(posy,posx))
        mixer.music.load(r'C:\Users\pawan\Desktop\work\tic-tac-toe-using-pygame\sounds\o_sound.mp3')
        X_and_O= 'x'
    mixer.music.play()    
    pg.display.update()

# now we will get the position/coordinate of that part of screen where user have clicked
def userClick():
    #get coordinates of mouse click
    x,y = pg.mouse.get_pos()
    #print(x,y)
    #get column of mouse click (1-3)
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
    #get row of mouse click (1-3)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    #print(row,col)
    if(row and col and Tic_Tac_Toe_table[row-1][col-1] is None):
        global X_and_O
        #draw the x or o on screen
        drawXO(row,col)
        check_win()

#restart game
def reset_game():
    global Tic_Tac_Toe_table, winner,X_and_O, match_draw
    time.sleep(3)
    if X_and_O == 'x':
        X_and_O = 'x'
    else:
        X_and_O = 'o'     
    Tic_Tac_Toe_table = [[None]*3,[None]*3,[None]*3]
    match_draw = False
    winner=None
    game_opening()
    #print(score)

game_opening()
mixer.init()
mixer.music.set_volume(0.6)
while(True):
    
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # user clicked and then place an "X" or "O"
            userClick()
            if(winner or match_draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(15)
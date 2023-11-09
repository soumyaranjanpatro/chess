import pygame

#initialize pygame ,display screen and give timer
pygame.init()
screen=pygame.display.set_mode((640,640))
pygame.display.set_caption("MSK CHESS GAME")

font=pygame.font.Font("freesansbold.ttf",16)
mid_font=pygame.font.Font("freesansbold.ttf",32)
big_font=pygame.font.Font("freesansbold.ttf",48)

timer=pygame.time.Clock()
fps=60

#define the pieces
white_pieces=["rook","knight","bishop","king","queen","bishop","knight","rook",
              "pawn","pawn","pawn","pawn","pawn","pawn","pawn","pawn"]
white_positions=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                 (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
black_pieces=["rook","knight","bishop","king","queen","bishop","knight","rook",
              "pawn","pawn","pawn","pawn","pawn","pawn","pawn","pawn"]
black_positions=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                 (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]

turn=0
selection=100
valid_moves=[]

#pieces images
black_pawn=pygame.image.load("E:/code/python/Chess/images/blackpawn.png")
black_pawn=pygame.transform.scale(black_pawn,(64,64))
black_pawn_small=pygame.transform.scale(black_pawn,(36,36))
black_rook=pygame.image.load("E:/code/python/Chess/images/blackrook.png")
black_rook=pygame.transform.scale(black_rook,(64,64))
black_rook_small=pygame.transform.scale(black_rook,(36,36))
black_knight=pygame.image.load("E:/code/python/Chess/images/blackknight.png")
black_knight=pygame.transform.scale(black_knight,(64,64))
black_knight_small=pygame.transform.scale(black_knight,(36,36))
black_bishop=pygame.image.load("E:/code/python/Chess/images/blackbishop.png")
black_bishop=pygame.transform.scale(black_bishop,(64,64))
black_bishop_small=pygame.transform.scale(black_bishop,(36,36))
black_king=pygame.image.load("E:/code/python/Chess/images/blackking.png")
black_king=pygame.transform.scale(black_king,(64,64))
black_king_small=pygame.transform.scale(black_king,(36,36))
black_queen=pygame.image.load("E:/code/python/Chess/images/blackqueen.png")
black_queen=pygame.transform.scale(black_queen,(64,64))
black_queen_small=pygame.transform.scale(black_queen,(36,36))

white_pawn=pygame.image.load("E:/code/python/Chess/images/whitepawn.png")
white_pawn=pygame.transform.scale(white_pawn,(64,64))
white_pawn_small=pygame.transform.scale(white_pawn,(36,36))
white_rook=pygame.image.load("E:/code/python/Chess/images/whiterook.png")
white_rook=pygame.transform.scale(white_rook,(64,64))
white_rook_small=pygame.transform.scale(white_rook,(36,36))
white_knight=pygame.image.load("E:/code/python/Chess/images/whiteknight.png")
white_knight=pygame.transform.scale(white_knight,(64,64))
white_knight_small=pygame.transform.scale(white_knight,(36,36))
white_bishop=pygame.image.load("E:/code/python/Chess/images/whitebishop.png")
white_bishop=pygame.transform.scale(white_bishop,(64,64))
white_bishop_small=pygame.transform.scale(white_bishop,(36,36))
white_king=pygame.image.load("E:/code/python/Chess/images/whiteking.png")
white_king=pygame.transform.scale(white_king,(64,64))
white_king_small=pygame.transform.scale(white_king,(36,36))
white_queen=pygame.image.load("E:/code/python/Chess/images/whitequeen.png")
white_queen=pygame.transform.scale(white_queen,(64,64))
white_queen_small=pygame.transform.scale(white_queen,(36,36))

captured_white=[]
captured_black=[]

white_images=[white_pawn,white_rook,white_knight,white_bishop,white_king,white_queen]
white_images_small=[white_pawn_small,white_rook_small, white_knight_small,white_bishop_small,white_king_small,white_queen_small]
black_images=[black_pawn,black_rook,black_knight,black_bishop,black_king,black_queen]
black_images_small=[black_pawn_small,black_rook_small,black_knight_small,black_bishop_small,black_king_small,black_queen_small]

pieces=["pawn","rook","knight","bishop","king","queen"]
counter=0
winner=''
gameover=False

#all possible moves for all pieces
def check_options(pieces,location,turn):
    move_list=[]
    all_move_list=[]
    for i in range(len(pieces)):
        if pieces[i]=="pawn":
            move_list=check_pawn(location[i],turn)
        elif pieces[i]=="rook":
            move_list=check_rook(location[i],turn)
        elif pieces[i]=="knight":
            move_list=check_knight(location[i],turn)
        elif pieces[i]=="bishop":
            move_list=check_bishop(location[i],turn)
        elif pieces[i]=="king":
            move_list=check_king(location[i],turn)
        else:
            move_list=check_queen(location[i],turn)
        all_move_list.append(move_list)
    return all_move_list

#all possible moves for pawn
def check_pawn(location ,turn):
    move_list=[]
    if turn=="white":
        if (location[0],location[1]+1) not in (black_positions and white_positions) and location[1]<7:
            move_list.append((location[0],location[1]+1))
        if (location[0],location[1]+2) not in (black_positions and white_positions) and location[1]==1:
            move_list.append((location[0],location[1]+2))
        if (location[0]+1,location[1]+1) in black_positions:
            move_list.append((location[0]+1,location[1]+1))
        if (location[0]-1,location[1]+1) in black_positions:
            move_list.append((location[0]-1,location[1]+1))
    else:
        if (location[0],location[1]-1) not in (black_positions and white_positions) and location[1]>0:
            move_list.append((location[0],location[1]-1))
        if (location[0],location[1]-2) not in (black_positions and white_positions) and location[1]==6:
            move_list.append((location[0],location[1]-2))
        if (location[0]+1,location[1]-1) in white_positions:
            move_list.append((location[0]+1,location[1]-1))
        if (location[0]-1,location[1]-1) in white_positions:
            move_list.append((location[0]-1,location[1]-1))
    return move_list

#all possible moves for rook
def check_rook(location ,turn):
    move_list=[]
    if turn=="white":
        friend_list=white_positions
        enemy_list=black_positions
    else:
        friend_list=black_positions
        enemy_list=white_positions
    for i in range(4):
        chain=1
        path=True
        if i==0:
            x=1
            y=0
        elif i==1:
            x=-1
            y=0
        elif i==2:
            x=0
            y=1
        else:
            x=0
            y=-1
        while path:
            if (location[0]+chain*x,location[1]+chain*y) not in friend_list and (0<=location[0]+chain*x<=7 and 0<=location[1]+chain*y<=7):
                move_list.append((location[0]+chain*x,location[1]+chain*y))
                if (location[0]+chain*x,location[1]+chain*y) in enemy_list:
                    path=False
                chain+=1
            else:
                path=False
    return move_list

#all possible moves for a knight
def check_knight(location ,turn):
    move_list=[]
    if turn=="white":
        friend_list=white_positions
    else:
        friend_list=black_positions
    targets=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for i in range(8):
        target=(location[0]+targets[i][0],location[1]+targets[i][1])
        if target not in friend_list and 0<=target[0]<=7 and 0<=target[1]<=7:
            move_list.append(target)
    return move_list

#all possible moves for bishop
def check_bishop(location ,turn):
    move_list=[]
    if turn=="white":
        friend_list=white_positions
        enemy_list=black_positions
    else:
        friend_list=black_positions
        enemy_list=white_positions
    for i in range(4):
        chain=1
        path=True
        if i==0:
            x=1
            y=1
        elif i==1:
            x=-1
            y=-1
        elif i==2:
            x=-1
            y=1
        else:
            x=1
            y=-1
        while path:
            if (location[0]+chain*x,location[1]+chain*y) not in friend_list and (0<=location[0]+chain*x<=7 and 0<=location[1]+chain*y<=7):
                move_list.append((location[0]+chain*x,location[1]+chain*y))
                if (location[0]+chain*x,location[1]+chain*y) in enemy_list:
                    path=False
                chain+=1
            else:
                path=False
    return move_list

#all possible moves for king
def check_king(location ,turn):
    move_list=[]
    if turn=="white":
        friend_list=white_positions
    else:
        friend_list=black_positions
    targets=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
    for i in range(8):
        target=(location[0]+targets[i][0],location[1]+targets[i][1])
        if target not in friend_list and 0<=target[0]<=7 and 0<=target[1]<=7:
            move_list.append(target)
    return move_list

#all possible moves for queen
def check_queen(location ,turn):
    move_list=check_bishop(location,turn)
    second_list=check_rook(location,turn)
    for i in range(len(second_list)):
        move_list.append(second_list[i])
    return move_list

#Draw the board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [480 - (column * 160), row * 80, 80, 80])
        else:
            pygame.draw.rect(screen, 'light gray', [
                             560 - (column * 160), row * 80, 80, 80])
        pygame.draw.rect(screen, 'gray', [0, 640, 640, 80])
        pygame.draw.rect(screen, 'gold', [0, 640, 640, 80], 5)
        pygame.draw.rect(screen, 'gold', [640, 0, 160, 640], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(
            status_text[turn], True, 'black'), (20, 640))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 80 * i), (640, 80 * i), 2)
            pygame.draw.line(screen, 'black', (80 * i, 0), (80 * i, 640), 2)
        screen.blit(mid_font.render('FORFEIT', True, 'black'), (650, 670))

#draw pieces
def draw_pieces():
    for i in range(len(white_pieces)):
        index = pieces.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_positions[i][0]*80+10,white_positions[i][1]*80+10))
        else:
            screen.blit(white_images[index],(white_positions[i][0]*80+10,white_positions[i][1]*80+10))
        if turn<2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [white_positions[i][0] * 80 + 1, white_positions[i][1] * 80 + 1,80, 80], 2)
    
    for i in range(len(black_pieces)):
        index = pieces.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_positions[i][0] * 80 + 10, black_positions[i][1] * 80 + 10))
        else:
            screen.blit(black_images[index], (black_positions[i][0] * 80 + 10, black_positions[i][1] * 80 + 10))
        if turn>= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_positions[i][0] * 80 + 1, black_positions[i][1] * 80 + 1,80, 80], 2)

#captured pieces
def draw_captured():
    for i in range(len(captured_white)):
        captured_piece = captured_white[i]
        index = pieces.index(captured_piece)
        screen.blit(black_images_small[index], (665, 5 + 40 * i))
    for i in range(len(captured_black)):
        captured_piece = captured_black[i]
        index = pieces.index(captured_piece)
        screen.blit(white_images_small[index], (665, 5 + 40 * i))

#king in check
def draw_check():
    if turn < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_positions[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_positions[king_index][0] * 80 + 1,
                                                              white_positions[king_index][1] * 80 + 1, 80, 80], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_positions[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_positions[king_index][0] * 80 + 1,
                                                               black_positions[king_index][1] * 80 + 1, 80, 80], 5)

#check for valid moves for selected piece
def check_valid_moves():
    if turn< 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options

#valid moves shown on screen
def draw_valid(moves):
    if turn< 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(
            screen, color, (moves[i][0] * 80 + 40, moves[i][1] * 80 + 40), 5)

#GAME OVER
def draw_game_over():
    pygame.draw.rect(screen, 'black', [160, 160, 320, 56])
    screen.blit(font.render(
        f'{winner} won the game!', True, 'white'), (180, 180))
    screen.blit(font.render(f'Press ENTER to Restart!',
                True, 'white'), (180, 200))

#main block of code
black_options=check_options(black_pieces,black_positions,"black")
white_options=check_options(white_pieces,white_positions,"white")
run=True
while run:
    timer.tick(fps)
    if counter<30:
        counter+=1
    else:
        counter=0
    screen.fill("darkgrey")
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not gameover:
            x_coord = event.pos[0] // 80
            y_coord = event.pos[1] // 80
            click_coords = (x_coord, y_coord)
            if turn<= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_positions:
                    selection = white_positions.index(click_coords)
                    if turn== 0:
                        turn= 1
                if click_coords in valid_moves and selection != 100:
                    white_positions[selection] = click_coords
                    if click_coords in black_positions:
                        black_piece = black_positions.index(click_coords)
                        captured_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_positions.pop(black_piece)
                    black_options = check_options(
                        black_pieces, black_positions, 'black')
                    white_options = check_options(
                        white_pieces, white_positions, 'white')
                    turn= 2
                    selection = 100
                    valid_moves = []
            if turn> 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_positions:
                    selection = black_positions.index(click_coords)
                    if turn == 2:
                        turn= 3
                if click_coords in valid_moves and selection != 100:
                    black_positions[selection] = click_coords
                    if click_coords in white_positions:
                        white_piece = white_positions.index(click_coords)
                        captured_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_positions.pop(white_piece)
                    black_options = check_options(
                        black_pieces, black_positions, 'black')
                    white_options = check_options(
                        white_pieces, white_positions, 'white')
                    turn= 0
                    selection = 100
                    valid_moves = []

        if event.type == pygame.KEYDOWN and gameover:
            if event.key == pygame.K_RETURN:
                gameover = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_positions = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_positions = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_white= []
                captured_black= []
                turn= 0
                selection = 100
                valid_moves = []
                black_options = check_options(
                    black_pieces, black_positions, 'black')
                white_options = check_options(
                    white_pieces, white_positions, 'white')

    if winner != '':
        gameover = True
        draw_game_over()

    pygame.display.flip()

pygame.quit()
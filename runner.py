import pygame
import sys
import time

import tictactoe as ttt

pygame.init()

size = width, height = 600, 400

pygame.display.set_caption("Tic-Tac-Toe Game")
icon = pygame.image.load("ttt.png")
pygame.display.set_icon(icon)

orange = (204,85,0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("os-reg.ttf", 28)
largeFont = pygame.font.Font("os-reg.ttf", 40)
moveFont = pygame.font.Font("os-reg.ttf", 60)

player = None 
board = ttt.init_state() 
ai_turn = False 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(orange)

    if player is None:
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = (width / 2, 50)
        screen.blit(title, titleRect)

        playXButton = pygame.Rect(width / 8, height / 2, width / 4, 50)
        playX = mediumFont.render("Play as X", True, orange)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), height / 2, width / 4, 50)
        playO = mediumFont.render("Play as O", True, orange)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)

                player = ttt.X  
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                player = ttt.O  

    else:
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size), height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(tile_origin[0] + j * tile_size, tile_origin[1] + i * tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        plyr = ttt.plyr(board)

        if game_over:
            winr = ttt.winr(board)
            if winr is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winr} wins."
        elif player == plyr:
            title = f"Play as {player}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        if player != plyr and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.mini_max_algorithm(board)
                board = ttt.res(board, move)
                ai_turn = False
            else:
                ai_turn = True

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and player == plyr and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        board = ttt.res(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, orange)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)

            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    player = None
                    board = ttt.init_state()
                    ai_turn = False

    pygame.display.flip()

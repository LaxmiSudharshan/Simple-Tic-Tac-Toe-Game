import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((30, 30, 30))
pygame.display.set_caption("Tic Tac Toe Game")

# Grid
pygame.draw.line(screen, (255, 255, 255), (0, 200), (600, 200), 5)
pygame.draw.line(screen, (255, 255, 255), (0, 400), (600, 400), 5)
pygame.draw.line(screen, (255, 255, 255), (200, 0), (200, 600), 5)
pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 5)

pygame.display.flip()

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

current_player = "X"
cell_size = 200
font = pygame.font.SysFont(None, 60)
game_over = False


def check_winner(player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def check_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // cell_size
            col = x // cell_size

            if board[row][col] == "":
                board[row][col] = current_player

                if current_player == "X":
                    pygame.draw.line(screen, (0, 255, 0), (col*200+30, row*200+30), (col*200+170, row*200+170), 5)
                    pygame.draw.line(screen, (0, 255, 0), (col*200+170, row*200+30), (col*200+30, row*200+170), 5)

                    if check_winner("X"):
                        screen.blit(font.render("Oh, X Wins the Game", True, (0,0,0)), (180,260))
                        game_over = True

                    current_player = "O"

                else:
                    pygame.draw.circle(screen, (255, 0, 0),
                                       (col*200+100, row*200+100), 70, 5)

                    if check_winner("O"):
                        screen.blit(font.render("Oh, O Wins the Game", True, (0,0,0)), (180,260))
                        game_over = True

                    current_player = "X"

                if not game_over and check_draw():
                    screen.blit(font.render("Draw!", True, (255,255,0)), (220,260))
                    game_over = True

                pygame.display.flip()

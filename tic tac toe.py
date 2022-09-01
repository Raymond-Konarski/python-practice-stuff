import pygame

pygame.init()
BLACK = (0, 0, 0)
clock = pygame.time.Clock()

default_size = default_width, default_height = 500, 500
speed = 1
screen = pygame.display.set_mode(default_size)
pygame.display.set_caption("really bad tic tac toe attempt")
line_thickness = 5

std_dist = min(screen.get_height(), screen.get_width()) / 5


def coord_to_index(x, y):
    return x + (y * 5)


def index_to_coord(index):
    x = index % 5
    y = (index / 5).__floor__()
    return x, y


def draw_lines():
    dbl_b(1, 2, 4, 2)
    dbl_b(1, 3, 4, 3)
    dbl_b(2, 1, 2, 4)
    dbl_b(3, 1, 3, 4)
    # draw_board_line((std_dist,std_dist*2),(std_dist*4,std_dist*2))


def dbl_b(i, j, k, l):
    draw_board_line((std_dist * i, std_dist * j), (std_dist * k, std_dist * l))


def draw_board_line(start, end):
    pygame.draw.line(screen, (255, 255, 255), start, end, line_thickness)


# Board Draw Info
class Board:
    padding = std_dist
    size = width, height = screen.get_width() - (2 * padding), screen.get_height() - (2 * padding)
    block_size = (width / 3, height / 3)


def block(num):
    place_width = Board.padding + ((num - 1) % 3) * Board.width / 3
    place_height = Board.padding + ((num - 1) / 3).__floor__() * Board.height / 3
    return place_width, place_height


running = True
place = 400
while running:
    # Tick Clock
    delta = clock.tick(30) / 1000
    # Input Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Draw Constant
    screen.fill(BLACK)
    draw_lines()
    # Draw Changing

    # Update
    pygame.display.flip()

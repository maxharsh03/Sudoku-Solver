import pygame
import sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (240, 240, 240)
WINDOW_HEIGHT = 513
WINDOW_WIDTH = 513
ROWS = 9
COLS = 9
font = pygame.font.SysFont("ComicSans", 40)

# sudoku board
grid = [[0, 0, 6, 0, 7, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 2, 0],
        [4, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 8, 5, 0, 0, 2, 0, 7, 0],
        [0, 3, 4, 5, 0, 0, 0, 0, 0],
        [0, 1, 0, 7, 0, 0, 0, 0, 0],
        [3, 4, 0, 9, 1, 5, 0, 8, 7],
        [0, 0, 8, 4, 0, 0, 9, 0, 3],
        [1, 0, 0, 6, 0, 0, 0, 5, 0]]


# checks if board is completed
def check_empties(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return False
    return True


# checks if particular move is valid
def validate_board(grid, row, col, n):
    for i in range(9):  # validates row
        if grid[row][i] == n:
            return False

    for j in range(9):  # validates column
        if grid[j][col] == n:
            return False

    x = row//3*3
    y = col//3*3

    for i in range(x,x+3):  # validates box
        for j in range(y,y+3):
            if grid[i][j] == n:
                return False
    return True


# solves the sudoku board by backtracking
def solve(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if check_empties(grid):
                return True
            if grid[i][j] == 0:
                for n in range(1,10):
                    # validates guess
                    if validate_board(grid,i,j,n):
                        # temporarily assigns number to that spot
                        grid[i][j] = n
                        update(grid)

                        # means the guess we just took is valid, call function again
                        if solve(grid):
                            return True
                        # if not valid than we reset to 0 and guess again
                        grid[i][j] = 0
                        update(grid)

                # this is when we backtrack
                return False


def update(grid):
    SCREEN.fill(WHITE)
    draw_grid()
    fill_numbers(grid)
    pygame.display.update()


def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    while True:
        draw_grid()
        if solve(grid):
            print("Solved!")
        else:
            print("No solution exists")
        quit()

        pygame.display.update()


def draw_grid():
    block_size = WINDOW_WIDTH//ROWS
    for x in range(0, WINDOW_WIDTH, block_size):
        for y in range(0, WINDOW_HEIGHT, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(SCREEN, BLACK, rect, 2)


def fill_numbers(grid):
    block_size = WINDOW_WIDTH//ROWS
    for i in range(9):
        for j in range(9):
            text_surface = font.render(str(grid[i][j]), True, (15,15,15))
            if grid[i][j] != 0:
                SCREEN.blit(text_surface, (j*block_size+20,i*block_size+20))
            else:
                SCREEN.blit(text_surface, (j*block_size+20, i*block_size+20))


main()

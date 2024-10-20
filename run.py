import random

def create_grid(size):
    return [['~' for _ in range(size)] for _ in range(size)]

def display_grid(grid, hide_ships=True):
    size = len(grid)
    print(" " + " ".join(stri(i) for i in range(size)))
    for idx, row in enumerate(grid):
        display_row = []
        for cell in row:
            if hide_ships and cell == 'S':
                display_row.append('~')
            else:
                display_row.append(cell)
        print(f"{idx} "+" ".join(display_row))
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

def place_ships(grid, num_ships):
    siz = len(grid)
    ships_placed = 0
    while ships_placed < num_ships:
        orientation = random.choice(['H', 'V'])
        ship_length = random.randint(2, 3) #Ships of length 2 or 3
        if orientation == 'H':
            row = random.randint(0, size - 1)
            col = random.randint(0, size - ship_length)
            if all(grid[row][col + i] == '~' for i in range(ship_length)):
                for i in range(ship_length):
                    grid[row][col + i] = 'S'
                ships_placed += 1
        else:
            row = random.randint(0, size - ship_length)
            col = random.randint(0, size - 1)
            if all(grid[row + i][col] == '~' for i in range(ship_length)):
                for i in range(ship_length):
                    grid[row + i][col] = 'S'
                ships_placed += 1
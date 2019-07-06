# Project Euler - Problem 15 - Lattice paths
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# find number of paths in a n x n grid
# uses the idea of a grid being made up of 2 Pascal's Triangles to compute

def generate_grid(n):
    grid = []
    for row in range(n):
        grid.append([0]*n)
    return grid


def paths_through_grid(n):
    all_paths = 1 # counter to track total paths through a grid 
    grid = generate_grid(n) 

    for row in range(n):
        for column in range(n):
            if row == 0:
                grid[row][column] = 1
            elif column == 0:
                grid[row][column] = 1
            else:    
                grid[row][column] = grid[row][column-1]+grid[row-1][column]
        all_paths += sum(grid[row])

    return (grid, all_paths, grid[n-1][n-1])


paths_grid = paths_through_grid(20)
print("Total Paths In Grid: ", paths_grid[1])
print("Max Paths To Final Cell: ", paths_grid[2])

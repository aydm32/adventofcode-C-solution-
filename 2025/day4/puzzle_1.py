
"""" Adventofcode 2025 day4_part1 solution """


with open("puzzle_input_1.txt") as file: 
    grid = [ line.strip() for line in file if line.strip() ]

directions = [(-1,1) , (0,1),  (1,1),
              (-1,0) ,         (1,0),
              (-1,-1),(0,-1), (1,-1)]

rows, cols = len(grid), len(grid[0])

output = 0

for i in range(rows): 
    for j in range(cols): 
        if grid[i][j] != '@':
            continue
        rolls = 0 
        for dx, dy in directions: 
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] =='@':
                rolls += 1 
        if rolls < 4 :
            output += 1

print(output)

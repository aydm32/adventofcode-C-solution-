""" Adventofcode 2025 day6 part1 solution""" 

with open("puzzle_input_1.txt") as file: 
    data = []
    for line in file: 
        cleaned = (line.strip()).split()
        data.append(list(cleaned))  

total = 0 
for i in range(len(data[0])): 
    if data[4][i] == '+': 
        for j in range(0,4):
            total += int(data[j][i])
    elif data[4][i] == '*': 
        sub_total = 1
        for j in range(0,4): 
            sub_total *= int(data[j][i])
        total += sub_total
print(total)


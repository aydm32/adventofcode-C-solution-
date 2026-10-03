"""Advent of Code 2025 day 6 part 2"""

data = []
with open("puzzle_input_1.txt") as file:
    for line in file:
        cleaned = line.strip('\n')
        if cleaned.strip() != "":              
            data.append(list(cleaned))

width = max(len(row) for row in data)          
for row in data:
    while len(row) < width:
        row.append(' ')

operations = data[-1]
while ' ' in operations:
    operations.remove(' ')
numbers = data[:-1]

nums = []
for i in range(width):                         
    num = []
    for j in range(len(numbers)):
        num.append(numbers[j][i])
    nums.append(num)

for num in nums:
    while ' ' in num:
        num.remove(' ')

values = []
for num in nums:
    n = 0
    for i in range(len(num)):
        n += int(num[i]) * (10 ** (len(num) - i - 1))
    values.append(n)
values.append(0)                               

total = 0
j = 0                                          
for op in operations:
    if op == '+':
        sub_total = 0
    else:
        sub_total = 1
    while values[j] != 0:
        if op == '+':
            sub_total += values[j]
        else:
            sub_total *= values[j]
        j += 1
    j += 1                                     
    total += sub_total

print(total)

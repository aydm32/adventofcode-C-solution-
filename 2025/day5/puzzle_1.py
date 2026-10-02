""" Adventofcode 2025 day5_part1 solution"""

with open("puzzle_input_1.txt") as file: 
    ranges = []
    ids = []
    ranges_end = True 
    for line in file: 
        if line == '\n': 
            ranges_end = False 
        cleaned = line.strip()
        if cleaned != "":
            if ranges_end: 
                ranges.append(cleaned)
            else : 
                ids.append(cleaned)

count = 0
for id in ids: 
    id = int(id)
    fresh = False
    for range in ranges: 
        a, b = range.split("-")
        if id <= int(b) and id >= int(a) : 
            if not fresh: 
                count += 1 
                fresh = True
print(count)

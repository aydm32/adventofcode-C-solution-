"""Advent of Code 2025 day 5 part 2"""

ranges = []
with open("puzzle_input_1.txt") as file:
    for line in file:
        cleaned = line.strip()
        if cleaned == "":              
            break
        a, b = cleaned.split("-")
        ranges.append((int(a), int(b)))   

ranges.sort()                          

fresh = 0
last_end = None                        

for a, b in ranges:
    if last_end is None or a > last_end:
        # no overlap: the whole range is new
        fresh += b - a + 1
        last_end = b
    elif b > last_end:
        # overlap: only the part beyond last_end is new
        fresh += b - last_end
        last_end = b

print(fresh)

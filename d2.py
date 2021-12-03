from aoc import get_input

list = get_input(2).splitlines()

def p1(l):
    horizontal = 0
    vertical = 0
    
    for input in l:
        if input[:-2] == "forward":
            horizontal += int(input[-1])
        elif input[:-2] == "up": 
            vertical -= int(input[-1])
        elif input[:-2] == "down":
            vertical += int(input[-1])

    
    return horizontal * vertical

def p2(l):
    horizontal = 0
    vertical = 0
    aim = 0
    
    for input in l:
        if input[:-2] == "forward":
            horizontal += int(input[-1])
            vertical += (aim * int(input[-1]))
        elif input[:-2] == "up": 
            aim -= int(input[-1])
        elif input[:-2] == "down":
            aim += int(input[-1])

    
    return horizontal * vertical


print(f"p1: {p1(list)} p2: {p2(list)}")


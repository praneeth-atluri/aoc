with open('2015/day01.txt') as f:
    instructions = f.read()

    current_floor = 0
    for position, instruction in enumerate(instructions, start=1):
        if instruction == '(':
            current_floor = current_floor + 1
        if instruction == ')':
            current_floor -= 1
        if current_floor == -1:
            print(position)
            break

    print(current_floor)
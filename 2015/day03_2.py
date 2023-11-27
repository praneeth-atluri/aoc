with open('2015/day03.txt') as f:
    directions = f.read()

# Initialize the positions for Santa and Robo-Santa
santa_position = (0, 0)
robo_santa_position = (0, 0)

# Create a set to store visited positions
visited_positions = {(0, 0)}

# Flag to alternate between Santa and Robo-Santa
is_santa_turn = True

# Process the directions
for direction in directions:
    if is_santa_turn:
        current_position = santa_position
    else:
        current_position = robo_santa_position

    if direction == 'v':
        current_position = (current_position[0], current_position[1] - 1)
    elif direction == '^':
        current_position = (current_position[0], current_position[1] + 1)
    elif direction == '>':
        current_position = (current_position[0] + 1, current_position[1])
    elif direction == '<':
        current_position = (current_position[0] - 1, current_position[1])

    visited_positions.add(current_position)

    if is_santa_turn:
        santa_position = current_position
    else:
        robo_santa_position = current_position

    # Switch the turn between Santa and Robo-Santa
    is_santa_turn = not is_santa_turn

# Calculate the number of unique locations visited
unique_locations = len(visited_positions)

# Print the result
print("Total unique locations visited:", unique_locations)

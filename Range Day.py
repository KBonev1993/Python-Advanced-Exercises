def get_next_pos(direction, row, col, steps):
    if direction == "up":
        return row - steps, col
    elif direction == "down":
        return row + steps, col
    elif direction == "left":
        return row, col - steps
    else:
        return row, col + steps


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = 5
matrix = []
position_row = 0
position_col = 0
total_targets = 0


for row in range(size):
    rows = input().split()
    matrix.append(rows)
    for col in range(size):
        if rows[col] == "A":
            position_row = row
            position_col = col
        elif rows[col] == "x":
            total_targets += 1

targets_left = total_targets
hit_targets = []
line = int(input())

for _ in range(line):
    command_args = input().split()
    command = command_args[0]
    direction = command_args[1]
    if command == "move":
        steps = int(command_args[2])
        next_row, next_col = get_next_pos(direction, position_row, position_col, steps)

        if is_outside(next_row, next_col, size) or matrix[next_row][next_col] != ".":
            continue

        matrix[position_row][position_col] = "."
        position_row, position_col = next_row, next_col
        matrix[position_row][position_col] = "A"

    else:
        bullet_row, bullet_col = position_row, position_col
        while True:
            bullet_row, bullet_col = get_next_pos(direction, bullet_row, bullet_col, 1)

            if is_outside(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == "x":
                targets_left -= 1
                matrix[bullet_row][bullet_col] = "."
                hit_targets.append([bullet_row, bullet_col])
                break
        if targets_left == 0:
            break

if targets_left == 0:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {targets_left} targets left.")

for hit_target in hit_targets:
    print(hit_target)

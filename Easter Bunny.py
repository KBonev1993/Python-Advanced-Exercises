def move_up(row, col):
    return row - 1, col

def move_down(row, col):
    return row + 1, col

def move_left(row, col):
    return row, col - 1

def move_right(row, col):
    return row,col + 1

directions = {
    "right": move_right,
    "up": move_up,
    "down": move_down,
    "left": move_left

}
rows = int(input())
matrix = []
best_sum = float("-inf")
starting_point_row = 0
starting_point_col = 0
best_dir = ""
for row in range(rows):
    numbers = [x for x in input().split()]
    matrix.append(numbers)
    for col in range(rows):
        if numbers[col] == "B":
            starting_point_col = col
            starting_point_row = row

for direction,step in directions.items():
    current_row, current_col = starting_point_row, starting_point_col
    current_score = 0
    path = []
    while True:
        current_row,current_col = step(current_row, current_col)
        if current_col < 0 or current_row < 0 or current_row >= rows or current_col >= rows:
            break
        if matrix[current_row][current_col] == "X":
            break
        path.append([current_row, current_col])
        current_score += int(matrix[current_row][current_col])
    if current_score > best_sum:
        best_sum = current_score
        best_dir = direction
        best_path = path

print(best_dir)
print(*best_path, sep= "\n")
print(best_sum)

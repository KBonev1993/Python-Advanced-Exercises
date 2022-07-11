rows, cols = [int(x) for x in input().split(", ")]
matrix = []
best_row_one = 0
best_row_second = 0
max_sum = 0
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = matrix[row][col] + matrix[row + 1][col] + matrix[row][col + 1] + matrix[row + 1][col + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            best_row_one = matrix[row][col], matrix[row][col + 1]
            best_row_second =  matrix[row + 1][col], matrix[row + 1][col + 1]
        else:
            continue

print(*best_row_one)
print(*best_row_second)
print(max_sum)


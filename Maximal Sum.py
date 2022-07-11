import sys

rows, cols = [int(x) for x in input().split()]
matrix = []
matrix_sum = -sys.maxsize
best_row = -sys.maxsize
best_col = -sys.maxsize
for _ in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for row in range(rows - 2):
    for col in range(cols - 2):
        current_matrix = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2]\
                + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +\
                matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col +2]
        if current_matrix > matrix_sum:
            matrix_sum = current_matrix
            best_row = row
            best_col = col

print(f"Sum = {matrix_sum}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}")

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
        letters = [x for x in input().split()]
        matrix.append(letters)

result = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            result += 1
    continue

print(result)

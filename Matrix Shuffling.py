def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    numbers = [x for x in input().split()]
    matrix.append(numbers)



while True:
    line = input()
    if line == "END":
        break
    data = line.split()
    command = data[0]

    if not command == "swap" or len(data) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in data[1:]]
    
    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print("Invalid input!")
        continue
    else:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(*row, sep=" ")

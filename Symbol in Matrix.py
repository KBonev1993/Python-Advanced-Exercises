rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append(input())

symbol = input()

symbol_not_found = True
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            symbol_not_found = False

if symbol_not_found:
    print(f"{symbol} does not occur in the matrix")

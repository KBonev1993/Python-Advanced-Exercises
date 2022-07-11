def is_valid(row, col, rows):
    return row < 0 or col < 0 or row >= rows or col >= rows
 
 
rows = int(input())
matrix = []
quantity_of_tea = 0
alice_position = []
 
for i in range(rows):
    current_row = input().split()
    matrix.append(current_row)
 
    for j in range(rows):
        if matrix[i][j] == 'A':
            alice_position = [i, j]
 
command = input()
 
 
while quantity_of_tea < 10:
    matrix[alice_position[0]][alice_position[1]] = '*'
    if command == 'up':
        alice_position[0] -= 1
    elif command == 'down':
        alice_position[0] += 1
    elif command == 'left':
        alice_position[1] -= 1
    elif command == 'right':
        alice_position[1] += 1
 
    current_row = alice_position[0]
    current_col = alice_position[1]
    if is_valid(current_row, current_col, rows):
        break
    if matrix[current_row][current_col] == 'R':
        matrix[current_row][current_col] = '*'
        break
    elif matrix[current_row][current_col] == '.':
        command = input()
        continue
    elif matrix[current_row][current_col] == '*':
        command = input()
        continue
    else:
        quantity_of_tea += int(matrix[current_row][current_col])
        if quantity_of_tea >= 10:
            break
 
    command = input()
 
if quantity_of_tea >= 10:
    matrix[alice_position[0]][alice_position[1]] = '*'
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
 
for row in matrix:
    print(*row,sep=' ')

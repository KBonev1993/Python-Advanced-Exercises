size = int(input())
matrix = []

for _ in range(size):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)


while True:
    line = input()
    if line == "END":
        break
    command, command_row, command_col, value = line.split()
    int_command_row = int(command_row)
    int_command_col = int(command_col)
    if int_command_row < 0 or int_command_col < 0 or int_command_row >= size or int_command_col >= size:
        print("Invalid coordinates")
        continue
    else:
        if command == "Add":
            matrix[int_command_row][int_command_col] += int(value)
        if command == "Subtract":
            matrix[int_command_row][int_command_col] -= int(value)


for el in matrix:
    print(*el, sep=" ")

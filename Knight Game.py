n = int(input())
 
matrix = []
for _ in range(n):
    matrix.append(list(input()))
 
knights = {}
 
 
def is_inside(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False
 
 
def add_knight(p):
    if p not in knights:
        knights[p] = 0
    knights[p] += 1
 
 
def possible_attack(r, c):
    position = str(r) + " " + str(c)
    if is_inside(r - 1, c - 2):
        if matrix[r - 1][c - 2] == "K":
            add_knight(position)
    if is_inside(r - 2, c - 1):
        if matrix[r - 2][c - 1] == "K":
            add_knight(position)
    if is_inside(r - 2, c + 1):
        if matrix[r - 2][c + 1] == "K":
            add_knight(position)
    if is_inside(r - 1, c + 2):
        if matrix[r - 1][c + 2] == "K":
            add_knight(position)
    if is_inside(r + 1, c + 2):
        if matrix[r + 1][c + 2] == "K":
            add_knight(position)
    if is_inside(r + 2, c + 1):
        if matrix[r + 2][c + 1] == "K":
            add_knight(position)
    if is_inside(r + 2, c - 1):
        if matrix[r + 2][c - 1] == "K":
            add_knight(position)
    if is_inside(r + 1, c - 2):
        if matrix[r + 1][c - 2] == "K":
            add_knight(position)
 
 
knights_removed = 0
while True:
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "K":
                possible_attack(i, j)
    if knights:
        max_attacks = max(knights, key=lambda x: knights[x])
        row_remove, col_remove = [int(x) for x in max_attacks.split()]
        matrix[row_remove][col_remove] = "0"
        knights_removed += 1
    else:
        break
    knights = {}
 
print(knights_removed)

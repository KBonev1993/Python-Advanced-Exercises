rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
for _ in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

for idx in range(rows):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][rows - 1 - idx])

a = sum(primary_diagonal)
b = sum(secondary_diagonal)
print(abs(a - b))

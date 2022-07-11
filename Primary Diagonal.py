rows = int(input())

matrix = []
res = 0

for _ in range(rows):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

for rows in range(len(matrix)):
    for cols in range(len(matrix)):
        if rows == cols:
            res += matrix[rows][cols]

print(res)

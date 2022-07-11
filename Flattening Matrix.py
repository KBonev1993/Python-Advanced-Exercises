rows = int(input())

matrix = []

for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    matrix.extend(nums)

print(matrix)

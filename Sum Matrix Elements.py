rows,columns = [int(x) for x in input().split(", ")]
result = 0
matrix = []
for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    result += sum(nums)
    matrix.append(nums)

print(result)
print(matrix)

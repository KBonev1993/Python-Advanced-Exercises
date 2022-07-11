rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
for _ in range(rows):
    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)

for idx in range(rows):
    primary_diagonal.append(matrix[idx][idx])
    secondary_diagonal.append(matrix[idx][rows - 1 - idx])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

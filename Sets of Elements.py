m, n = [int(x) for x in input().split()]
first_set = set()
second_set = set()

for _ in range(m):
    numbers = int(input())
    first_set.add(numbers)

for _ in range(n):
    numbers = int(input())
    second_set.add(numbers)

final_set = second_set.intersection(first_set)
print('\n'.join([str(x)for x in final_set]))

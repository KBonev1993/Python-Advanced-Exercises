n = int(input())
odd_set = set()
even_set = set()
current_sum = 0
odd_sum = 0
even_sum = 0

for row in range(1, n + 1):

    names = input()
    for char in names:
        current_sum += ord(char)
    final_sum = int(current_sum / row)
    if final_sum % 2 == 0:
        even_set.add(final_sum)
        even_sum += final_sum
    else:
        odd_set.add(final_sum)
        odd_sum += final_sum
    current_sum = 0
final_sum = 0


if odd_sum == even_sum:
    result = odd_set.union(even_set)
elif even_sum > odd_sum:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(*result, sep=', ')


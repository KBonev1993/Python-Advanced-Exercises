def intersection(range_info):
    start,end = [int(x) for x in range_info.split(',')]
    return set(range(start, end + 1))

n = int(input())
best_intersection = set()

for _ in range(n):
    two_ranges = input().split('-')
    first_half = intersection(two_ranges[0])
    second_half = intersection(two_ranges[1])
    current_intersection = first_half.intersection(second_half)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection


print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}]\
 with length {len(best_intersection)}")

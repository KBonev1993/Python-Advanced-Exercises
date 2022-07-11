numbers = input().split()
positive_numbers = [int(x) for x in numbers if int(x) > 0]
negative_numbers = [int(x) for x in numbers if int(x) < 0]
positive_numbers_sum = sum(positive_numbers)
negative_numbers_sum = sum(negative_numbers)

print(negative_numbers_sum)
print(positive_numbers_sum)
if positive_numbers_sum > abs(negative_numbers_sum):
    print(f"The positives are stronger than the negatives")
else:
    print(f"The negatives are stronger than the positives")

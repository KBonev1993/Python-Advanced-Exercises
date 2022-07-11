box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_capacity = rack_capacity
current_rack = 1

while box_of_clothes:
    current_cloth = box_of_clothes[-1]
    if current_cloth <= current_capacity:
        current_capacity -= current_cloth
        box_of_clothes.pop()
    else:
        current_rack += 1
        current_capacity = rack_capacity

print(current_rack)

from collections import deque

quantity_of_food = int(input())
food_orders = deque([int(x) for x in input().split()])
food = deque()
biggest_order = max(food_orders)
print(biggest_order)

while food_orders:
    current_order = food_orders[0]
    if current_order <= quantity_of_food:
        quantity_of_food -= current_order
        food_orders.popleft()
    else:
        break

if food_orders:
    print(f"Orders left: {' '.join([str(x) for x in food_orders])}")
else:
    print(f"Orders complete")

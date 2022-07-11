n = int(input())
cars = set()

for _ in range(n):
    command, car = input().split(', ')
    if command == "IN":
        cars.add(car)
    elif command == "OUT":
        cars.discard(car)
if cars:
    print('\n'.join(cars))
else:
    print(f"Parking Lot is Empty")

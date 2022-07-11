from collections import deque

petrol_pumps = int(input())
pumps = deque()


for _ in range(petrol_pumps):
    pumps_data = [int(x) for x in input().split()]
    pumps.append(pumps_data)

for attempt in range(petrol_pumps):
    tank = 0
    failed = False
    for fuel, distance in pumps:
        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break

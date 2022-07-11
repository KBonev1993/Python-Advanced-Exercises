from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
operators = deque(input().split())
honey = 0

while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()
    if nectar >= bee:
        operator = operators.popleft()
        if operator == "+":
            honey += bee + nectar
        elif operator == "-":
            honey += abs(bee - nectar)
        elif operator == "*":
            honey += bee * nectar
        elif operator == "/" and nectar > 0:
            honey += abs(bee / nectar)
    else:
        working_bees.appendleft(bee)
        continue

print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")

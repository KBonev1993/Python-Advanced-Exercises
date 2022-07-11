from collections import deque

customers = input()
line = deque()

while not customers == "End":
    if customers == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(customers)
    customers = input()
print(f"{len(line)} people remaining.")

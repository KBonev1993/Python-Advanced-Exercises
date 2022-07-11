from collections import deque

litres_of_water = int(input())
people =  input()
line = deque()

while not people == "Start":
    line.append(people)
    people = input()

command = input()
while not command == "End":
    if command.isdigit():
        required_liters = int(command)
        people = line.popleft()
        if litres_of_water >= required_liters:
            litres_of_water -= required_liters
            print(f"{people} got water")
        elif litres_of_water < required_liters:
            print(f"{people} must wait")

    else:
        _, refill_water = command.split()
        litres_of_water += int(refill_water)
    command = input()

print(f"{litres_of_water} liters left")

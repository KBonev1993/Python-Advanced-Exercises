n = int(input())
numbers_stack = []

for _ in range(n):
    query = input().split()
    command = query[0]
    if command == "1":
        number = query[1]
        numbers_stack.append(number)
    elif command == "2" and numbers_stack:
        numbers_stack.pop()
    elif command == "3" and numbers_stack:
        print(max(numbers_stack))
    elif command == "4" and numbers_stack:
        print(min(numbers_stack))

while numbers_stack:
    number = numbers_stack.pop()
    if numbers_stack:
        print(number, end=', ')
    else:
        print(number)

first_numbers = set([int(x) for x in input().split()])
second_numbers = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            [first_numbers.add(int(x)) for x in command[2:]]
        else:
            [second_numbers.add(int(x)) for x in command[2:]]
    elif command[0] == "Remove":
        if command[1] == "First":
            [first_numbers.discard(int(x)) for x in command[2:]]
        else:
            [second_numbers.discard(int(x)) for x in command[2:]]
    else:
        print(first_numbers.issubset(second_numbers) or second_numbers.issubset(first_numbers))

print(*sorted(first_numbers), sep=", ")
print(*sorted(second_numbers), sep=", ")

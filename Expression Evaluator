from collections import deque

elements = input().split()
numbers = deque()

for element in elements:
        if element in "-+/*":
            while len(numbers) > 1:
                first_number = numbers.popleft()
                second_number = numbers.popleft()
                new_number = 0
                if element == "+":
                    new_number = int(first_number) + int(second_number)
                    numbers.appendleft(int(new_number))
                elif element == "-":
                    new_number = int(first_number) - int(second_number)
                    numbers.appendleft(int(new_number))
                elif element == "*":
                    new_number = int(first_number) * int(second_number)
                    numbers.appendleft(int(new_number))
                elif element == "/":
                    new_number = int(first_number) / int(second_number)
                    numbers.appendleft(int(new_number))

        else:
            numbers.append(int(element))

print(numbers.popleft())

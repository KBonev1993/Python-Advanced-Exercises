numbers = input()
numbers_stack = []

for char in range(len(numbers)):
    if numbers[char] == "(":
        numbers_stack.append(char)
    elif numbers[char] == ")":
        start_index = numbers_stack.pop()
        print(numbers[start_index: char+1])

parentheses = input()
par_stack = []
balanced = True

for char in parentheses:
    if char in "{[(":
        par_stack.append(char)
    elif not par_stack:
        balanced = False
        break
    else:
        last_open_bracket = par_stack.pop()
        if f"{last_open_bracket}{char}" not in "{}[]()":
            balanced = False
            break

if balanced:
    print('YES')
else:
    print('NO')


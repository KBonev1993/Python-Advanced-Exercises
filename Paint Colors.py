from collections import deque
 
substrings = deque(input().split())
 
color_names = ('blue', 'red', 'yellow', 'orange', 'purple', 'green')
colors = []
 
while substrings:
    first = substrings.popleft()
    if substrings:
        last = substrings.pop()
    else:
        last = ''
    if first + last in color_names:
        colors.append(first + last)
    elif last + first in color_names:
        colors.append(last + first)
    else:
        first = first[:-1]
        last = last[:-1]
        if len(first) > 0:
            substrings.insert(len(substrings) // 2, first)
        if len(last) > 0:
            substrings.insert(len(substrings) // 2, last)
 
if 'orange' in colors and ('yellow' not in colors or 'red' not in colors):
    colors.remove('orange')
if 'purple' in colors and ('blue' not in colors or 'red' not in colors):
    colors.remove('purple')
if 'green' in colors and ('yellow' not in colors or 'blue' not in colors):
    colors.remove('green')
 
print(colors)

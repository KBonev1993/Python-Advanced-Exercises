a = input().split("|")
c = []

while a:
    c.extend(a.pop().split())

print(*c, sep=" ")

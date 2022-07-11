n = int(input())
guests = set()

for _ in range(n):
    codes = input()
    guests.add(codes)

guests_code = input()
while not guests_code == "END":
    guests.discard(guests_code)
    guests_code = input()

print(len(guests))
print('\n'.join(sorted(guests)))

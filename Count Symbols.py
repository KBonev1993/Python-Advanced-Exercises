text = input()
text_dict = {}
for char in text:
    if char not in text_dict:
        text_dict[char] = 0
    text_dict[char] += 1

for key,value in sorted(text_dict.items()):
    print(f"{key}: {value} time/s")

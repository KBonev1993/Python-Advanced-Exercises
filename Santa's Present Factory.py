from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    result = magic * material

    if result in presents:
        toy = presents[result]
        if toy in crafted_presents:
            crafted_presents[toy] += 1
        else:
            crafted_presents[toy] = 1
    elif result < 0:
        result = magic + material
        materials.append(result)
    elif result > 0:
        materials.append(material + 15)
    else:
        if magic == 0 and material == 0:
            continue
        elif magic == 0:
            materials.append(material)
        elif material == 0:
            magic_level.appendleft(magic)

if "Doll" in crafted_presents and "Wooden train" in crafted_presents \
    or "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if magic_level:
    print(f" Magic left: {', '.join([str(x) for x in magic_level])}")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

for toy,value in sorted(crafted_presents.items()):
    print(f"{toy}: {value}")

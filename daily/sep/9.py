properties = [[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]
properties.sort(key=lambda x: (-x[0], x[1]))

print(properties)

max_defense = 0
res = 0
for i in range(len(properties)):
    if max_defense > properties[i][1]:
        res += 1
    max_defense = max(max_defense, properties[i][1])


print(res)

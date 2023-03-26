arr = [1, 2, 3]
res = [[]]

for num in arr:
    for i in range(len(res)):
        res.append(res[i] + [num])

print(res)

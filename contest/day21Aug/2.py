from collections import defaultdict


num = "00011"
num = sorted(num, reverse=True)
num = list(num)

print(num)
d = defaultdict(int)
for i in num:
    d[i] += 1

num = list(set(num))

arr_side = []
arr_side_left = []


num = sorted(num, reverse=True)
print(num)

print(d)
for i in num:
    print(i, d[i])
    if d[i] >= 2:
        for j in range(d[i] // 2):
            arr_side.append(i)
            arr_side_left.append(i)
for i in num:
    if d[i] % 2 == 1:
        arr_side.append(i)
        break


print("arr_side", arr_side)
if(arr_side[0] == '0'):
    print(arr_side[-1])

arr_side_left = arr_side_left[::-1]
print("arr_side_left", arr_side_left)
res = [*arr_side, *arr_side_left]

print(res)
res = "".join(res)
print(res)
print(type(res))

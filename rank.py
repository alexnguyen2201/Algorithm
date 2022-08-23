num = 6
arr = ["doc", "doc(1)", "doc(1)", "doc(1)", "doc(2)", "doc(1)"]
k = {}

for i in range(num):
    file = arr[i]
    if file in k:
        print(f"{file}({k[file]})")
        k[f"{file}({k[file]})"] = 1
        k[file] += 1
    else:
        print(f"{file}")
        k[file] = 1

print(k)

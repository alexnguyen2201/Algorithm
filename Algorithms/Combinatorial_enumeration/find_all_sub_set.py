s = 'ABCD'

current_str = []
res = []


def backtrack(i):
    if i == len(s):
        return
    current_str.append(s[i])
    res.append(current_str[:])
    for i in range(i+1, len(s)):
        backtrack(i)
    current_str.pop()


for i in range(len(s)):
    backtrack(i)

for i in res:
    print("".join(i))

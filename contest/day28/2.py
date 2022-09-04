s = "leet**cod*e"

stack = []

for i in s:
    if stack and i == "*":
        stack.pop()
    if i != "*":
        stack.append(i)

print("".join(stack)))

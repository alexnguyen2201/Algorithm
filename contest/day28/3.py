garbage = ["MMM", "PGM", "GP"]
travel = [3, 10]

last_M = 0
last_P = 0
last_G = 0

for i in range(len(garbage)-1, -1, -1):
    if "M" in garbage[i]:
        last_M = i
        break

for i in range(len(garbage)-1, -1, -1):
    if "P" in garbage[i]:
        last_P = i
        break

for i in range(len(garbage)-1, -1, -1):
    if "G" in garbage[i]:
        last_G = i
        break

# MPG
print(last_M, last_P, last_G)
res = 0
for i in garbage:
    res += len(i)

res += (sum(travel[:last_M]) + sum(travel[:last_P]) + sum(travel[:last_G]))

print(res)

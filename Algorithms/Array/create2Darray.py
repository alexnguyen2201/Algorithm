cols = 2
rows = 3
f = [[0 for x in range(cols)] for _ in range(rows)]


print(f)
memo = [[0] * (rows + 1) for _ in range(cols + 1)]

# Example
# memo = [[0] * 5 for _ in range(3)]


memo = [[0] * 5 for _ in range(3)]
print(memo)
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
memo[0][0] = 1
print(memo)


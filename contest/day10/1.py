

amount = [5, 4, 4]

amount.sort(reverse=True)

print(amount)
seconds = 0

while amount:
    if amount[-1] == 0:
        amount.pop()

    if amount and amount[-1] == 0:
        amount.pop()

    if not amount:
        break

    if len(amount) == 3 or len(amount) == 2:
        amount[0] -= 1
        amount[1] -= 1
        amount.sort(reverse=True)
        seconds += 1
    else:
        amount[0] -= 1
        seconds += 1

print(seconds)

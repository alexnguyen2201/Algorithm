weights = [1, 4, 4]
k = 3



def feasible(capacity) -> bool:
    days = 1
    total = 0
    arr = []
    for weight in weights:
        total += weight
        if total > capacity:  # too heavy, wait for the next day
            arr.append(total - weight)
            total = weight
            days += 1
            if days > k:  # cannot ship within D days
                return False
    arr.append(total)
    print(arr)
    return True


capacity = 5
feasible(capacity)
# print(arr)

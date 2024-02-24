def check_meet(x1, x2, v1, v2):
    if v1 == v2 and x1 != x2:
        return False

    if (x1 - x2) % (v2 - v1) == 0 and (x1 - x2) // (v2 - v1) >= 0:
        return True

    return False


print(check_meet(2, 5, 1, 2))

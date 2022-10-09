def find_x(a, b):
    a_str = bin(a)[2:]
    b_str = bin(b)[2:]
    if len(a_str) < len(b_str):
        a_str = "".join(['0' for _ in range(len(b_str) - len(a_str))]) + a_str
    elif len(a_str) > len(b_str):
        b_str = "".join(['0' for _ in range(len(a_str) - len(b_str))]) + b_str

    print(a_str)
    print(b_str)

    res = []
    for i in range(len(a_str)):
        if b_str[i] == '0':
            res.append(a_str[i])
        else:
            res.append(str(1-int(a_str[i])))
    return int("".join(res), 2)


print(find_x(5, 2))

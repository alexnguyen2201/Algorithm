start = "_L__R__R_"
target = "L______RR"


def canChange():
    index_start = []
    for i in range(len(start)):
        if start[i] == "L":
            index_start.append((i, 0))
        if start[i] == "R":
            index_start.append((i, 1))

    index_target = []
    for i in range(len(target)):
        if target[i] == "L":
            index_target.append((i, 0))
        if target[i] == "R":
            index_target.append((i, 1))

    for i in range(len(index_start)):
        si = index_start[i]
        ti = index_target[i]
        if si[1] == 0:
            if si[0] < ti[0]:
                return False
        else:
            if si[0] > ti[0]:
                return False

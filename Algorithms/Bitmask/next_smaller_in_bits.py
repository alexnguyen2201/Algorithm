from collections import deque


def next_smaller(n):
    n_str = list(str(n))
    n_int = [int(i) for i in n_str]

    if len(n_int) == 1:
        return -1

    index = -1
    for i in range(len(n_int)-1, -1, -1):
        queue = deque()
        for j in range(i+1, len(n_int)):

            if n_int[i] > n_int[j]:
                while queue and n_int[j] >= queue[-1][1]:
                    queue.pop()
                queue.append((j, n_int[j]))

        if queue:
            index = i
            n_int[i], n_int[queue[-1][0]] = n_int[queue[-1][0]], n_int[i]
            break

    if not queue:
        return -1
    else:
        left = n_int[:index+1]
        right = n_int[index+1:]
        right.sort(reverse=True)
        all_arr = left + right

        if all_arr[0] == 0:
            return -1

        return int("".join([str(i) for i in all_arr]))


print(next_smaller(907))

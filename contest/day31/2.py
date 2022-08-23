grades = [10, 6, 12, 7, 3, 5]

# [3, 5, 6, 7, 10, 12]


def maximumGroups(grades):
    grades.sort()
    print(grades)

    prev_len = 1
    prev_sum = grades[0]

    res = 1
    curr_index = 1

    while curr_index < len(grades):

        curr_sum = 0
        curr_len = 0

        while curr_len <= prev_len or curr_sum <= prev_sum:
            if curr_index == len(grades):
                return res

            curr_len += 1
            curr_sum += grades[curr_index]
            curr_index += 1

        res += 1

        prev_len = curr_len
        prev_sum = curr_sum

    return res


print(maximumGroups(grades))

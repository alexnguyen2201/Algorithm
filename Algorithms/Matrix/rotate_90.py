def rotate_90_degree_anticlckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i - 1], matrix)))

    return new_matrix


def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix


def rotate_90_degree_clckwise_by_zip_method(matrix):
    return list(list(x)[::-1] for x in zip(*matrix))


def rotate_90_degree_anticlckwise_by_zip_method(matrix):
    return list(list(x) for x in zip(*matrix))[::-1]


matrix = [
    [1, 2, 3],
    [11, 22, 33]
]

print(rotate_90_degree_clckwise_by_zip_method(matrix))
print(rotate_90_degree_anticlckwise_by_zip_method(matrix))

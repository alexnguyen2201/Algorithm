def BS(arr, X, left):
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= X:
            right = mid
        else:
            left = mid + 1

    return left


def countPairsWithDiffK(arr, N, distance):
    count = 0
    arr.sort()
    for i in range(N):
        first_index = BS(arr, arr[i] + distance, i + 1)
        if first_index != N:
            last_index = BS(arr, arr[i] + distance + 1, i + 1)
            count += last_index - first_index

    return count


if __name__ == '__main__':
    array = [1, 3, 5, 8, 6, 4, 6]
    n = len(array)
    k = 2
    print("Count of pairs with given diff is ", countPairsWithDiffK(array, n, k))


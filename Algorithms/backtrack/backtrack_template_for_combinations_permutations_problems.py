# def subsets(nums):
#     res, path = [], []
#     dfs(0, res, path, nums)
#     return res
#
#
# def dfs(index, res, path, nums):
#     res.append(path[:])
#     for i in range(index, len(nums)):
#         path.append(nums[i])
#         dfs(i + 1, res, path, nums)
#         path.pop()

########################################################################################################################
"""
Simple version
"""
import collections
from typing import List

nums = [1, 2, 3]
res, path = [], []


def dfs(index):
    res.append(path[:])

    for i in range(index, len(nums)):
        path.append(nums[i])
        dfs(i + 1)
        path.pop()


dfs(0)
print(res)

########################################################################################################################
"""
Tối ưu tốc độ, nhưng yếu về space
"""


# https://leetcode.com/problems/combination-sum/description/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path, res = [], []
        candidates.sort()

        def dfs(start, path, curr_sum):
            if curr_sum == target:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                if curr_sum + candidates[i] > target:
                    break
                dfs(i, path + [candidates[i]], curr_sum + candidates[i])
                # call dfs(i) not dfs(i+1) because we can use duplicates here!

        dfs(0, [], 0)
        return res


# Cách tối ưu hơn để không phải tính sum (tiêu tốn O(n)) mỗi lần chạy vào hàm là:
# sử dụng dfs(start, curr_sum).


########################################################################################################################

nums = [1, 1, 2, 2, 2, 3, 3, 3]
res, path = [], []
target = 3

counter = collections.Counter()
counter = [(c, counter[c]) for c in counter]


# Chuyển counter sang dạng list như này coi như một cách implement ngắn gọn của Orderdict


def dfs2(index, curr_sum):
    if curr_sum > target:
        return
    if curr_sum == target:
        res.append(path[:])

    for i in range(index, len(counter)):
        """
        code kiểu bucket như này sẽ không tạo ra các path bị lặp
        lý do là khi for tiến thêm một bước ta đi sang một bucket khác.
        ví dụ:
        [1,1,2,2,2,2,5,5,6]
        target = 7
        -> [(2, 4), (5, 1), (6, 1)]
        recusive: [2,2,2,2] + other bucket
        recusive: [2,2,2] + other bucket
        recusive: [2,2] + other bucket
        recusive: [2] + other bucket
        recusive: None + otherbucket  (go to next bucket)
        """
        candidate, freq = counter[i]
        if not freq:
            continue

        path.append(candidate)
        counter[i] = (candidate, freq - 1)

        dfs2(i, curr_sum + candidate)

        path.pop()
        counter[i] = (candidate, freq)


dfs(0)
print(res)


########################################################################################################################
def backtrack(row, diagonals, anti_diagonals, cols, state):
    # Base case - N queens have been placed
    if row == n:
        ans.append(state)
        return

    for col in range(n):
        curr_diagonal = row - col
        curr_anti_diagonal = row + col

        # If the queen is not placeable
        if (
                col in cols
                or curr_diagonal in diagonals
                or curr_anti_diagonal in anti_diagonals
        ):
            continue

        # "Add" the queen to the board
        cols.add(col)
        diagonals.add(curr_diagonal)
        anti_diagonals.add(curr_anti_diagonal)
        state[row][col] = "Q"

        # Move on to the next row with the updated board state
        backtrack(row + 1, diagonals, anti_diagonals, cols, state)

        # "Remove" the queen from the board since we have already
        # explored all valid paths using the above function call
        cols.remove(col)
        diagonals.remove(curr_diagonal)
        anti_diagonals.remove(curr_anti_diagonal)
        state[row][col] = "."

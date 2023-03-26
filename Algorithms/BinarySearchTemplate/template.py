# Minimize k, s.t. condition(k) is True


def binary_search(array):
    def condition(value):
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1,n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left


"""
Template phía trên rất mạnh:
Điều quan trọng là tìm được đúng:
- init range tìm kiếm: left và right
- retunr left hoặc left - 1 (ghi nhớ trong đầu là: left là giá trị nhỏ nhất thoả mãn điều kiện `condition`)
- Thiết kế condition. (Phần khó nhất)

Ví dụ trong bài binary search tìm số x trong arr (đã xắp xếp), nếu ko tìm được thì nhét nó vào vị trí thoả mãn:
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
        
Ta phải chọn right = len(nums) vì có thể phải nhét vào vị trí này khi mà target lớn hơn mọi số trong nums.
Điều kiện là: vị trí nhỏ nhất thoả mãn >= target. (nếu == target thì case mà nó không bằng thì auto nhét vào cuối --> sai)
"""

"""
Template nguoc, left là giá trị lớn nhất thoả mãn điều kiện:
        while left < right:
            mid = right - (right - left) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left
"""







# another faster template in case always finded.

# while left <= right:
#     mid = (left + right) // 2
#     if condition(mid):
#         right = mid - 1
#         res = mid
#     else:
#         left = mid + 1
#
# return mid



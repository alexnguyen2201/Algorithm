"""
cho một dãy, tìm cặp x + y có tổng lớn nhất
"""

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans, cur = 0, values[0]
        for i in range(1, len(values)):
            ans = max(ans, cur+values[i])  # x = cur giữ nguyên, y = values[i]
            cur = max(cur, values[i])  # chọn giá trị x to nhất
        return ans


values = [1, 5, 6, 2, 3]

print(Solution().maxScoreSightseeingPair(values))

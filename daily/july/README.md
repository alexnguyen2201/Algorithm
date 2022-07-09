# July 2022

- Day 9:
https://vnoi.info/wiki/algo/data-structures/deque-min-max.md
```C++
deque <int> dq;

/* Làm rỗng deque */
while (dq.size()) dq.pop_front();

/* Duyệt lần lượt các phần tử từ 1 đến N */
for (int i = 1; i <= N; ++i) { 
    /* Loại bỏ các phần tử có giá trị lớn hơn hoặc bằng A[i] */
    while (dq.size() && A[dq.back()] >= A[i]) dq.pop_back();
    
    /* Đẩy phần tử i vào queue */
    dq.push_back(i); 
    
    /* Nếu phần tử đầu tiên trong deque nằm ngoài khoảng tính 
       thì ta sẽ loại bỏ ra khỏi deque */
    if (dq.front() + k <= i) dq.pop_front(); 
    
    /* minRange[i] là giá trị nhỏ nhất trong đoạn [i – k + 1 … i] */
    if (i >= k) minRange[i] = A[dq.front()]; 
}
```


# Python
```python
from collections import deque

nums = [1, 3, 5, 7, 4, 5, 9, 5]
k = 4
min_range = []
queue = deque([])

print(queue)

for i in range(len(nums)):
    while queue and nums[queue[-1]] >= nums[i]:
        queue.pop()

    queue.append(i)

    if queue[0] + k <= i:
        queue.popleft()

    if i >= k-1:
        min_range.append(nums[queue[0]])

    print(queue, min_range)

```

Ví dụ trên là slide trên array.


Ở bài 1696. Jump Game VI

Nếu chỉ dùng Dp mà ko sử dụng deque ta sẽ có code dp bottom-up như sau:



```python
from typing import List
from math import inf

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            max_res = -inf

            for j in range(max(0, i-k), i):
                max_res = max(max_res, dp[j])

            dp[i] = max_res + nums[i]

        return dp[len(nums)-1]

```

Mỗi vòng lặp i lại có k vòng lặp bên trong. Nên độ phức tạo là O(NK).

## Áp dụng Deque
Vì cách sử dụng DP phía trên lặp lại khá nhiều các đoạn overlap giữa 2 lần loop liên tiếp các đoạn dp[i-k, i-1] và dp[i-k+1, i].

Sử dụng tư tưởng dùng deque, ta sẽ lấy 1 deque để lưu các slide-k của dp[i]. Chỉ lấy các phần tử lớn nhất trong một slide-k. Như vậy thì ta không cần loop dp từ i-k đến i-1 để tìm phần tử lớn nhất trong đó nữa, mà chỉ cần truy xuất ngay queue[0].


```python
from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = [0] * n
        score[0] = nums[0]
        dq = deque()
        dq.append(0)
        for i in range(1, n):
            # pop the old index
            while dq and dq[0] < i - k:
                dq.popleft()
            score[i] = score[dq[0]] + nums[i]
            # pop the smaller value
            while dq and score[i] >= score[dq[-1]]:
                dq.pop()
            dq.append(i)
        return score[-1]
```
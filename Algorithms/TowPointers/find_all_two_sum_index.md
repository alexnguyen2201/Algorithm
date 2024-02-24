cho dãy xắp sếp tăng dần, và một target:
nums = [1, 2, 2, 7, 7, 8, 8, 11, 15]
target = 9

Liệt kê tất cả các cặp chỉ số, mà có tổng bằng 9?
output = [[0,5], [0,6], [1,4], [1,3], [2,4], [2,3]]

worst case still N^2 vi:

ví dụ n/2và n/2 thì sẽ có n^2/4 = O(N^2) kết quả = target nên ko có O(N) thật

nhưng nếu các case là khác nhau nhiều thì dùng hash map rất có lợi, xấp xỉ O(N)

```python
res = []
seen = defaultdict(list)

for i, value in enumerate(nums):
    remain = target - value
    if remain in seen:
        result.extend([[idx, i] for idx in seen[remain]])
    else:
        seen[value].append(i)

return result
```
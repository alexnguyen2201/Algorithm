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

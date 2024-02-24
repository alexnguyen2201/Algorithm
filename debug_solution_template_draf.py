from lctest import *


@testcase(
    log(3, [1, 5], [2])
)
class Solution:

    @solution
    def sol(self, houses, heaters):

        def check(m):
            if m == 1:
                print('3 here!')
            p1 = 0
            # flag = True
            for i in heaters:
                begin = i - m
                end = i + m
                if houses[p1] < begin:
                    return False
                else:
                    while p1 < n and houses[p1] <= end:
                        p1 += 1
                if p1 >= n:
                    break
            if houses[p1] > end:
                return False
            return True

        houses.sort()
        heaters.sort()
        n = len(houses)
        left = 0
        right = 1000000000

        while left < right:
            mid = left + (right - left) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return right




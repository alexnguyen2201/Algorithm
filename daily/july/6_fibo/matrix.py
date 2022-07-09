from dataclasses import dataclass


@dataclass
class Mat2x2:
    m00: int
    m01: int
    m10: int
    m11: int

    def mult(self, b):
        return Mat2x2(
            self.m00 * b.m00 + self.m01 * b.m10,
            self.m00 * b.m01 + self.m01 * b.m11,
            self.m10 * b.m00 + self.m11 * b.m10,
            self.m10 * b.m01 + self.m11 * b.m11
        )

    def pow(self, n: int):
        res = Mat2x2(1, 1, 1, 0)

        while n > 0:
            if n & 1:
                res = res.mult(self)

            n >>= 1
            self = self.mult(self)

        return res


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1

        base = Mat2x2(1, 1, 1, 0)
        p = base.pow(n-2)
        return p.m00

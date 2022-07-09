from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def isInterleaveRecursive(i1=0, i2=0) -> bool:
            return i1 + i2 == len(s3) \
                or (i1 < len(s1) and s1[i1] == s3[i1+i2]
                    and isInterleaveRecursive(i1+1, i2)) \
                or (i2 < len(s2) and s2[i2] == s3[i1+i2]
                    and isInterleaveRecursive(i1, i2+1))
        return isInterleaveRecursive()

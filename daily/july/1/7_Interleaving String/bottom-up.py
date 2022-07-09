class Solution:
    def isInterleave(self, s1,  s2,  s3):

        if len(s3) != len(s1) + len(s2):
            return False

        dp = [
            [False] * (len(s2) + 1) for _ in range(len(s1) + 1)
        ]

        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                else:
                    dp[i][j] = (
                        (
                            dp[i - 1][j]
                            and s1[i - 1] == s3[i + j - 1])
                        or (
                            dp[i][j - 1] and
                            s2[j - 1] == s3[i + j - 1]
                        )
                    )

        return dp[len(s1)][len(s2)]

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def check(word):
            left = 0
            right = len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1

            return True

        res = 0
        res_str = ''

        output = ['']

        for i in s:
            output += [curr + i for curr in output]

        print(output)
        print(len(output))

        for item in output:
            if check(item) and len(item) >= res:
                res = len(item)
                res_str = item

        print(res_str)
        return res


s = Solution()
print(s.longestPalindromeSubseq("nwlrbbmqbh"))
print(s.longestPalindromeSubseq("nwlrbbmqbh"))

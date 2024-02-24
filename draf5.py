class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        flag = True
        begin = end = 0
        match_len = 0

        while end < len(s):
            c = s[end]
            hm[c] = hm.get(c, 0) + 1
            if hm[c] > 1:
                flag = False
            end += 1

            while not flag:
                tempc = s[begin]
                if tempc in hm:
                    hm[tempc] -= 1
                    if hm[tempc] == 1:
                        flag = True
                begin += 1

            match_len = max(end - begin, match_len)

        return match_len

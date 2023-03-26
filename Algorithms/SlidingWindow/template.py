import math


class Solution:
    def slidingWindowTemplateByNguyenSon(self, s: str, t: str):
        result = []
        if len(t) > len(s):
            return result

        # create a hashmap to save the Characters of the target substring.
        # (K, V) = (Character, Frequency of the Characters)
        hm = {}
        for c in t:
            hm[c] = hm.get(c, 0) + 1

        counter = len(hm)

        # Two pointers: begin - left pointer of the window; end - right pointer of the window
        begin = end = 0

        # the length of the substring which match the target string.
        match_len = math.inf

        while end < len(s):
            c = s[end]

            if c in hm:
                hm[c] -= 1 # plus or minus one
                if hm[c] == 0: counter -= 1 # modify the counter the requirement (different condition).

            end += 1

            while counter == 0: # counter condition. different question may have different condition

                tempc = s[begin]
                if tempc in hm:
                    hm[tempc] += 1 # plus or minus one
                    if hm[tempc] > 0:
                        counter += 1 # modify the counter according the requirement (different condition).

                    # save / update(min/max) the result if find a target
                    # result collections or result int value

                begin += 1

            return result





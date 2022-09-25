class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        arr = 0
        for num in data:
            if 0 <= num <= 127:
                continue
            elif num <= 191:
                arr -= 1
            elif num <= 223:
                arr += 1
            elif num <= 239:
                arr += 2
            elif num <= 247:
                arr += 3
            elif num > 247:
                arr += inf

        return arr == 0

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        has_changed = True
        while(has_changed):
            has_changed = False
            for i in range(0, len(ratings)):
                if(
                    i < len(ratings) - 1
                    and ratings[i] > ratings[i+1]
                    and candies[i] <= candies[i+1]
                ):
                    candies[i] = candies[i+1] + 1
                    has_changed = True
                if(
                    i > 0
                    and ratings[i] > ratings[i-1]
                    and candies[i] <= candies[i-1]
                ):
                    candies[i] = candies[i-1] + 1
                    has_changed = True
        return sum([candy for candy in candies])

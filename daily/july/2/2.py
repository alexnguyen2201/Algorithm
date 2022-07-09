class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        M = 1000000007

        horizontalCuts = [0, *horizontalCuts, h]
        verticalCuts = [0, *verticalCuts, w]

        horizontalCuts.sort()
        verticalCuts.sort()

        max_horizontal_edge = max(horizontalCuts[i] - horizontalCuts[i-1]
                                  for i in range(1, len(horizontalCuts)))

        max_vertical_edge = max(verticalCuts[i] - verticalCuts[i-1]
                                for i in range(1, len(verticalCuts)))

        return ((max_horizontal_edge % M) * (max_vertical_edge % M)) % M

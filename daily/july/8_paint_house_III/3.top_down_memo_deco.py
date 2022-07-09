from functools import cache


class Solution:

    def minCost(self, houses, cost, m, n, target):
        MAX_COST = 1000001

        @cache
        def find_min_cost(curr_index, neighbors_cnt, prev_color):
            if curr_index == len(houses):
                return 0 if neighbors_cnt == target else MAX_COST

            if neighbors_cnt > target:
                return MAX_COST

            min_cost = MAX_COST

            if houses[curr_index] != 0:
                new_neighbors_cnt = neighbors_cnt + \
                    (0, 1)[houses[curr_index] != prev_color]
                min_cost = find_min_cost(
                    curr_index + 1, new_neighbors_cnt, houses[curr_index])

            else:
                for color in range(1, len(cost[0])+1):
                    new_neighbors_cnt = neighbors_cnt + \
                        (0, 1)[color != prev_color]
                    curr_cost = cost[curr_index][color-1] + \
                        find_min_cost(curr_index+1, new_neighbors_cnt, color)
                    min_cost = min(min_cost, curr_cost)

            return min_cost

        answer = find_min_cost(0, 0, 0)
        return (answer, -1)[answer == MAX_COST]

# flake8: noqa


class Solution:

    def minCost(self, houses, cost, m, n, target):

        memo = [[[None for _ in range(21)]
                 for _ in range(100)] for _ in range(100)]
        MAX_COST = 1000001

        def find_min_cost(curr_index: int, neighbors_cnt: int, prev_color: int):

            if curr_index == len(houses):
                return 0 if neighbors_cnt == target else MAX_COST

            if neighbors_cnt > target:
                return MAX_COST

            print(curr_index, neighbors_cnt, prev_color)
            if memo[curr_index][neighbors_cnt][prev_color] is not None:
                return memo[curr_index][neighbors_cnt][prev_color]

            min_cost = MAX_COST

            # Nếu nhà tại index này đã tô màu -> update neighbors_cnt và prev_color
            if houses[curr_index] != 0:
                new_neighbors_cnt = neighbors_cnt + \
                    (0, 1)[houses[curr_index] != prev_color]
                min_cost = find_min_cost(
                    curr_index + 1, new_neighbors_cnt, houses[curr_index])

            # Nếu nhà tại index này chưa tô màu -> tô từ màu 1 đến màu cuối
            else:
                for color in range(1, len(cost[0])+1):
                    print(curr_index, color)
                    new_neighbors_cnt = neighbors_cnt + \
                        (0, 1)[color != prev_color]
                    curr_cost = cost[curr_index][color-1] + \
                        find_min_cost(curr_index+1, new_neighbors_cnt, color)
                    min_cost = min(min_cost, curr_cost)

            memo[curr_index][neighbors_cnt][prev_color] = min_cost
            return min_cost

        answer = find_min_cost(0, 0, 0)
        return (answer, -1)[answer == MAX_COST]

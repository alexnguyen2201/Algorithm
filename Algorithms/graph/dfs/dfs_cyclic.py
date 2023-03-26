# https://leetcode.com/problems/longest-cycle-in-a-graph/description/

class Solution(object):
    def longestCycle(self, edges):
        from collections import defaultdict
        G = defaultdict(list)
        for i, v in enumerate(edges):
            G[i].append(v)

        def dfs(node):
            nonlocal answer
            visit[node] = 1
            for nei in G[node]:
                if nei != -1 and not visit[nei]:
                    dist[nei] = dist[node] + 1
                    dfs(nei)
                else:
                    if nei in dist:
                        answer = max(answer, dist[node] - dist[nei] + 1)

        n = len(edges)
        visit = [0] * n
        answer = -1

        for node in range(n):
            if not visit[node]:
                dist = {}  # for each connected components
                dist[node] = 1
                dfs(node)
        return answer

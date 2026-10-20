# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=R2sjm5jfwYY
# iPad PDF Notes              : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/iPad%20PDF%20Notes/Leetcode-1615-Maximal%20Network%20Rank.pdf
# Company Tags                : MICROSOFT
# Leetcode Link               : https://leetcode.com/problems/maximal-network-rank/

from collections import defaultdict
from typing import List

# ************************************************ C++ ********************************************************
# Approach-1 (Simply checking each pair of nodes) - O(V^2)
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)  # unordered_map<int, unordered_set<int>>

        for road in roads:
            u = road[0]
            v = road[1]

            adj[u].add(v)
            adj[v].add(u)

        maxRank = 0

        for i in range(n):
            for j in range(i+1, n):

                i_rank = len(adj[i])
                j_rank = len(adj[j])

                rank = i_rank + j_rank

                if j in adj[i]:
                    rank -= 1

                maxRank = max(maxRank, rank)

        return maxRank

Approach1 = Solution


# Approach-2 (Using degree count & keeping a check if nodes are connected) - T.C. (O(V^2))
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        connected = [[False] * n for _ in range(n)]

        for road in roads:
            u = road[0]
            v = road[1]

            degree[u] += 1
            degree[v] += 1

            connected[u][v] = True
            connected[v][u] = True

        maxRank = 0

        for i in range(n):
            for j in range(i+1, n):

                i_rank = degree[i]
                j_rank = degree[j]

                rank = i_rank + j_rank

                if connected[i][j] or connected[j][i]:
                    rank -= 1

                maxRank = max(maxRank, rank)

        return maxRank

Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]]) == 4
        assert S().maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]) == 5
        assert S().maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]) == 5
    print("ok")

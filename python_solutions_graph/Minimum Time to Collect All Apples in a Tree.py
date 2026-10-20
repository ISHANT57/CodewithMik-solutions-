# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=qSBvKlUq0xo
# Company Tags                : Microsoft
# Leetcode Link               : https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

from typing import List
from collections import defaultdict


# DFS - O(V+E) - We visit all nodes and edges in the graph
class Solution:
    def DFS(self, adj, curr: int, parent: int, hasApple: List[bool]) -> int:
        time = 0

        for child in adj[curr]:
            if child == parent:
                continue

            time_from_bachha_log = self.DFS(adj, child, curr, hasApple)

            if time_from_bachha_log or hasApple[child]:
                time += 2 + time_from_bachha_log

        return time

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)

        for vec in edges:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        return self.DFS(adj, 0, -1, hasApple)


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]) == 8
    assert Solution().minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False]*7) == 0
    print("ok")

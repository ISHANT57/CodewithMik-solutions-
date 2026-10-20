# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=42Z0eaopoZ8
# Company Tags                : META
# Leetcode Link               : https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

import sys
from typing import List

sys.setrecursionlimit(10 ** 6)


# DFS - Using Visited Array
class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, parent, adj, visited):
        visited[node] = True

        for child, sign in adj[node]:
            if not visited[child]:
                self.count += sign
                self.dfs(child, node, adj, visited)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], 0))
        visited = [False] * n
        self.dfs(0, -1, adj, visited)
        return self.count


Approach1 = Solution


# DFS - Without using Visited Array because there will be no cycle and hence this is undirected graph
class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, parent, adj):
        for child, sign in adj[node]:
            if child != parent:
                self.count += sign
                self.dfs(child, node, adj)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for connection in connections:
            adj[connection[0]].append((connection[1], 1))
            adj[connection[1]].append((connection[0], 0))

        self.dfs(0, -1, adj)
        return self.count


Approach2 = Solution


# BFS - Soon


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
        assert S().minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
        assert S().minReorder(3, [[1, 0], [2, 0]]) == 0
    print("ok")

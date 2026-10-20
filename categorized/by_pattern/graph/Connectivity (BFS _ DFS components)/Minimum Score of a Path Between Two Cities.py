# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ZsGTpXm966E
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

# LEETCODE WEEKLY CONTEST - 322

from typing import List
from collections import defaultdict


# DFS
class Solution:
    def dfs(self, adj, u: int, visited: List[bool], result: List[int]) -> None:
        # result is a one-element list to emulate C++ reference (int &result)

        visited[u] = True

        for vec in adj[u]:
            v = vec[0]
            c = vec[1]

            result[0] = min(result[0], c)

            if not visited[v]:
                self.dfs(adj, v, visited, result)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)  # unordered_map<int, vector<pair<int, int>>>

        for vec in roads:

            u = vec[0]
            v = vec[1]
            c = vec[2]

            adj[u].append((v, c))
            adj[v].append((u, c))

        result = [2**31 - 1]  # INT_MAX
        # NOTE: C++ visited has size n and is indexed by 1-based city ids; here size n+1 avoids
        # out-of-range indexing (C++ was lenient about it).
        visited = [False] * (n + 1)
        self.dfs(adj, 1, visited, result)

        return result[0]


Approach1 = Solution

# BFS soon
# Also, Union Find approach will be provided soon in Union Find sub-repo


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    assert Solution().minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]) == 5
    assert Solution().minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2
    print("ok")

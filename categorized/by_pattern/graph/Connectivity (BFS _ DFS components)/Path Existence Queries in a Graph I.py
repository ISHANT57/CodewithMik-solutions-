# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=jMCxNXLHKGE
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/path-existence-queries-in-a-graph-i
# (Java duplicate sections of the original file are skipped)

import sys
from typing import List
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


# ***************************************************** C++ (Python port) *****************************************************
# Approach-1 (Using DFS for each query) - TLE
# T.C : O(q * (V+E)), q = number of queries, V + E is for DFS, V = number of vertices, E = number of edges
# S.C : O(V+E), V = number of vertices, E = number of edges
class Solution:
    def dfs(self, cur, target, adj, visited):
        if cur == target:
            return True

        visited[cur] = True

        for ngbr in adj[cur]:
            if not visited[ngbr]:
                if self.dfs(ngbr, target, adj, visited):
                    return True

        return False

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                adj[i].append(i + 1)
                adj[i + 1].append(i)

        result = []
        for query in queries:
            u = query[0]
            v = query[1]
            visited = [False] * n
            result.append(self.dfs(u, v, adj, visited))
        return result


Approach1 = Solution


# Approach-2 (Using DFS once and then mark component) - TLE
# T.C : O((V+E) + q), V + E is for DFS, V = number of vertices, E = number of edges
# S.C : O(V+E), V = number of vertices, E = number of edges
class Solution:
    def dfs(self, cur, compId, adj, component):
        component[cur] = compId
        for ngbr in adj[cur]:
            if component[ngbr] == -1:
                self.dfs(ngbr, compId, adj, component)

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                adj[i].append(i + 1)
                adj[i + 1].append(i)

        component = [-1] * n
        compId = 0
        for i in range(n):
            if component[i] == -1:
                self.dfs(i, compId, adj, component)
                compId += 1

        result = []
        for query in queries:
            result.append(component[query[0]] == component[query[1]])
        return result


Approach2 = Solution


# Approach-3 (Simple observation - assign components)
# T.C : O(n+q)
# S.C : O(n)
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [-1] * n
        compId = 0
        component[0] = compId
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                compId += 1
            component[i] = compId

        result = []
        for query in queries:
            result.append(component[query[0]] == component[query[1]])
        return result


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().pathExistenceQueries(2, [1, 3], 1, [[0, 0], [0, 1]]) == [True, False]
        assert S().pathExistenceQueries(4, [2, 5, 6, 8], 2, [[0, 1], [0, 2], [1, 3], [2, 3]]) == [False, False, True, True]
    print("ok")

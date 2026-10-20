# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=m6cp4eHWLak
# Company Tags                : <soon>
# Leetcode Link               : https://leetcode.com/problems/longest-cycle-in-a-graph/

from typing import List


# Using DFS (Just using "Cycle Detection in Directed Graph using DFS" code)
class Solution:
    def __init__(self):
        self.result = -1

    def dfs(self, u: int, edges: List[int], visited: List[bool], dist: List[int], inRecursion: List[bool]) -> None:

        if u != -1:

            visited[u] = True
            inRecursion[u] = True

            v = edges[u]

            if v != -1 and not visited[v]:

                dist[v] = dist[u] + 1

                self.dfs(v, edges, visited, dist, inRecursion)

            elif v != -1 and inRecursion[v] == True:  # cycle

                self.result = max(self.result, dist[u] - dist[v] + 1)

            inRecursion[u] = False

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        visited = [False] * n

        dist = [1] * n
        inRecursion = [False] * n

        for i in range(n):

            if not visited[i]:
                self.dfs(i, edges, visited, dist, inRecursion)

        return self.result


Approach1 = Solution

# Using BFS - (Kahn's Algo) - Soon


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    assert Solution().longestCycle([3, 3, 4, 2, 3]) == 3
    assert Solution().longestCycle([2, -1, 3, 1]) == -1
    print("ok")

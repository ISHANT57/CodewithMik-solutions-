#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=NS3C4W_jJJM
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid

from typing import List
import heapq

INT_MAX = 2**31 - 1

# Approach-1 (Backtracking DFS to try all paths) - TLE
# T.C : O(4^(m*n))
# S.C : O(m*n)
class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.m = 0
        self.n = 0

    def dfs(self, i: int, j: int, grid: List[List[int]], visited: List[List[bool]], cost: int) -> int:
        if i == self.m-1 and j == self.n-1:  # reached destination
            return cost

        visited[i][j] = True

        # explore
        minCost = INT_MAX
        for dir_i in range(4):
            i_ = i + self.dir[dir_i][0]
            j_ = j + self.dir[dir_i][1]

            if i_ >= 0 and i_ < self.m and j_ >= 0 and j_ < self.n and not visited[i_][j_]:
                nextCost = cost + (1 if (grid[i][j]-1 != dir_i) else 0)

                minCost = min(minCost, self.dfs(i_, j_, grid, visited, nextCost))

        visited[i][j] = False
        return minCost

    def minCost(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        visited = [[False] * self.n for _ in range(self.m)]

        return self.dfs(0, 0, grid, visited, 0)  # explore all paths by backtracking

Approach1 = Solution


# Approach-2 (Dijkstra's Algorithm) - Accepted
# T.C : O((m*n) * log(m*n))
# S.C : O(m*n)
class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        pq = []  # min-heap of int
        result = [[INT_MAX] * n for _ in range(m)]

        heapq.heappush(pq, [0, 0, 0])
        result[0][0] = 0
        # T.C : O(m*n * log(m*n))
        # S.C : O(m*n)
        while pq:
            curr = heapq.heappop(pq)  # log(size of pq)

            currCost = curr[0]
            i = curr[1]
            j = curr[2]

            if result[i][j] < currCost:
                continue

            for dir_i in range(4):
                i_ = i + self.dir[dir_i][0]
                j_ = j + self.dir[dir_i][1]

                if i_ >= 0 and j_ >= 0 and i_ < m and j_ < n:
                    gridDir = grid[i][j]
                    dirCost = 1 if (gridDir-1 != dir_i) else 0

                    newCost = currCost + dirCost

                    if newCost < result[i_][j_]:
                        result[i_][j_] = newCost
                        heapq.heappush(pq, [newCost, i_, j_])
        return result[m-1][n-1]  # min cost to reach (m-1, n-1)

Approach2 = Solution


if __name__ == "__main__":
    g1 = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
    g2 = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
    g3 = [[1, 2], [4, 3]]
    for sol in (Approach1, Approach2):
        assert sol().minCost(g1) == 3
        assert sol().minCost(g2) == 0
        assert sol().minCost(g3) == 1
    print("ok")

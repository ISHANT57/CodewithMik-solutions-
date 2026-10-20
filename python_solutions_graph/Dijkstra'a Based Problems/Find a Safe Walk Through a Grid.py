# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ZIFAFLARoLs
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/find-a-safe-walk-through-a-grid

from typing import List
from collections import deque
import heapq

INT_MAX = 2**31 - 1


# Appoach-1 Using Dijkstra's
# T.C : O(E * log V) = O(m*n * log(m*n))
# S.C : O(m*n)
class Solution:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # typedef pair<int, pair<int,int>> P; -> tuple (d, (r, c))

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        pq = []  # min-heap via heapq (greater<P>)

        result = [[INT_MAX] * n for _ in range(m)]

        result[0][0] = grid[0][0]  # Source = {0, 0}
        heapq.heappush(pq, (result[0][0], (0, 0)))

        while pq:
            d, cell = heapq.heappop(pq)
            r, c = cell

            if d > result[r][c]:
                continue

            for dir in self.directions:
                nr = r + dir[0]
                nc = c + dir[1]

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if d + grid[nr][nc] < result[nr][nc]:
                    result[nr][nc] = d + grid[nr][nc]
                    heapq.heappush(pq, (d + grid[nr][nc], (nr, nc)))

        return health - result[m - 1][n - 1] >= 1


Approach1 = Solution


# Appoach-2 (Using 0-1 BFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        result = [[INT_MAX] * n for _ in range(m)]
        dq = deque()

        result[0][0] = grid[0][0]  # source {0, 0}
        dq.appendleft((0, 0))

        while dq:
            r, c = dq.popleft()

            for dir in self.directions:
                nr = r + dir[0]
                nc = c + dir[1]

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if result[r][c] + grid[nr][nc] < result[nr][nc]:

                    result[nr][nc] = result[r][c] + grid[nr][nc]

                    if grid[nr][nc] == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

        return health - result[m - 1][n - 1] >= 1


Approach2 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2):
        assert A().findSafeWalk([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 1) == True
        assert A().findSafeWalk([[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], 3) == False
        assert A().findSafeWalk([[1,1,1],[1,0,1],[1,1,1]], 5) == True
    print("ok")

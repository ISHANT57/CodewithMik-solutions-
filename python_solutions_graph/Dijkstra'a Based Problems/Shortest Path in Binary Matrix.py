# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=XsF-Xj_y5x8
# Company Tags                : Google, Meta, Microsoft, Amazon
# Leetcode Link               : https://leetcode.com/problems/shortest-path-in-binary-matrix/

from typing import List
import heapq
from collections import deque

INT_MAX = 2**31 - 1


# Approach-1 (Using BFS - Works because all edges are of weight = 1)
class Solution:
    directions = [[1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0 or grid[0][0] != 0:
            return -1

        que = deque()
        que.append((0, 0))
        grid[0][0] = 1

        def isSafe(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        steps = 1

        while que:
            N = len(que)
            while N > 0:
                N -= 1
                curr = que.popleft()
                x = curr[0]
                y = curr[1]

                if x == m - 1 and y == n - 1:
                    return steps

                for dir in self.directions:
                    x_ = x + dir[0]
                    y_ = y + dir[1]

                    if isSafe(x_, y_) and grid[x_][y_] == 0:
                        que.append((x_, y_))
                        grid[x_][y_] = 1
            steps += 1

        return -1


Approach1 = Solution


# Approach-2 (Using Dijkstra's Algorithm) - Using Priority_queue (min-heap)
class Solution:
    directions = [[1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0 or grid[0][0] != 0:
            return -1

        def isSafe(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        result = [[INT_MAX] * n for _ in range(m)]
        pq = []  # min heap of (d, (x, y))

        heapq.heappush(pq, (0, (0, 0)))
        result[0][0] = 0

        while pq:
            d, node = heapq.heappop(pq)

            x = node[0]
            y = node[1]

            for dir in self.directions:
                x_ = x + dir[0]
                y_ = y + dir[1]
                dist = 1

                if isSafe(x_, y_) and grid[x_][y_] == 0 and d + dist < result[x_][y_]:
                    heapq.heappush(pq, (d + dist, (x_, y_)))
                    grid[x_][y_] = 1
                    result[x_][y_] = d + dist

        if result[m - 1][n - 1] == INT_MAX:
            return -1

        return result[m - 1][n - 1] + 1


Approach2 = Solution


# Approach-3 (Using Dijkstra's Algorithm) - Using queue (min-heap)
# This works because every weight is 1 and it will be similar to min-heap only
class Solution:
    directions = [[1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0 or grid[0][0] != 0:
            return -1

        def isSafe(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        result = [[INT_MAX] * n for _ in range(m)]
        pq = deque()

        pq.append((0, (0, 0)))
        result[0][0] = 0

        while pq:
            d, node = pq.popleft()

            x = node[0]
            y = node[1]

            for dir in self.directions:
                x_ = x + dir[0]
                y_ = y + dir[1]
                dist = 1

                if isSafe(x_, y_) and grid[x_][y_] == 0 and d + dist < result[x_][y_]:
                    pq.append((d + dist, (x_, y_)))
                    grid[x_][y_] = 1
                    result[x_][y_] = d + dist

        if result[m - 1][n - 1] == INT_MAX:
            return -1

        return result[m - 1][n - 1] + 1


Approach3 = Solution


if __name__ == "__main__":
    for sol in (Approach1, Approach2, Approach3):
        assert sol().shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
        assert sol().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
        assert sol().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    print("ok")

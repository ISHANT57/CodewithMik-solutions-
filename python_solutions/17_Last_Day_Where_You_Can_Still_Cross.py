# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=U4C7-PF_fi8
# Company Tags                : GOOGLE (on site interview), META
# Leetcode Link               : https://leetcode.com/problems/last-day-where-you-can-still-cross/solution/

import sys
from collections import deque
from typing import List

sys.setrecursionlimit(1000000)  # Approach-1 DFS can recurse deeply


# Approach-1 (Using Binary Search + DFS)
class Solution:
    def __init__(self):
        self.ROW = 0
        self.COL = 0
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(self, grid: List[List[int]], i: int, j: int) -> bool:

        if i < 0 or i >= self.ROW or j < 0 or j >= self.COL or grid[i][j] == 1:
            return False

        if i == self.ROW - 1:
            return True

        grid[i][j] = 1
        for dir in self.directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if self.dfs(grid, new_i, new_j):
                return True

        return False

    def canCross(self, cells: List[List[int]], day: int) -> bool:
        grid = [[0] * self.COL for _ in range(self.ROW)]

        for i in range(day + 1):
            r = cells[i][0] - 1
            c = cells[i][1] - 1

            grid[r][c] = 1

        for j in range(self.COL):
            if grid[0][j] == 0 and self.dfs(grid, 0, j):
                return True
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.ROW = row
        self.COL = col
        grid = [[0] * col for _ in range(row)]

        n = len(cells)

        l = 0
        r = len(cells) - 1
        lastDay = 0

        while l <= r:

            mid = l + (r - l) // 2

            if self.canCross(cells, mid):
                lastDay = mid + 1
                l = mid + 1
            else:
                r = mid - 1

        return lastDay


Approach1 = Solution  # alias so both approaches can be tested below


# Approach-2 (Binary Search + BFS)
class Solution:
    def __init__(self):
        self.ROW = 0
        self.COL = 0
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(self, grid: List[List[int]], i: int, j: int) -> bool:

        que = deque()
        que.append((i, j))
        grid[i][j] = 1

        while que:

            temp = que.popleft()

            x = temp[0]
            y = temp[1]

            if x == self.ROW - 1:
                return True

            for dir in self.directions:

                new_x = x + dir[0]
                new_y = y + dir[1]

                if 0 <= new_x < self.ROW and 0 <= new_y < self.COL and grid[new_x][new_y] == 0:
                    que.append((new_x, new_y))
                    grid[new_x][new_y] = 1

        return False

    def canCross(self, cells: List[List[int]], day: int) -> bool:
        grid = [[0] * self.COL for _ in range(self.ROW)]

        for i in range(day + 1):
            r = cells[i][0] - 1
            c = cells[i][1] - 1

            grid[r][c] = 1

        for j in range(self.COL):
            if grid[0][j] == 0 and self.bfs(grid, 0, j):
                return True
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.ROW = row
        self.COL = col

        n = len(cells)

        l = 0
        r = len(cells) - 1
        lastDay = 0

        while l <= r:

            mid = l + (r - l) // 2

            if self.canCross(cells, mid):
                lastDay = mid + 1
                l = mid + 1
            else:
                r = mid - 1

        return lastDay


Approach2 = Solution


# Approach-3 (Using Union Find)
# Will soon upload in Union Find repo


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        s = S()
        assert s.latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]) == 2
        assert S().latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 1
        assert S().latestDayToCross(3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]) == 3
    print("ok")

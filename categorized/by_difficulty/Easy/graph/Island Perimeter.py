# MY YOUTUBE VIDEO ON THIS Qn :
# Company Tags                : Google
# Leetcode Link               : https://leetcode.com/problems/island-perimeter/

import copy
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(10**6)

# Approach-1 (DFS)
# T.C : O(m*n)
# S.C : O(1) Auxiliary Space
class Solution:

    def dfs(self, grid: List[List[int]], i: int, j: int) -> None:

        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0:
            self.peri += 1
            return

        if grid[i][j] == -1:
            return

        grid[i][j] = -1  # mark visited

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.peri = 0

        for i in range(self.m):
            for j in range(self.n):

                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    return self.peri

        return -1

Approach1 = Solution


# Approach-2 (BFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(self, grid: List[List[int]], i: int, j: int) -> int:
        perim = 0

        que = deque()  # queue of (i, j) tuples
        que.append((i, j))
        grid[i][j] = -1

        while que:

            it = que.popleft()

            # it[0] = i
            # it[1] = j

            for dir in self.directions:
                i_ = it[0] + dir[0]
                j_ = it[1] + dir[1]

                if i_ < 0 or i_ >= self.m or j_ < 0 or j_ >= self.n or grid[i_][j_] == 0:
                    perim += 1
                elif grid[i_][j_] == -1:
                    continue
                else:
                    que.append((i_, j_))
                    grid[i_][j_] = -1

        return perim

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        for i in range(self.m):
            for j in range(self.n):

                if grid[i][j] == 1:
                    return self.bfs(grid, i, j)

        return -1

Approach2 = Solution


# Approach-3 (Iterative)
# T.C : O(m*n)
# S.C : O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                if i-1 < 0 or grid[i-1][j] == 0:  # up
                    perimeter += 1

                if i+1 >= m or grid[i+1][j] == 0:  # down
                    perimeter += 1

                if j-1 < 0 or grid[i][j-1] == 0:  # left
                    perimeter += 1

                if j+1 >= n or grid[i][j+1] == 0:  # right
                    perimeter += 1

        return perimeter

Approach3 = Solution


if __name__ == "__main__":
    g = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    for S in (Approach1, Approach2, Approach3):
        assert S().islandPerimeter(copy.deepcopy(g)) == 16
        assert S().islandPerimeter([[1]]) == 4
        assert S().islandPerimeter([[1,0]]) == 4
    print("ok")

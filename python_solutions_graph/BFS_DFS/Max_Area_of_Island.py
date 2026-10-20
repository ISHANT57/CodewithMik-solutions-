# Company Tags  : Amazon
# Leetcode Link : https://leetcode.com/problems/max-area-of-island/
#
# NOTE : "Disjoint Set Union" can be used to solve this too. It will help to clear concept of Disjoin Set Data Structure
# Find the Disjoint Set Union approach here : "Interview_DS_Algo/Graph/Disjoin Set"  repository
# Link  : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Disjoin%20Set/Max%20Area%20of%20Island.cpp

from typing import List
from collections import deque


# Approach-1 (DFS)
class Solution:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(self, grid: List[List[int]], i: int, j: int, m: int, n: int) -> int:
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0

        count = 1
        grid[i][j] = 0
        for dir in self.directions:
            i_ = i + dir[0]
            j_ = j + dir[1]
            count += self.dfs(grid, i_, j_, m, n)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j, m, n))

        return maxArea


Approach1 = Solution


# Approach-2 (BFS)
class Solution:
    # P = pair<int, int> -> tuple
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        que = deque()
        que.append((i, j))
        grid[i][j] = 0
        size = 0

        def isSafe(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == 1

        while que:
            curr = que.popleft()
            size += 1

            for dir in self.directions:
                x = curr[0] + dir[0]
                y = curr[1] + dir[1]

                if isSafe(x, y):
                    grid[x][y] = 0
                    que.append((x, y))
        return size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        result = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    result = max(result, self.bfs(i, j, grid))

        return result


Approach2 = Solution


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    import copy
    assert Approach1().maxAreaOfIsland(copy.deepcopy(g)) == 6
    assert Approach2().maxAreaOfIsland(copy.deepcopy(g)) == 6
    assert Approach1().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    print("ok")

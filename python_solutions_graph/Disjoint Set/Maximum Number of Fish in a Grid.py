# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=kfs9vzv7kHc
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

from typing import List
from collections import deque


########################################## Python (converted from C++) ##########################################
# Approach-1 (Using DSU)
# T.C : O(m*n * alpha(m*n))
# S.C : O(m*n)
class DSU:
    def __init__(self, n: int):  # size of parent and size array
        self.parent = [0] * n
        self.size = [0] * n

        for i in range(n):
            self.parent[i] = i
            self.size[i] = 0  # fis count ios 0 initially for each

    # find the parent of x
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:  # both already in same group
            return

        if self.size[x_parent] > self.size[y_parent]:
            self.parent[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        else:
            self.parent[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]

    def setSize(self, x: int, fishCount: int) -> None:
        self.size[x] = fishCount

    def getMaxFishCount(self) -> int:
        return max(self.size)


class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        totalCells = m * n

        dsu = DSU(totalCells)
        # DSU = alpha(totalCells)

        # Initialize size array with initial fish count of each cell
        # O(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    idx = i * n + j
                    dsu.setSize(idx, grid[i][j])

        # O(m*n * alpha(m*n))
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    idx = i * n + j  # parent ka index milgaya
                    for dir in self.directions:
                        i_ = i + dir[0]
                        j_ = j + dir[1]
                        if i_ >= 0 and i_ < m and j_ >= 0 and j_ < n and grid[i_][j_] > 0:
                            idx_ = i_ * n + j_  # parent ka index
                            dsu.Union(idx, idx_)

        return dsu.getMaxFishCount()


Approach1 = Solution


# Approach-2 (Using BFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def bfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        que = deque()  # queue<pair<int,int>>
        que.append((i, j))
        fishCount = grid[i][j]
        grid[i][j] = 0

        while que:
            i, j = que.popleft()

            for dir in self.directions:
                i_ = dir[0] + i
                j_ = dir[1] + j

                if i_ >= 0 and j_ >= 0 and i_ < self.m and j_ < self.n and grid[i_][j_] > 0:
                    que.append((i_, j_))
                    fishCount += grid[i_][j_]
                    grid[i_][j_] = 0

        return fishCount

    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        maxFish = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] > 0:  # water cell found
                    maxFish = max(maxFish, self.bfs(i, j, grid))

        return maxFish


Approach2 = Solution


# Approach-3 (Using DFS)
# T.C : O(m*n * alpha(m*n))
# S.C : O(m*n)
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def dfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0:
            return 0

        fishCount = grid[i][j]
        grid[i][j] = 0  # took the fish from this cell

        for dir in self.directions:
            i_ = i + dir[0]
            j_ = j + dir[1]

            fishCount += self.dfs(i_, j_, grid)

        return fishCount

    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        maxFish = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] > 0:  # water cell found
                    maxFish = max(maxFish, self.dfs(i, j, grid))

        return maxFish


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]) == 7
        assert S().findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == 1
    print("ok")

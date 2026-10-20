# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=iCAC-QrQ-4A
# Company Tags                : Google, Uber
# Leetcode Link               : https://leetcode.com/problems/making-a-large-island/

from typing import List


# ********************************************************************** C++ **********************************************************************
# Approach - 1 - Brute Force DFS (you can do BFS as well)
# T.C : O(n^4)
# S.C : O(n^2)
class Solution:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def DFS(self, grid: List[List[int]], i: int, j: int, visited: List[List[bool]]) -> int:
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0 or visited[i][j]:
            return 0

        visited[i][j] = True
        count = 1

        for dir in self.directions:
            count += self.DFS(grid, i + dir[0], j + dir[1], visited)

        return count

    def findLargestIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        m, n = self.m, self.n
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # Try converting each 0 to 1
                    grid[i][j] = 1

                    visited = [[False] * n for _ in range(m)]
                    largest = 0

                    for x in range(m):
                        for y in range(n):
                            if grid[x][y] == 1 and not visited[x][y]:
                                largest = max(largest, self.DFS(grid, x, y, visited))

                    maxArea = max(maxArea, largest)
                    grid[i][j] = 0  # Backtrack

        return m * n if maxArea == 0 else maxArea  # If the grid was full of 1s

    def largestIsland(self, grid: List[List[int]]) -> int:
        return self.findLargestIsland(grid)


Approach1 = Solution


# Approach - 2 - Better Brute Force DFS (you can do BFS as well)
# T.C : O(n^4)
# S.C : O(n^2)
class Solution:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def DFS(self, grid: List[List[int]], i: int, j: int, visited: List[List[bool]]) -> int:
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == 0 or visited[i][j]:
            return 0

        visited[i][j] = True
        count = 1

        for dir in self.directions:
            count += self.DFS(grid, i + dir[0], j + dir[1], visited)

        return count

    def findLargestIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        m, n = self.m, self.n
        maxArea = 0
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    size = self.DFS(grid, i, j, visited)
                    maxArea = max(maxArea, size)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # Try converting each 0 to 1
                    grid[i][j] = 1

                    visited = [[False] * n for _ in range(n)]
                    size = self.DFS(grid, i, j, visited)

                    maxArea = max(maxArea, size)
                    grid[i][j] = 0  # Backtrack

        return m * n if maxArea == 0 else maxArea  # If the grid was full of 1s

    def largestIsland(self, grid: List[List[int]]) -> int:
        return self.findLargestIsland(grid)


Approach2 = Solution


# Approach - 3  - Optimal DFS (You can use BFS as well)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def DFS(self, grid: List[List[int]], i: int, j: int, id: int) -> int:
        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] != 1:
            return 0

        grid[i][j] = id
        count = 1

        for dir in self.directions:
            x = i + dir[0]
            y = j + dir[1]

            count += self.DFS(grid, x, y, id)

        return count

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        m, n = self.m, self.n
        maxArea = 0
        mp = {}  # unordered_map<int, int>
        island_id = 2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    size = self.DFS(grid, i, j, island_id)
                    maxArea = max(maxArea, size)
                    mp[island_id] = size
                    island_id += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    st = set()
                    for dir in self.directions:
                        x = i + dir[0]
                        y = j + dir[1]
                        if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] != 0:
                            st.add(grid[x][y])

                    sum = 1  # converting current 0 to 1
                    for s in st:
                        sum += mp[s]
                    maxArea = max(maxArea, sum)

        return maxArea


Approach3 = Solution


# Approach-4 (Using DSU)
# T.C : O(m*n * alpha(m*n))
# S.C : O(m*n)
class DSU:

    def __init__(self, n: int):
        self.parent = [0] * n
        self.size = [1] * n
        for i in range(n):
            self.parent[i] = i

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        if self.size[rootX] > self.size[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]

    def getSize(self, x: int) -> int:
        return self.size[self.find(x)]


class Solution:
    # Global directions array
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        totalCells = n * n
        dsu = DSU(totalCells)
        maxArea = 0

        # Step 1: Connect all existing 1s using DSU
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    idx = i * n + j
                    for dir in self.directions:
                        i_ = i + dir[0]
                        j_ = j + dir[1]
                        idx_ = i_ * n + j_
                        if i_ >= 0 and i_ < n and j_ >= 0 and j_ < n and grid[i_][j_] == 1:
                            dsu.Union(idx, idx_)

        # Step 2: Find the largest island without modification
        for idx in range(totalCells):
            if grid[idx // n][idx % n] == 1:
                maxArea = max(maxArea, dsu.getSize(idx))

        # Step 3: Try flipping each 0 to 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    uniqueParents = set()
                    for dir in self.directions:
                        i_ = i + dir[0]
                        j_ = j + dir[1]
                        idx_ = i_ * n + j_
                        if i_ >= 0 and i_ < n and j_ >= 0 and j_ < n and grid[i_][j_] == 1:
                            uniqueParents.add(dsu.find(idx_))

                    newSize = 1  # Flip this 0 to 1
                    for parent in uniqueParents:
                        newSize += dsu.getSize(parent)
                    maxArea = max(maxArea, newSize)

        return maxArea


Approach4 = Solution

# (The Java section of the original file duplicates the above and is skipped.)


if __name__ == "__main__":
    import sys, copy
    sys.setrecursionlimit(10**6)
    for S in (Approach1, Approach3, Approach4):
        assert S().largestIsland(copy.deepcopy([[1, 0], [0, 1]])) == 3
        assert S().largestIsland(copy.deepcopy([[1, 1], [1, 0]])) == 4
        assert S().largestIsland(copy.deepcopy([[1, 1], [1, 1]])) == 4
    # Approach2 (kept exactly as the instructor wrote it) checked on the same examples
    for g, exp in (([[1, 0], [0, 1]], 3), ([[1, 1], [1, 0]], 4), ([[1, 1], [1, 1]], 4)):
        assert Approach2().largestIsland(copy.deepcopy(g)) == exp
    print("ok")

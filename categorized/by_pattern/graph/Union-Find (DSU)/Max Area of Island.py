# Company Tags  : Amazon
# Leetcode Link : https://leetcode.com/problems/max-area-of-island/
#
# The BFS and DFS approaches are present in "Interview_DS_Algo/Graph/BFS_DFS" repository
# Link to BFS/DFS : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/BFS_DFS/Max_Area_of_Island.cpp

from typing import List


class UnionFind:
    def __init__(self, m: int, n: int):
        self.parent = [i for i in range(m * n)]

        self.size = [1] * (m * n)  # initially size of each group is 1 (itself)
        self.rank = [0] * (m * n)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
            return self.parent[x]

        return x

    # this is the trick, we return size of group after uniting the nodes in a group
    # Union by rank compression
    def Union(self, x: int, y: int) -> int:
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x == p_y:
            return self.size[p_x]

        if self.rank[p_x] > self.rank[p_y]:
            self.parent[p_y] = p_x
            self.size[p_x] += self.size[p_y]
            return self.size[p_x]
        elif self.rank[p_y] > self.rank[p_x]:
            self.parent[p_x] = p_y
            self.size[p_y] += self.size[p_x]
            return self.size[p_y]
        else:
            self.parent[p_x] = p_y
            self.size[p_y] += self.size[p_x]
            self.rank[p_y] += 1
            return self.size[p_y]

    def getGroupSize(self, x: int) -> int:
        # first find the parent of x (which represents the group)
        px = self.find(x)
        return self.size[px]


class Solution:
    def __init__(self):
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.m = 0
        self.n = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        m, n = self.m, self.n
        result = 0
        uf = UnionFind(m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    result = max(result, self.link(i, j, grid, uf))

        return result

    def link(self, i: int, j: int, grid: List[List[int]], uf: UnionFind) -> int:
        """
            Below is a general way of findind index of an
            element of a 2-d matrix visualzied in a 1-d matrix
        """
        n = self.n
        index = i * n + j

        size = uf.getGroupSize(index)

        def isSafe(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1

        for dir in self.directions:
            x = i + dir[0]
            y = j + dir[1]

            if isSafe(x, y):
                size = max(size, uf.Union(index, x * n + y))
        return size


Approach1 = Solution


if __name__ == "__main__":
    g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    assert Solution().maxAreaOfIsland(g) == 6
    assert Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    print("ok")

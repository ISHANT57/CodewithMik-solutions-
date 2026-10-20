# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=yYKGNW6Y7BA
# Company Tags                : Paytm, Amazon, Microsoft, Samsung, Snapdeal, Citrix, D-E-Shaw, Ola Cabs, Visa, Linkedin, Opera, Streamoid Technologies, Informatica
# Leetcode Qn Link            : https://leetcode.com/problems/number-of-islands/

from typing import List
from collections import deque


# Approach-1 (DFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        # You can also use lambda function for checking if next cell is valid or not
        # isSafe = lambda i, j: not (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1')

        grid[i][j] = '$'

        for p in self.dir:
            i_ = i + p[0]
            j_ = j + p[1]
            self.dfs(grid, i_, j_)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count


Approach1 = Solution


# Approach-2 (BFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(self, grid: List[List[str]], i: int, j: int, que: deque) -> None:
        que.append((i, j))
        grid[i][j] = '$'

        # lambda function (You can also add if check instead of lambda)
        def isSafe(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return False
            return True

        while que:
            curr = que.popleft()

            for p in self.dir:
                i_ = curr[0] + p[0]
                j_ = curr[1] + p[1]

                if isSafe(i_, j_):
                    que.append((i_, j_))
                    grid[i_][j_] = '$'

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        que = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j, que)
                    count += 1

        return count


Approach2 = Solution

# (Java section of the original file skipped: duplicates of the C++ approaches)

if __name__ == "__main__":
    def g():
        return [list("11110"), list("11010"), list("11000"), list("00000")]

    def g2():
        return [list("11000"), list("11000"), list("00100"), list("00011")]

    for S in (Approach1, Approach2):
        assert S().numIslands(g()) == 1
        assert S().numIslands(g2()) == 3
    print("ok")

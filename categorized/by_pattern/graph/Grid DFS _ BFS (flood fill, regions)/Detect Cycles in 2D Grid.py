#     Scroll below to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=gpHzIs3xXkU
#     Company Tags                : will update later
#     Leetcode Link               : https://leetcode.com/problems/detect-cycles-in-2d-grid

from typing import List
from collections import deque


# ****************************************************************** C++ (ported to Python) ******************************************************************
# Approach-1 (Using DFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    def cycleDetectDFS(self, r: int, c: int, prev_r: int, prev_c: int,
                       grid: List[List[str]], visited: List[List[bool]]) -> bool:

        if visited[r][c]:
            return True

        visited[r][c] = True

        # explore neighbours
        for dir in self.directions:
            new_r = r + dir[0]
            new_c = c + dir[1]

            if (new_r >= 0 and new_r < self.m and new_c >= 0 and new_c < self.n
                    and grid[new_r][new_c] == grid[r][c]):
                if new_r == prev_r and new_c == prev_c:
                    continue

                if self.cycleDetectDFS(new_r, new_c, r, c, grid, visited):
                    return True

        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.m = len(grid)
        self.n = len(grid[0])

        visited = [[False] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if not visited[i][j] and self.cycleDetectDFS(i, j, i, j, grid, visited):
                    return True

        return False


Approach1 = Solution


# Approach-2 (Using BFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    def cycleDetectBFS(self, r: int, c: int, grid: List[List[str]], visited: List[List[bool]]) -> bool:
        # r, c, prev_r, prev_c
        que = deque()

        que.append((r, c, -1, -1))
        visited[r][c] = True

        while que:
            curr_r, curr_c, prev_r, prev_c = que.popleft()

            # explore neighbours
            for dir in self.directions:
                new_r = curr_r + dir[0]
                new_c = curr_c + dir[1]

                if (new_r >= 0 and new_r < self.m and new_c >= 0 and new_c < self.n
                        and grid[new_r][new_c] == grid[curr_r][curr_c]):

                    if new_r == prev_r and new_c == prev_c:
                        continue

                    if visited[new_r][new_c]:
                        return True

                    visited[new_r][new_c] = True

                    que.append((new_r, new_c, curr_r, curr_c))

        return False

    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.m = len(grid)
        self.n = len(grid[0])

        visited = [[False] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if not visited[i][j] and self.cycleDetectBFS(i, j, grid, visited):
                    return True

        return False


Approach2 = Solution


if __name__ == "__main__":
    g1 = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]
    g2 = [["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]
    g3 = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]
    for cls in (Approach1, Approach2):
        assert cls().containsCycle(g1) is True
        assert cls().containsCycle(g2) is True
        assert cls().containsCycle(g3) is False
    print("ok")

#     Scroll below to see JAVA code also (Java section skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=KVm0XBHxQtQ
#     Company Tags                : will update later
#     Leetcode Link               : https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid

from typing import List


# ****************************************************************** C++ (ported to Python) ******************************************************************
# Approach (Using DFS)
# T.C : O(m*n)
# S.C : O(m*n)
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

        self.directions = {
            1: [[0, -1], [0, 1]],
            2: [[-1, 0], [1, 0]],
            3: [[0, -1], [1, 0]],
            4: [[0, 1], [1, 0]],
            5: [[0, -1], [-1, 0]],
            6: [[-1, 0], [0, 1]],
        }

    def dfs(self, grid: List[List[int]], i: int, j: int, visited: List[List[bool]]) -> bool:
        if i == self.m - 1 and j == self.n - 1:
            return True

        visited[i][j] = True

        for dir in self.directions[grid[i][j]]:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if new_i < 0 or new_i >= self.m or new_j < 0 or new_j >= self.n or visited[new_i][new_j]:
                continue

            # IMPORTANT = can you come back to i and j from new_i and new_j
            for backDir in self.directions[grid[new_i][new_j]]:
                if new_i + backDir[0] == i and new_j + backDir[1] == j:
                    if self.dfs(grid, new_i, new_j, visited):
                        return True

        return False

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.m = len(grid)
        self.n = len(grid[0])

        visited = [[False] * self.n for _ in range(self.m)]
        # T.C : O(m*n)

        return self.dfs(grid, 0, 0, visited)


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.hasValidPath([[2, 4, 3], [6, 5, 2]]) is True
    assert Solution().hasValidPath([[1, 2, 1], [1, 2, 1]]) is False
    assert Solution().hasValidPath([[1, 1, 2]]) is False
    print("ok")

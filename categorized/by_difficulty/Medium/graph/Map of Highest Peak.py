# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=nQe5OBs0FgQ
# Company Tags                : Google, Microsoft
# Leetcode Link               : https://leetcode.com/problems/map-of-highest-peak/description/

from typing import List
from collections import deque


# Approach - Using Multi-Source BFS
# T.C : O(m * n) , We will visit all cells once
# S.C : O(m * n), in worst case queue will contain all the cells
class Solution:
    # typedef pair<int, int> P  -> tuple (i, j)
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        height = [[-1] * n for _ in range(m)]

        que = deque()
        # Height of water cells must be 0 only
        # T.C : O(m*n)
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:  # this cell is water
                    height[i][j] = 0  # This is a source for hitting BFS
                    que.append((i, j))

        # Apply khandani template - Multi source BFS ka
        # T.C : O(m*n)
        # S.C : O(m*n)
        while que:
            N = len(que)

            while N > 0:
                N -= 1
                curr = que.popleft()

                i = curr[0]
                j = curr[1]

                for dir in self.directions:
                    i_ = i + dir[0]
                    j_ = j + dir[1]

                    if i_ >= 0 and i_ < m and j_ >= 0 and j_ < n and height[i_][j_] == -1:
                        height[i_][j_] = height[i][j] + 1
                        que.append((i_, j_))

        return height


Approach1 = Solution

# (Java section of the original file skipped: duplicate of the C++ approach)

if __name__ == "__main__":
    assert Solution().highestPeak([[0, 1], [0, 0]]) == [[1, 0], [2, 1]]
    assert Solution().highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]) == [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
    print("ok")

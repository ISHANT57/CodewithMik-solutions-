# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Jiu0jqm0mB0
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/rotting-oranges/description/

from typing import List
from collections import deque


# Approach - Using Multi-Source BFS
# T.C : O(m * n) , We will visit all cells once
# S.C : O(m * n), in worst case queue will contain all the cells
class Solution:
    # typedef pair<int, int> P  -> tuple (i, j)
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        que = deque()
        freshCount = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j))  # Storing all possible sources at once in the queue
                elif grid[i][j] == 1:
                    freshCount += 1

        if freshCount == 0:
            return 0

        def isSafe(x, y):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]) and grid[x][y] == 1

        # Applying Multi-Source BFS
        time = 0
        while que:
            n = len(que)
            # because we want to cover all neighbours of a node
            # at once which are affected in a particular time frame
            while n > 0:
                n -= 1
                curr = que.popleft()
                i = curr[0]
                j = curr[1]

                for dir in self.directions:
                    new_i = i + dir[0]
                    new_j = j + dir[1]

                    if isSafe(new_i, new_j):
                        grid[new_i][new_j] = 2
                        que.append((new_i, new_j))
                        freshCount -= 1
            time += 1

        return time - 1 if freshCount == 0 else -1


Approach1 = Solution

# (Java section of the original file skipped: duplicate of the C++ approach)

if __name__ == "__main__":
    assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert Solution().orangesRotting([[0, 2]]) == 0
    print("ok")

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Q4bqto_yG6I
# Company Tags                : Similar Problem asked in Samsung
# Leetcode Link               : https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from typing import List
from collections import deque


# Simply Use BFS :
# Time  - O(m*n)
# Space - O(m+n)
class Solution:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        que = deque()
        que.append((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = '+'  # marking it visited
        steps = 0

        while que:
            size = len(que)

            while size:
                size -= 1
                temp = que.popleft()

                if (temp != (entrance[0], entrance[1]) and
                        (temp[0] == 0 or temp[0] == m - 1 or temp[1] == 0 or temp[1] == n - 1)):
                    return steps

                for dir in self.directions:
                    i = temp[0] + dir[0]
                    j = temp[1] + dir[1]

                    if i >= 0 and i < m and j >= 0 and j < n and maze[i][j] != '+':
                        que.append((i, j))
                        maze[i][j] = '+'  # marking it as visited

            steps += 1

        return -1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1, 2]) == 1
    assert Solution().nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], [1, 0]) == 2
    assert Solution().nearestExit([[".","+"]], [0, 0]) == -1
    print("ok")

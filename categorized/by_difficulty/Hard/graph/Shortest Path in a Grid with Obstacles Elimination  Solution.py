# MY YOUTUBE VIDE ON THIS Qn : https://www.youtube.com/watch?v=zpOhlTndBv0
# Company Tags               : Google
# Leetcode Link              : https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from typing import List
from collections import deque


# Approach-1 - BFS
class Solution:
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        que = deque()

        i = 0
        j = 0
        que.append([i, j, k])

        # C++ used bool visited[41][41][1601]; here sized from the input (obs ranges 0..k)
        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

        steps = 0
        while que:
            size = len(que)
            while size > 0:
                size -= 1
                temp = que.popleft()
                curr_i = temp[0]
                curr_j = temp[1]
                obs = temp[2]

                if curr_i == m - 1 and curr_j == n - 1:
                    return steps

                for dir in self.directions:

                    new_i = curr_i + dir[0]
                    new_j = curr_j + dir[1]

                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                        continue

                    if grid[new_i][new_j] == 0 and not visited[new_i][new_j][obs]:
                        que.append([new_i, new_j, obs])
                        visited[new_i][new_j][obs] = True
                    elif grid[new_i][new_j] == 1 and obs > 0 and not visited[new_i][new_j][obs - 1]:
                        que.append([new_i, new_j, obs - 1])
                        visited[new_i][new_j][obs - 1] = True

            steps += 1

        return -1


Approach1 = Solution


# Approach-2 - BFS : (little simplified)
class Solution:
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        obs = [[float('inf')] * n for _ in range(m)]  # INT_MAX

        que = deque()
        que.append([0, 0, 0])

        obs[0][0] = 0  # Number of obstacles faced till this index (i, j)

        steps = 0
        while que:
            N = len(que)

            while N > 0:
                N -= 1
                curr = que.popleft()
                x = curr[0]
                y = curr[1]

                if x == m - 1 and y == n - 1:
                    return steps

                for dir in self.dirs:
                    new_x = x + dir[0]
                    new_y = y + dir[1]

                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                        currObstacle = curr[2] + grid[new_x][new_y]
                        if currObstacle >= obs[new_x][new_y] or currObstacle > k:
                            continue

                        obs[new_x][new_y] = currObstacle
                        que.append([new_x, new_y, currObstacle])

            steps += 1

        return -1


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1) == 6
        assert S().shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1) == -1
    print("ok")

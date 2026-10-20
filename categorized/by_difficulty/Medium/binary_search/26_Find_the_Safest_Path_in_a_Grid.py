# Scroll below to see JAVA code also (Java section not ported: this file is the Python 3 port of the C++ code)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=8I0Z_eajcvs
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/find-the-safest-path-in-a-grid/description/

from collections import deque
from typing import List


# ************************************************************ C++ (ported to Python) ************************************************************************
# T.C : O(log(n) * n^2)
# S.C : O(n^2)
class Solution:
    def __init__(self):
        self.n = 0

        self.directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    def check(self, distNearestThief: List[List[int]], sf: int) -> bool:
        n = self.n
        que = deque()

        visited = [[False] * n for _ in range(n)]
        # 0,0 --> n-1, n-1
        que.append((0, 0))
        visited[0][0] = True

        if distNearestThief[0][0] < sf:
            return False

        while que:
            curr_i, curr_j = que.popleft()

            if curr_i == n - 1 and curr_j == n - 1:
                return True

            for dir in self.directions:
                new_i = curr_i + dir[0]
                new_j = curr_j + dir[1]

                if 0 <= new_i < n and 0 <= new_j < n and visited[new_i][new_j] != True:
                    if distNearestThief[new_i][new_j] < sf:
                        continue  # reject this cell
                    que.append((new_i, new_j))
                    visited[new_i][new_j] = True

        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        self.n = n

        # Step-1 Precalculation of distNearestThief - for each cell
        distNearestThief = [[-1] * n for _ in range(n)]
        que = deque()
        visited = [[False] * n for _ in range(n)]

        # push all cells in queue where theives are present
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    que.append((i, j))
                    visited[i][j] = True

        level = 0
        while que:
            size = len(que)

            while size > 0:
                size -= 1
                curr_i, curr_j = que.popleft()
                distNearestThief[curr_i][curr_j] = level
                for dir in self.directions:
                    new_i = curr_i + dir[0]
                    new_j = curr_j + dir[1]

                    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or visited[new_i][new_j]:
                        continue

                    que.append((new_i, new_j))
                    visited[new_i][new_j] = True

            level += 1

        # Step-2 Apply binary search on SF
        l = 0
        r = 400
        result = 0

        while l <= r:
            mid_sf = l + (r - l) // 2

            if self.check(distNearestThief, mid_sf):
                result = mid_sf
                l = mid_sf + 1
            else:
                r = mid_sf - 1

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0
    assert s.maximumSafenessFactor([[0, 0, 1], [0, 0, 0], [0, 0, 0]]) == 2
    assert s.maximumSafenessFactor([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]) == 2
    print("ok")

#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=UQogvDBoHe4
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner

from typing import List
import heapq

INT_MAX = 2**31 - 1

# Approach (Using Dijkstra's Algorothm - Assuming obstacle with edge weight 1 and empty with 0)
# T.C : O(m*n log(m*n))
# S.C : O(m*n)
class Solution:
    # P = pair<int, pair<int,int>> -> (d, (i, j)) tuples
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        result = [[INT_MAX] * n for _ in range(m)]
        # result[i][j] = minimum distance/obstacleCount between [0][0] to [i][j]
        result[0][0] = 0

        pq = []  # min-heap
        heapq.heappush(pq, (0, (0, 0)))  # {wt, {i, j}}
        # O(Elog(V))
        # E = number of edges
        # V = number of vertices
        while pq:
            curr = heapq.heappop(pq)

            d = curr[0]
            i = curr[1][0]
            j = curr[1][1]

            for dir in self.directions:
                x = i + dir[0]
                y = j + dir[1]

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                wt = 1 if grid[x][y] == 1 else 0

                if d + wt < result[x][y]:
                    result[x][y] = d + wt
                    heapq.heappush(pq, (d+wt, (x, y)))

        return result[m-1][n-1]

Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]) == 2
    assert s.minimumObstacles([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]) == 0
    print("ok")

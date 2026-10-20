#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=DzfmJoFq1pc
#     Company Tags                : Samsung
#     GfG Link                    : https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

from typing import List


# Time Complexity - O(n^3)
class Solution:
    def shortest_distance(self, grid: List[List[int]]) -> None:
        n = len(grid)

        for i in range(n):
            for j in range(n):

                if grid[i][j] == -1:
                    grid[i][j] = 100000

        for via in range(n):

            for i in range(n):
                for j in range(n):

                    grid[i][j] = min(grid[i][j], grid[i][via] + grid[via][j])

        for i in range(n):
            for j in range(n):

                if grid[i][j] == 100000:
                    grid[i][j] = -1


Approach1 = Solution


if __name__ == "__main__":
    g = [[0, 25], [-1, 0]]
    Solution().shortest_distance(g)
    assert g == [[0, 25], [-1, 0]]
    g = [[0, 1, 43], [1, 0, 6], [-1, -1, 0]]
    Solution().shortest_distance(g)
    assert g == [[0, 1, 7], [1, 0, 6], [-1, -1, 0]], g
    print("ok")

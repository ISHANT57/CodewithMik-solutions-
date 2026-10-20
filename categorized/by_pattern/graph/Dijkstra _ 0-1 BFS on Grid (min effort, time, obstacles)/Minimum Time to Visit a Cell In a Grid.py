#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=2H9CVEmmMUM
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid

from typing import List
import heapq

INT_MAX = 2**31 - 1

# Approach-1 (Using Dijkstra's Algorothm) - STORING RESULT IN 2D Matrix
# T.C : O(m*n log(m*n))
# S.C : O(m*n)
class Solution:
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # P = pair<int, pair<int,int>> -> (time, (row, col)) tuples

    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        visited = [[False] * n for _ in range(m)]
        result = [[INT_MAX] * n for _ in range(m)]
        pq = []  # min-heap

        heapq.heappush(pq, (grid[0][0], (0, 0)))  # Start at top-left corner
        result[0][0] = 0
        while pq:
            # Get the current time, row, and column
            time, (row, col) = heapq.heappop(pq)

            # Reached destination
            if row == m - 1 and col == n - 1:
                return result[m-1][n-1]

            # Mark the current cell as visited
            if visited[row][col]:
                continue
            visited[row][col] = True

            # Explore the neighboring cells
            for dir in self.direction:
                r = row + dir[0]
                c = col + dir[1]
                if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                    continue

                if grid[r][c] <= time+1:
                    heapq.heappush(pq, (time+1, (r, c)))
                    result[r][c] = time+1
                elif (grid[r][c]-time) % 2 == 0:
                    heapq.heappush(pq, (grid[r][c]+1, (r, c)))
                    result[r][c] = grid[r][c]+1
                else:
                    heapq.heappush(pq, (grid[r][c], (r, c)))
                    result[r][c] = grid[r][c]
        return -1

Approach1 = Solution


# Approach-2 (Using Dijkstra's Algorothm) - Without Storing result in a 2D Matrix
# T.C : O(m*n log(m*n))
# S.C : O(m*n)
class Solution:
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # P = pair<int, pair<int,int>> -> (time, (row, col)) tuples

    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        visited = [[False] * n for _ in range(m)]
        pq = []  # min-heap

        heapq.heappush(pq, (grid[0][0], (0, 0)))  # Start at top-left corner
        while pq:
            # Get the current time, row, and column
            time, (row, col) = heapq.heappop(pq)

            # Reached destination
            if row == m - 1 and col == n - 1:
                return time

            # Mark the current cell as visited
            if visited[row][col]:
                continue
            visited[row][col] = True

            # Explore the neighboring cells
            for dir in self.direction:
                r = row + dir[0]
                c = col + dir[1]
                if r < 0 or r >= m or c < 0 or c >= n or visited[r][c]:
                    continue

                if grid[r][c] <= time+1:
                    heapq.heappush(pq, (time+1, (r, c)))
                elif (grid[r][c]-time) % 2 == 0:
                    heapq.heappush(pq, (grid[r][c]+1, (r, c)))
                else:
                    heapq.heappush(pq, (grid[r][c], (r, c)))
        return -1

Approach2 = Solution


if __name__ == "__main__":
    for sol in (Approach1, Approach2):
        assert sol().minimumTime([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]) == 7
        assert sol().minimumTime([[0, 2, 4], [3, 2, 1], [1, 0, 4]]) == -1
    print("ok")

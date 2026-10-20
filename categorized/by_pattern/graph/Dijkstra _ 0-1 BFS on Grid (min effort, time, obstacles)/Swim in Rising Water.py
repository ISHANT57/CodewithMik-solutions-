#     Scroll below to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=9WYhuzn8hd8
#     Company Tags                : Amazon
#     Leetcode Link               : https://leetcode.com/problems/swim-in-rising-water/
#
#     The question can be stated as follows: there are multiple paths from (0, 0) to (n - 1, n - 1),
#     each path has a max value from all of the steps .
#     And what is smallest of that value res in the path among all of them ?
#
#     Similar Question - Leetcode : 1102 (Path With Maximum Minimum Value) (Premium Question)

import heapq
import sys
from typing import List

sys.setrecursionlimit(10000)


# ************************************ C++ (ported to Python) ************************************
# Approach -1 (Binary Search + BFS) Time : O(n^2 * log(n))
# NOTE - In the paths, we have to find the maximum from the minimum path (Minimize the Maximum Hints towards Binary Search)
# T.C : O(n^2 * log(n^2)) = O(n^2 log n)
# S.C : O(n^2) for visited
class Solution:
    def __init__(self):
        self.n = 0
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.visited = []

    def reachable(self, grid: List[List[int]], i: int, j: int, mid: int) -> bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n or self.visited[i][j] or grid[i][j] > mid:
            return False

        self.visited[i][j] = True

        if i == self.n - 1 and j == self.n - 1:
            return True

        for dir in self.directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if self.reachable(grid, new_i, new_j, mid):
                return True

        return False

    def swimInWater(self, grid: List[List[int]]) -> int:
        self.n = len(grid)

        l, r = grid[0][0], self.n * self.n - 1
        result = 0

        while l <= r:
            mid = l + (r - l) // 2
            self.visited = [[False] * self.n for _ in range(self.n)]

            if self.reachable(grid, 0, 0, mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


Approach1 = Solution


# Approach-2 Dijkstra's Algo (priority_queue) Time : O(n^2 * log(n))
# Single Source, Single Destination, We have to find the shortest path to reach m-1, n-1 and in the process, calculate result
# T.C : O(n^2 * log(n^2)) = O(n^2 log n) --- Because TC of Dijkstra if E*logV where E = number of edges, V = number of vertices
# S.C : O(n^2) for visited
class Solution:
    def __init__(self):
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = [[2**31 - 1] * n for _ in range(n)]

        pq = []  # min-heap by time, entries (time, (i, j)) (pair<int, pair<int,int>>)
        result[0][0] = grid[0][0]
        heapq.heappush(pq, (grid[0][0], (0, 0)))

        while pq:
            currTime, cell = heapq.heappop(pq)
            i, j = cell

            # if we reached destination, return time
            if i == n - 1 and j == n - 1:
                return currTime

            # Skip if we've already found a better path
            if currTime > result[i][j]:
                continue

            for dir in self.directions:
                i_ = i + dir[0]
                j_ = j + dir[1]
                if 0 <= i_ < n and 0 <= j_ < n:
                    nextTime = max(currTime, grid[i_][j_])

                    if nextTime < result[i_][j_]:
                        result[i_][j_] = nextTime
                        heapq.heappush(pq, (nextTime, (i_, j_)))

        return -1  # should never reach here


Approach2 = Solution

if __name__ == "__main__":
    g1 = [[0, 2], [1, 3]]
    g2 = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    for A in (Approach1, Approach2):
        assert A().swimInWater(g1) == 3
        assert A().swimInWater(g2) == 16
    print("ok")

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=QIu9HeyEjPc
#     Company Tags                : GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/path-with-minimum-effort/
#
# NOTE: the original C++ declares `dirs` but loops over an undeclared `directions`
#       (does not compile as written). Here the loop uses `dirs`, the evident intent.

from typing import List
import heapq

INT_MAX = 2**31 - 1

# Approach-1 : Using Dijkstra's Algo
class Solution:
    # P = pair<int, pair<int,int>> -> (diff, (x, y)) tuples
    dirs = [
                [-1, 0],
        [0, -1],        [0, 1],
                [1, 0]
    ]
    # Interesting right :-)

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        def isSafe(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        result = [[INT_MAX] * n for _ in range(m)]
        pq = []  # min-heap

        heapq.heappush(pq, (0, (0, 0)))
        result[0][0] = 0

        while pq:
            diff, node = heapq.heappop(pq)

            x = node[0]
            y = node[1]

            # Why returning now ?
            # Because there is no way that the rest of elements can update the weight of destination cell even smaller due to the min heap.
            if x == m-1 and y == n-1:
                return diff

            for dir in self.dirs:
                x_ = x + dir[0]
                y_ = y + dir[1]

                if isSafe(x_, y_):

                    newDiff = max(diff, abs(heights[x][y] - heights[x_][y_]))
                    if result[x_][y_] > newDiff:
                        result[x_][y_] = newDiff
                        heapq.heappush(pq, (result[x_][y_], (x_, y_)))

        return result[m-1][n-1]

Approach1 = Solution


# Approach-2 (Binary Search + DFS)
# Will update, soon


if __name__ == "__main__":
    s = Solution()
    assert s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    print("ok")
